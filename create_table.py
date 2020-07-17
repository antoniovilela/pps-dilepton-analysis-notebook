import uproot4
import awkward1 as ak
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mplhep
import numba as nb
import scipy.constants
import h5py
import argparse
plt.style.use(mplhep.style.CMS)

parser = argparse.ArgumentParser(description = 'Creates data table from ntuple')
parser.add_argument('--files', help = 'File paths' )
parser.add_argument('--label', help = 'Label suffix' )
parser.add_argument('--apply_exclusive', dest = 'apply_exclusive', action = 'store_true', required = False, help = '' )
#parser.add_argument('-n', '--events', dest = 'events', type = int, required = False, default = 100000, help = 'Number of events to process' )
#parser.add_argument('-v', '--verbose', action = 'store_true', dest = 'verbose', required = False, help = 'Enable verbose' )
args = parser.parse_args()

fileNames_ = args.files.split(",")
print( "Reading files: " )
for item in fileNames_: print ( item )
label_ = args.label
print ( "Label: " + label_ ) 
apply_exclusive_ = False
if hasattr( args, 'apply_exclusive') and args.apply_exclusive: apply_exclusive_ = args.apply_exclusive
print ( "Apply exclusive selection: {}".format( apply_exclusive_ ) )

def select_events( events, apply_exclusive=True ):
    
    msk1 = ( events.nMuonCand >= 2 )
    events_sel1 = events[msk1]

    msk2 = ( np.array( events_sel1.MuonCand.pt[:,0] >= 50. ) & np.array( events_sel1.MuonCand.pt[:,1] >= 50. ) &
             np.array( events_sel1.MuonCand.istight[:,0] == 1 ) & np.array( events_sel1.MuonCand.istight[:,1] == 1 ) &
             np.array( ( events_sel1.MuonCand.charge[:,0] * events_sel1.MuonCand.charge[:,1] ) == -1 ) &
             np.array( np.abs( events_sel1.MuonCand.vtxz[:,0] - events_sel1.PrimVertexCand.z[:,0] ) <= 0.02 ) &
             np.array( np.abs( events_sel1.MuonCand.vtxz[:,1] - events_sel1.PrimVertexCand.z[:,0] ) <= 0.02 ) ) 
    events_sel2 = events_sel1[msk2]

    dphi = events_sel2.MuonCand.phi[:,0] - events_sel2.MuonCand.phi[:,1]
    
    dphi = np.where( dphi >=  scipy.constants.pi, dphi - 2*scipy.constants.pi, dphi)
    dphi = np.where( dphi <  -scipy.constants.pi, dphi + 2*scipy.constants.pi, dphi)
    acopl = 1. - np.abs(dphi)/scipy.constants.pi

    events_sel2["Acopl"] = acopl

    m1 = events_sel2.MuonCand[:,0]
    m2 = events_sel2.MuonCand[:,1]

    invariant_mass = np.sqrt( 2*m1.pt*m2.pt*( np.cosh(m1.eta - m2.eta) - np.cos(m1.phi - m2.phi) ) )

    events_sel2["InvMass"] = invariant_mass

    energy_com = 13000.
    xi_mumu_plus = (1./energy_com) * ( m1.pt*np.exp(m1.eta) + m2.pt*np.exp(m2.eta) )
    xi_mumu_minus = (1./energy_com) * ( m1.pt*np.exp(-m1.eta) + m2.pt*np.exp(-m2.eta) )

    events_sel2["XiMuMuPlus"] = xi_mumu_plus
    events_sel2["XiMuMuMinus"] = xi_mumu_minus

    pfCands_ = events_sel2.PfCand

    pfCands_["dR_0"] = np.sqrt( ( pfCands_.eta - events_sel2.MuonCand.eta[:,0] )**2 + ( pfCands_.phi - events_sel2.MuonCand.phi[:,0] )**2 )
    pfCands_["dR_1"] = np.sqrt( ( pfCands_.eta - events_sel2.MuonCand.eta[:,1] )**2 + ( pfCands_.phi - events_sel2.MuonCand.phi[:,1] )**2 )

    pfCands_sel1_ = pfCands_[
                    pfCands_.fromPV == 3.0 
                    ]
    pfCands_sel2_ = pfCands_sel1_[
                    pfCands_sel1_.dR_0 > 0.3 
                    ]
    pfCands_sel3_ = pfCands_sel2_[
                    pfCands_sel2_.dR_1 > 0.3 
                    ]
    events_sel2[ "nExtraPfCandPV3" ] = ak.num( pfCands_sel3_ )
    
    if apply_exclusive:
        #msk3 = ( np.array( events_sel2["InvMass"] >= 110. ) & 
        #         np.array( events_sel2["Acopl"] <= 0.009 ) & 
        #         np.array( events_sel2["nPfCand"] <= 3 ) )
        msk3 = ( np.array( events_sel2["InvMass"] >= 110. ) & 
                 np.array( events_sel2["Acopl"] <= 0.009 ) & 
                 np.array( events_sel2["nExtraPfCandPV3"] <= 1 ) )
        events_sel3 = events_sel2[msk3]

        print ( len(events), len(events_sel1), len(events_sel2), len(events_sel3) )
        return events_sel3
    else:
        print ( len(events), len(events_sel1), len(events_sel2) )
        return events_sel2
    

