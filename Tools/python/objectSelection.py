from TopEFT.Tools.helpers import mZ, getVarValue, getObjDict, deltaR
from math import *
import numbers

jetVars = ['eta','pt','phi','btagCSV', 'id', 'area', 'DFbb', 'DFb']

def getJets(c, jetVars=jetVars, jetColl="Jet"):
    return [getObjDict(c, jetColl+'_', jetVars, i) for i in range(int(getVarValue(c, 'n'+jetColl)))]

def isAnalysisJet(j, ptCut=30, absEtaCut=2.4, ptVar='pt'):
  return j[ptVar]>ptCut and abs(j['eta'])<absEtaCut and j['id']

def getGoodJets(c, ptCut=30, absEtaCut=2.4, jetVars=jetVars, jetColl="Jet"):
    return filter(lambda j:isAnalysisJet(j, ptCut=ptCut, absEtaCut=absEtaCut), getJets(c, jetVars, jetColl=jetColl))

def getAllJets(c, leptons, ptCut=30, absEtaCut=2.4, jetVars=jetVars, jetCollections=[ "Jet", "DiscJet"]):

    jets = sum( [ filter(lambda j:isAnalysisJet(j, ptCut=ptCut, absEtaCut=absEtaCut), getJets(c, jetVars, jetColl=coll)) for coll in jetCollections], [] )
    res  = []

    for jet in jets:
        clean = True
        for lepton in leptons:
            if deltaR(lepton, jet) < 0.4:
                clean = False
                break
        if clean:
            res.append(jet)

    res.sort( key = lambda j:-j['pt'] )

    return res

def isBJet(j, tagger = 'CSVv2'):
    if tagger == 'CSVv2':
        return j['btagCSV']>0.8484
    elif tagger == 'DeepCSV':
        return j['DFbb'] + j['DFb'] > 0.6324

def getGoodBJets(c, tagger = 'CSVv2'):
    return filter(lambda j:isBJet(j, tagger = tagger), getGoodJets(c))

def getGenLeps(c):
    return [getObjDict(c, 'genLep_', ['eta','pt','phi','charge', 'pdgId', 'sourceId'], i) for i in range(int(getVarValue(c, 'ngenLep')))]

def getGenParts(c):
    return [getObjDict(c, 'GenPart_', ['eta','pt','phi','charge', 'pdgId', 'motherId', 'grandmotherId'], i) for i in range(int(getVarValue(c, 'nGenPart')))]

genVars = ['eta','pt','phi','mass','charge', 'status', 'pdgId', 'motherId', 'grandmotherId','nDaughters','daughterIndex1','daughterIndex2','nMothers','motherIndex1','motherIndex2','isPromptHard'] 
def getGenPartsAll(c):
    return [getObjDict(c, 'genPartAll_', genVars, i) for i in range(int(getVarValue(c, 'ngenPartAll')))]

def alwaysTrue(*args, **kwargs):
  return True
def alwaysFalse(*args, **kwargs):
  return False

#https://twiki.cern.ch/twiki/bin/viewauth/CMS/SUSLeptonSF

def isoSelector( isolation="relIso03", barrelCut=0.2, endcapCut=0.2 ):

    def func(l):
        return (l[isolation]<barrelCut and abs(l["eta"])<1.479) or (abs(l["eta"])>1.479 and abs(l["eta"]<999) and l[isolation]<endcapCut)

    return func

# MUONS
def muonSelector(isoVar = "relIso04", barrelIso = 0.25, endcapIso = 0.25, absEtaCut = 2.4, dxy = 0.05, dz = 0.1, loose=False):

    iso_ = isoSelector( isolation=isoVar, barrelCut=barrelIso, endcapCut=endcapIso)

    def func(l, ptCut = 10):
        return \
            l["pt"]>=ptCut\
            and abs(l["pdgId"])==13\
            and abs(l["eta"])<absEtaCut\
            and l["ICHEPmediumMuonId"]>=1 \
            and iso_(l) \
            and l["sip3d"]<4.0\
            and abs(l["dxy"])<dxy\
            and abs(l["dz"])<dz

    def funcLoose(l, ptCut = 10):
        return \
            l["pt"]>=ptCut\
            and abs(l["pdgId"])==13\
            and abs(l["eta"])<absEtaCut\
            and iso_(l) \
            and abs(l["dxy"])<dxy\
            and abs(l["dz"])<dz

    return func if not loose else funcLoose

