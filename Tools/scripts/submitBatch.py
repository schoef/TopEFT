#!/usr/bin/env python
"""
Usage:
submitBatch.py path/to/file_with_commands
or
submitBatch.py "command"

Will submit a batch job for each command line in the file_with_commands.
--dpm: Will create proxy certificate.
"""

# Standard imports
import hashlib, time
import os
import re


# some defaults
batch_job_file="batch_job"

# user info
hephy_user = os.getenv("USER")
hephy_user_initial = os.getenv("USER")[0]

# info on hosts (heplx or lxplus)
hostname = os.getenv("HOSTNAME")
hosts_info = {
            'heplx' : {'site': 'hephy.at' , 'batch':'slurm'   ,'def_opts':''},
            'worker' : {'site': 'hephy.at' , 'batch':'slurm'   ,'def_opts':''},
            'lxplus': {'site': 'cern.ch'  , 'batch':'lxbatch' ,'def_opts':'-q 8nh'}
        }
host   = [ h for h in hosts_info.keys() if h in hostname ]
if not len(host)==1:
    raise Exception("Host name (%s) was not recognized in hosts_info=%s"%(hostname, hosts_info) )
else:
    host = host[0]

host_info = hosts_info[host]
submit_time = time.strftime("%a%H%M%S", time.localtime())

# Parser
from optparse import OptionParser
parser = OptionParser()
parser.add_option("--title", dest="title",
                  help="Job Title on batch", default = "batch" )
parser.add_option("--output", dest="output", 
                  default="/afs/hephy.at/work/%s/%s/batch_output/"%(hephy_user_initial, hephy_user),
                  help="path for batch output ")
parser.add_option("--qos", dest="qos",
                  help="Job Title viewied in squeue", default = "" )
parser.add_option("--opts", dest="opts",
                  help="Give a string for any extra options", default = host_info['def_opts'] )
parser.add_option('--dpm', dest="dpm", default=False, action='store_true', help="Use dpm?")

parser.add_option('--logLevel', action='store', nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], default='INFO', help="Log level for logging" )

(options,args) = parser.parse_args()


# Logging
import TopEFT.Tools.logger as logger
logger  = logger.get_logger(options.logLevel, logFile = None)

# Arguments
batch_job_title  = options.title
batch_output_dir = options.output
qos              = options.qos
qos_options      = ['1h']

if qos and qos not in qos_options:
    raise Exception("The queue option (%s) is not recognized .... it should be one of %s"%(qos, qos_options))

def make_batch_job( batch_job_file, batch_job_title, batch_output_dir , command ):
    # If X509_USER_PROXY is set, use existing proxy.
    if options.dpm:
        if host == 'lxplus':
            from StopsDilepton.Tools.user import cern_proxy_certificate
            proxy_location = cern_proxy_certificate
        else:
            proxy_location = None

        from RootTools.core.helpers import renew_proxy
        proxy = renew_proxy( proxy_location )

        logger.info( "Using proxy certificate %s", proxy )
        proxy_cmd = "export X509_USER_PROXY=%s"%proxy
    else:
        proxy_cmd = ""            

    import subprocess

    if host == 'heplx':
        template =\
"""\
#!/bin/sh
#SBATCH -J {batch_job_title}
#SBATCH -D {pwd}
#SBATCH -o {batch_output_dir}batch-test.%j.out

{proxy_cmd}
voms-proxy-info -all
eval \`"scram runtime -sh"\` 
echo CMSSW_BASE: {cmssw_base} 
echo Executing user command  
echo "{command}"
{command} 

voms-proxy-info -all

""".format(\
                command          = command,
                cmssw_base       = os.getenv("CMSSW_BASE"),
                batch_output_dir = batch_output_dir,
                batch_job_title  = batch_job_title,
                pwd              = os.getenv("PWD"),
                proxy_cmd = proxy_cmd
              )
    elif host == 'lxplus':
        template =\
"""\
#!/bin/bash
export CMSSW_PROJECT_SRC={cmssw_base}/src

cd $CMSSW_PROJECT_SRC
eval `scramv1 ru -sh`

alias python={python_release}
which python
python --version

{proxy_cmd}
voms-proxy-info -all
echo CMSSW_BASE: $CMSSW_BASE
cd {pwd}
echo Executing user command while in $PWD
echo "{command}"
{command} 

voms-proxy-info -all

""".format(\
                command          = command,
                cmssw_base       = os.getenv("CMSSW_BASE"),
                #batch_output_dir = batch_output_dir,
                #batch_job_title  = batch_job_title,
                pwd              = os.getenv("PWD"),
                proxy_cmd = proxy_cmd,
                python_release = subprocess.check_output(['which', 'python']).rstrip(), 
              )

    batch_job = file(batch_job_file, "w")
    batch_job.write(template)
    batch_job.close()
    return

def getCommands( line ):
    commands = []
    split = None
    try:
        m=re.search(r"SPLIT[0-9][0-9]*", line)
        split=int(m.group(0).replace('SPLIT',''))
    except:
        pass 
    line = line.split('#')[0]
    if line:
        if split:
            logger.info( "Splitting in %i jobs", split )
            for i in range(split):
                commands.append(line+" --nJobs %i --job %i"%( split, i ))
        else:
            commands.append(line)
    return commands

if __name__ == '__main__':
    if not len(args) == 1:
        raise Exception("Only one argument accepted! Instead this was given: %s"%args)
    if os.path.isfile(args[0]):
        logger.info( "Reading commands from file: %s", args[0] )
        commands = []
        with open(args[0]) as f:
            for line in f.xreadlines():
                commands.extend( getCommands( line.rstrip("\n") ) )
                
    elif type(args[0]) == type(""):
        commands = getCommands( args[0] ) 
    if commands:
        logger.info( "Working on host %s", host )
        if host == 'heplx':
            if not os.path.isdir(batch_output_dir):
                os.mkdir(batch_output_dir)

            logger.info( "Batch system output file to be written to directory: %s", batch_output_dir )

            for command in commands:
                #job_file = tmp_job_dir +"/" + batch_job_file
                hash_string = hashlib.md5("%s"%time.time()).hexdigest()
                job_file = batch_job_file.rstrip(".sh")+"_%s.sh"%hash_string
                make_batch_job( job_file , batch_job_title, batch_output_dir , command  )
                os.system("sbatch %s %s"%(job_file , qos))
                os.remove(job_file)

        elif host == 'lxplus':
            opts = options.opts
            title= options.title
            title_opt = "-J %s"%title
            for command in commands:
                hash_string = hashlib.md5("%s"%time.time()).hexdigest()
                job_file = batch_job_file.rstrip(".sh")+"_%s.sh"%hash_string
                make_batch_job( job_file , batch_job_title, batch_output_dir , command  )
                submit_command = "bsub %s '%s'  < %s"%(opts , title_opt , job_file )
                os.system(submit_command)
                os.remove(job_file)