def select_protons(events):
    #protons_ = events.ProtCand[
    #    events.ProtCand.ismultirp == 1
    #    ]

    protons_ = events.ProtCand
    
    protons_["CrossingAngle"] = events[ "CrossingAngle" ]
    
    protons_["Muon0Pt"] = events.MuonCand.pt[:,0]
    protons_["Muon0Eta"] = events.MuonCand.eta[:,0]
    protons_["Muon0Phi"] = events.MuonCand.phi[:,0]
    protons_["Muon1Pt"] = events.MuonCand.pt[:,1]
    protons_["Muon1Eta"] = events.MuonCand.eta[:,1]
    protons_["Muon1Phi"] = events.MuonCand.phi[:,1]

    protons_["InvMass"] = events[ "InvMass" ]
    protons_["nExtraPfCandPV3"] = events[ "nExtraPfCandPV3" ]
    protons_["Acopl"] = events[ "Acopl" ]

    xi_mumu_plus_sel = events[ "XiMuMuPlus" ]
    protons_["XiMuMuPlus"] = xi_mumu_plus_sel
    xi_mumu_minus_sel = events[ "XiMuMuMinus" ]
    protons_["XiMuMuMinus"] = xi_mumu_minus_sel
    
    msk_num_prot = ( ak.num( protons_.xi ) > 0 )
    protons_ = protons_[ msk_num_prot ]
    
    print ( len(protons_) )
    
    return protons_

#fileNames = [
#    "/eos/cms/store/group/phys_pps/dilepton/DoubleMuon/UL-MiniAOD-2017/DoubleMuon_UL2017B.root",
#    "/eos/cms/store/group/phys_pps/dilepton/DoubleMuon/UL-MiniAOD-2017/DoubleMuon_UL2017C1.root"
#]

protons_xi_list = []
protons_ismultirp_list = []
protons_arm_list = []
protons_rpid1_list = []
protons_rpid2_list = []
protons_trackx1_list = []
protons_tracky1_list = []
protons_trackx2_list = []
protons_tracky2_list = []
protons_CrossingAngle_list = []
protons_InvMass_list = []
protons_nExtraPfCandPV3_list = []
protons_Acopl_list = []
protons_XiMuMuPlus_list = []
protons_XiMuMuMinus_list = []

for file_ in fileNames_:
    print ( file_ ) 
    root_ = uproot4.open( file_ )
    tree_ = root_["ggll_miniaod/ntp1"]
    
    #n_events_tree = np.array( uproot4.open( file_ + ":ggll_miniaod/ntp1/nMuonCand" ) ).size
    #print ( n_events_tree )
    
    keys = ["Run", "LumiSection", "BX", "EventNum", "CrossingAngle","nHLT", "HLT_Accept", "HLT_Prescl", "HLT_Name",
        "nMuonCand", "MuonCand_pt", "MuonCand_eta", "MuonCand_phi", "MuonCand_e", "MuonCand_charge", "MuonCand_vtxz", "MuonCand_istight",
        "nPrimVertexCand", "PrimVertexCand_z", "PrimVertexCand_chi2", "PrimVertexCand_ndof", "PrimVertexCand_tracks",
        "Weight", "PUWeightTrue"]
    keys.append( "nPfCand" )
    keys.extend( tree_.keys( filter_name="PfCand*" ) ) 
    keys.append( "nRecoProtCand" )
    keys.extend( tree_.keys( filter_name="ProtCand*" ) )  
    print ( keys )
    
    #n_events_chunk = 500000
    #start = np.arange(0, n_events_tree, n_events_chunk)
    #stop = np.full_like(start, -1)
    #stop[:-1] = start[1:]
    #print ( start )
    #print ( stop )
    #sum_chunks = 0
    #for (start_, stop_) in zip(start, stop):
    for events_ in tree_.iterate( keys , library="ak", how="zip", step_size="150 MB" ):
    #for events_ in tree_.iterate( keys , library="ak", how="zip", step_size="150 MB", entry_stop=200000 ):
        #if stop_ == -1: stop_ = None
        #print ( start_, stop_ )
        #events_ = tree_.arrays( keys , library="ak", how="zip", entry_start=start_, entry_stop=stop_ )
        #sum_chunks += len(events_)

        print ( len(events_), events_ )
        
        events_sel_ = select_events( events_, apply_exclusive_ )    
        protons_ = select_protons( events_sel_ )

        protons_xi = ak.flatten( protons_.xi )
        protons_ismultirp = ak.flatten( protons_.ismultirp )
        protons_arm = ak.flatten( protons_.arm )
        protons_rpid1 = ak.flatten( protons_.rpid1 )
        protons_rpid2 = ak.flatten( protons_.rpid2 )
        protons_trackx1 = ak.flatten( protons_.trackx1 )
        protons_tracky1 = ak.flatten( protons_.tracky1 )
        protons_trackx2 = ak.flatten( protons_.trackx2 )
        protons_tracky2 = ak.flatten( protons_.tracky2 )
        protons_CrossingAngle = ak.flatten( protons_.CrossingAngle )
        protons_InvMass = ak.flatten( protons_.InvMass )
        protons_nExtraPfCandPV3 = ak.flatten( protons_.nExtraPfCandPV3 )
        protons_Acopl = ak.flatten( protons_.Acopl )
        protons_XiMuMuPlus = ak.flatten( protons_.XiMuMuPlus )
        protons_XiMuMuMinus = ak.flatten( protons_.XiMuMuMinus )

        print ( len(protons_xi) )
        protons_xi_list.append( protons_xi )
        protons_ismultirp_list.append( protons_ismultirp )
        protons_arm_list.append( protons_arm )
        protons_rpid1_list.append( protons_rpid1 )
        protons_rpid2_list.append( protons_rpid2 )
        protons_trackx1_list.append( protons_trackx1 )
        protons_tracky1_list.append( protons_tracky1 )
        protons_trackx2_list.append( protons_trackx2 )
        protons_tracky2_list.append( protons_tracky2 )
        protons_CrossingAngle_list.append( protons_CrossingAngle )
        protons_InvMass_list.append( protons_InvMass )
        protons_nExtraPfCandPV3_list.append( protons_nExtraPfCandPV3 )
        protons_Acopl_list.append( protons_Acopl )
        protons_XiMuMuPlus_list.append( protons_XiMuMuPlus )
        protons_XiMuMuMinus_list.append( protons_XiMuMuMinus )
        
    #print ( sum_chunks )
    
    root_.close()
    