default_muon_selector = muonSelector( )

# ELECTRONS

ele_MVAID = {'M': {(0,0.8):0.837, (0.8, 1.479):0.715, (1.57, 999): 0.357}}

#ele_MVAID = {'M': {(0,0.8):0.913286 , (0.8, 1.479):0.805013, (1.57, 999): 0.358969},
#            'VL': {(0,0.8):-0.76, (0.8, 1.479):-0.52, (1.57, 999): -0.23}}

def eleMVAIDSelector( eleId ):
    ele_mva_WP = ele_MVAID[eleId]
    def func(l):
        abs_ele_eta = abs(l["eta"])
        for abs_ele_bin, mva_threshold in ele_mva_WP.iteritems():
            if abs_ele_eta>=abs_ele_bin[0] and abs_ele_eta<abs_ele_bin[1] and l["mvaIdSpring16"] > mva_threshold: return True
        return False
    return func

def eleCutIDSelector( ele_cut_Id = 4):
    def func(l):
        return l["eleCutId_Spring2016_25ns_v1_ConvVetoDxyDz"]>=ele_cut_Id 
    return func

def eleSelector(isoVar = "relIso03", barrelIso = 0.1, endcapIso = 0.1, absEtaCut = 2.5, dxy = 0.05, dz = 0.1, eleId = "M", noMissingHits=True, loose=False):

    iso_ = isoSelector( isolation=isoVar, barrelCut=barrelIso, endcapCut=endcapIso)
    

    if isinstance(eleId, numbers.Number): id_ = eleCutIDSelector( eleId )
    elif type(eleId)==type(""):           id_ = eleMVAIDSelector( eleId )
    else:                                 raise ValueError( "Don't know what to do with eleId %r" % eleId )

    def func(l, ptCut = 10):
        return \
            l["pt"]>=ptCut\
            and abs(l["eta"])<absEtaCut\
            and abs(l["pdgId"])==11\
            and id_(l)\
            and iso_(l)\
            and triggerEmulatorSelector(l)\
            and l["sip3d"]<4.0\
            and (l["lostHits"]==0 or not noMissingHits)\
            and abs(l["dxy"]) < dxy\
            and abs(l["dz"]) < dz

#            and triggerEmulatorSelector(l)\

    def funcLoose(l, ptCut = 10):
        return \
            l["pt"]>=ptCut\
            and abs(l["eta"])<absEtaCut\
            and abs(l["pdgId"])==11\
            and id_(l)\
            and iso_(l)\
            and abs(l["dxy"]) < dxy\
            and abs(l["dz"]) < dz

    return func if not loose else funcLoose

default_ele_selector = eleSelector( )

lepton_branches_data = 'pt/F,eta/F,etaSc/F,phi/F,pdgId/I,tightId/I,miniRelIso/F,relIso03/F,relIso04/F,sip3d/F,ICHEPmediumMuonId/I,mediumMuonId/I,lostHits/I,convVeto/I,dxy/F,dz/F,eleCutId_Spring2016_25ns_v1_ConvVetoDxyDz/I,mvaIdSpring16/F,hadronicOverEm/F,dEtaScTrkIn/F,dPhiScTrkIn/F,eInvMinusPInv/F,full5x5_sigmaIetaIeta/F,etaSc/F,mvaTTH/F,matchedTrgObj1Mu/F,matchedTrgObj1El/F'
lepton_branches_mc   = lepton_branches_data + ',mcMatchId/I,mcMatchAny/I'

leptonVars = [s.split('/')[0] for s in lepton_branches_mc.split(',')] 

def getLeptons(c, collVars=leptonVars):
    return [getObjDict(c, 'LepGood_', collVars, i) for i in range(int(getVarValue(c, 'nLepGood')))]
def getOtherLeptons(c, collVars=leptonVars):
    return [getObjDict(c, 'LepOther_', collVars, i) for i in range(int(getVarValue(c, 'nLepOther')))]
def getMuons(c, collVars=leptonVars):
    return [getObjDict(c, 'LepGood_', collVars, i) for i in range(int(getVarValue(c, 'nLepGood'))) if abs(getVarValue(c,"LepGood_pdgId",i))==13]
