import ROOT
ROOT.gROOT.LoadMacro("$CMSSW_BASE/src/TopEFT/tools/scripts/niceColorPalette.C")

def niceColorPalette(n=255):
    ROOT.niceColorPalette(n)