protons_xi_all            = np.array( np.concatenate( protons_xi_list ) )
protons_ismultirp_all     = np.array( np.concatenate( protons_ismultirp_list ) )
protons_arm_all           = np.array( np.concatenate( protons_arm_list ) )
protons_rpid1_all         = np.array( np.concatenate( protons_rpid1_list ) )
protons_rpid2_all         = np.array( np.concatenate( protons_rpid2_list ) )
protons_trackx1_all       = np.array( np.concatenate( protons_trackx1_list ) )
protons_tracky1_all       = np.array( np.concatenate( protons_tracky1_list ) )
protons_trackx2_all       = np.array( np.concatenate( protons_trackx2_list ) )
protons_tracky2_all       = np.array( np.concatenate( protons_tracky2_list ) )
protons_CrossingAngle_all = np.array( np.concatenate( protons_CrossingAngle_list ) )
protons_InvMass_all = np.array( np.concatenate( protons_InvMass_list ) )
protons_nExtraPfCandPV3_all = np.array( np.concatenate( protons_nExtraPfCandPV3_list ) )
protons_Acopl_all = np.array( np.concatenate( protons_Acopl_list ) )
protons_XiMuMuPlus_all    = np.array( np.concatenate( protons_XiMuMuPlus_list ) )
protons_XiMuMuMinus_all   = np.array( np.concatenate( protons_XiMuMuMinus_list ) )
print ( len( protons_xi_all ) )
print ( protons_xi_all )
print ( protons_ismultirp_all )
print ( protons_arm_all )
print ( protons_rpid1_all )
print ( protons_rpid2_all )
print ( protons_trackx1_all )
print ( protons_tracky1_all )
print ( protons_trackx2_all )
print ( protons_tracky2_all )
print ( protons_CrossingAngle_all )
print ( protons_InvMass_all )
print ( protons_nExtraPfCandPV3_all )
print ( protons_Acopl_all )
print ( protons_XiMuMuPlus_all )
print ( protons_XiMuMuMinus_all )

data_ = np.c_[
    protons_xi_all,
    protons_ismultirp_all,
    protons_arm_all,
    protons_rpid1_all,
    protons_rpid2_all,
    protons_trackx1_all,
    protons_tracky1_all,
    protons_trackx2_all,
    protons_tracky2_all,
    protons_CrossingAngle_all,
    protons_InvMass_all,
    protons_nExtraPfCandPV3_all,
    protons_Acopl_all,
    protons_XiMuMuPlus_all,
    protons_XiMuMuMinus_all
    ]
print ( data_.shape )
columns_ = np.array( ("Xi", "MultiRP", "Arm", "RPId1", "RPId2", "TrackX1", "TrackY1", "TrackX2", "TrackY2", "XAngle", "InvMass", "ExtraPfCands", "Acopl", "XiMuMuPlus", "XiMuMuMinus"), dtype='S' )

with h5py.File( 'output-' + label_ + '.h5', 'w') as f:
    dset = f.create_dataset( 'protons', data=data_ )
    dset_columns = f.create_dataset( 'columns', data=columns_ )
    print ( dset )
    print ( dset[-1] )   
    print ( dset_columns )
    print ( list( dset_columns ) )   
    