def getElectrons(c, collVars=leptonVars):
    return [getObjDict(c, 'LepGood_', collVars, i) for i in range(int(getVarValue(c, 'nLepGood'))) if abs(getVarValue(c,"LepGood_pdgId",i))==11]

def getGoodMuons(c, ptCut = 20, collVars=leptonVars, mu_selector = default_muon_selector):
    return [l for l in getMuons(c, collVars) if mu_selector(l, ptCut = ptCut)]
def getGoodElectrons(c, ptCut = 20, collVars=leptonVars, ele_selector = default_ele_selector):
    return [l for l in getElectrons(c, collVars) if ele_selector(l, ptCut = ptCut)]

def getGoodLeptons(c, ptCut=20, collVars=leptonVars, mu_selector = default_muon_selector, ele_selector = default_ele_selector):
    return [l for l in getLeptons(c, collVars) if (abs(l["pdgId"])==11 and ele_selector(l, ptCut = ptCut)) or (abs(l["pdgId"])==13 and mu_selector(l, ptCut = ptCut))]

#def getGoodAndOtherLeptons(c, ptCut=20, collVars=leptonVars, mu_selector = default_muon_selector, ele_selector = default_ele_selector):
#    good_lep = getLeptons(c, collVars)
#    other_lep = getOtherLeptons(c, collVars)
#    print "Getting leptons: good, other"
#    print len(good_lep), len(other_lep)
#    for l in other_lep: #dirty trick to find back the full lepton if it was in the 'other' collection
#        l['index']+=1000
#    res = [l for l in good_lep+other_lep if (abs(l["pdgId"])==11 and ele_selector(l, ptCut = ptCut)) or (abs(l["pdgId"])==13 and mu_selector(l, ptCut = ptCut))]
#    print len(res)
#    res.sort( key = lambda l:-l['pt'] )
#    return res

def getGoodAndOtherLeptons(c, ptCut=20, collVars=leptonVars, mu_selector = default_muon_selector, ele_selector = default_ele_selector):
    good_lep = [l for l in getLeptons(c, collVars) if (abs(l["pdgId"])==11 and ele_selector(l, ptCut = ptCut)) or (abs(l["pdgId"])==13 and mu_selector(l, ptCut = ptCut))]
    other_lep = [l for l in getOtherLeptons(c, collVars) if (abs(l["pdgId"])==11 and ele_selector(l, ptCut = ptCut)) or (abs(l["pdgId"])==13 and mu_selector(l, ptCut = ptCut))]
    all_lep = good_lep + other_lep
    all_lep.sort( key = lambda l:-l['pt'] )
    return all_lep

tauVars=['eta','pt','phi','pdgId','charge', 'dxy', 'dz', 'idDecayModeNewDMs', 'idCI3hit', 'idAntiMu','idAntiE','mcMatchId']

def getTaus(c, collVars=tauVars):
    return [getObjDict(c, 'TauGood_', collVars, i) for i in range(int(getVarValue(c, 'nTauGood')))]

def looseTauID(l, ptCut=20, absEtaCut=2.4):
    return \
        l["pt"]>=ptCut\
        and abs(l["eta"])<absEtaCut\
        and l["idDecayModeNewDMs"]>=1\
        and l["idCI3hit"]>=1\
        and l["idAntiMu"]>=1\
        and l["idAntiE"]>=1\

def getGoodTaus(c, collVars=tauVars):
    return [l for l in getTaus(c,collVars=collVars) if looseTauID(l)]

idCutBased={'loose':1 ,'medium':2, 'tight':3}
photonVars=['eta','pt','phi','mass','idCutBased','pdgId']
photonVarsMC = photonVars + ['mcPt']
def getPhotons(c, collVars=photonVars, idLevel='loose'):
    return [getObjDict(c, 'gamma_', collVars, i) for i in range(int(getVarValue(c, 'ngamma')))]
def getGoodPhotons(c, ptCut=50, idLevel="loose", isData=True, collVars=None):
    if collVars is None: collVars = photonVars if isData else photonVarsMC
    return [p for p in getPhotons(c, collVars) if p['idCutBased'] >= idCutBased[idLevel] and p['pt'] > ptCut and p['pdgId']==22]

def triggerEmulatorSelector(l):

    ECSc = abs(l["etaSc"])>1.479
    eInvMinusPInv = l["eInvMinusPInv"] if l["eInvMinusPInv"] > 0 else 9e9

    if l["hadronicOverEm"]          >= (0.10-0.03*ECSc):     return False
    if abs(l["dEtaScTrkIn"])        >= (0.01-0.002*ECSc):    return False
    if abs(l["dPhiScTrkIn"])        >= (0.04+0.03*ECSc):     return False
    if l["eInvMinusPInv"]           <= -0.05:                return False
    if l["eInvMinusPInv"]           >= (0.01-0.005*ECSc):    return False
    if l["full5x5_sigmaIetaIeta"]   >= (0.011+0.019*ECSc):   return False
    return True

def getFilterCut(isData=False, isFastSim = False, year = 2016):
    if isFastSim:
        filterCut            = "Flag_goodVertices"
    else:
        if year == 2017:
            #filterCut            = "(1)"
            filters = ["Flag_goodVertices", "Flag_globalTightHalo2016Filter", "Flag_HBHENoiseFilter", "Flag_HBHENoiseIsoFilter", "Flag_EcalDeadCellTriggerPrimitiveFilter", "Flag_BadPFMuonFilter", "Flag_BadChargedCandidateFilter"]
            filterCut = "&&".join(filters)
            #filterCut   = "Flag_goodVertices&&Flag_globalSuperTightHalo2016Filter&&Flag_HBHENoiseFilter&&Flag_HBHENoiseIsoFilter&&Flag_EcalDeadCellTriggerPrimitiveFilter&&Flag_BadPFMuonFilter&&Flag_BadChargedCandidateFilter"
            if isData:
                filterCut += "&&Flag_eeBadScFilter"
            #filterCut            = "Flag_goodVertices&&Flag_HBHENoiseIsoFilter&&Flag_HBHENoiseFilter&&Flag_globalTightHalo2016Filter&&Flag_EcalDeadCellTriggerPrimitiveFilter&&Flag_BadPFMuonFilter&&Flag_BadChargedCandidateFilter&&Flag_eeBadScFilter&&Flag_ecalBadCalibFilter"
        else:
            filterCut            = "Flag_goodVertices&&Flag_HBHENoiseIsoFilter&&Flag_HBHENoiseFilter&&Flag_globalTightHalo2016Filter&&Flag_eeBadScFilter&&Flag_EcalDeadCellTriggerPrimitiveFilter"
            filterCut            += "&&Flag_badChargedHadronSummer2016&&Flag_badMuonSummer2016"

        #if badMuonFilters == "Moriond2017":
        #    filterCut += "&&Flag_badChargedHadronSummer2016"
        #    if isData: filterCut += "&&Flag_badMuonMoriond2017&&Flag_badCloneMuonMoriond2017"
        #elif badMuonFilters == "Moriond2017Official":
        #    filterCut += "&&Flag_badChargedHadronSummer2016"
        #    if isData: filterCut += "&&Flag_noBadMuons&&!Flag_duplicateMuons"
        #elif badMuonFilters == "Summer2017":
        #    filterCut += "&&Flag_badMuonMoriond2017&&Flag_badCloneMuonMoriond2017"
        #elif badMuonFilters == "Summer2016":
        #    filterCut += "&&Flag_badChargedHadronSummer2016&&Flag_badMuonSummer2016"
        #elif badMuonFilters == "Summer2016_pt20":
        #    filterCut += "&&Flag_badChargedHadronSummer2016&&Flag_badMuonSummer2016_pt20"
        #elif badMuonFilters is None or badMuonFilters == "None":
        #    pass
        #elif badMuonFilters == "Moriond2017OnlyClone":
        #    filterCut += "&&Flag_badChargedHadronSummer2016"
        #    if isData: filterCut += "&&Flag_badCloneMuonMoriond2017"
        #elif badMuonFilters == "Moriond2017OnlyOther":
        #    filterCut += "&&Flag_badChargedHadronSummer2016"
        #    if isData: filterCut += "&&Flag_badMuonMoriond2017"
    if isData: filterCut += "&&weight>0"
    return filterCut
