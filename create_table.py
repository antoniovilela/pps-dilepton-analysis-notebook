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

parser = argparse.ArgumentParser(description = 'Creates data table from ntuple')
parser.add_argument('--files', help = 'File paths' )
parser.add_argument('--label', help = 'Label suffix' )
parser.add_argument('--apply_exclusive', dest = 'apply_exclusive', action = 'store_true', required = False, help = '' )
parser.add_argument('-n', '--events', dest = 'events', type = int, required = False, default = -1, help = 'Number of events to process' )
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
maxEvents_ = None
if hasattr( args, 'events' ) and args.events > 0: maxEvents_ = args.events
print ( "Number of events to process: {}".format( "All" if maxEvents_ is None else maxEvents_ ) )

def select_events( events, apply_exclusive=True ):

    selections_ = []
    counts_ = []

    msk_2muons = ( events.nMuonCand >= 2 )
    events_2muons = events[msk_2muons]    

    dphi = events_2muons.MuonCand.phi[:,0] - events_2muons.MuonCand.phi[:,1]
    
    dphi = np.where( dphi >=  scipy.constants.pi, dphi - 2*scipy.constants.pi, dphi)
    dphi = np.where( dphi <  -scipy.constants.pi, dphi + 2*scipy.constants.pi, dphi)
    acopl = 1. - np.abs(dphi)/scipy.constants.pi

    events_2muons["Acopl"] = acopl

    m1 = events_2muons.MuonCand[:,0]
    m2 = events_2muons.MuonCand[:,1]

    invariant_mass = np.sqrt( 2*m1.pt*m2.pt*( np.cosh(m1.eta - m2.eta) - np.cos(m1.phi - m2.phi) ) )

    events_2muons["InvMass"] = invariant_mass

    energy_com = 13000.
    xi_mumu_plus = (1./energy_com) * ( m1.pt*np.exp(m1.eta) + m2.pt*np.exp(m2.eta) )
    xi_mumu_minus = (1./energy_com) * ( m1.pt*np.exp(-m1.eta) + m2.pt*np.exp(-m2.eta) )

    events_2muons["XiMuMuPlus"] = xi_mumu_plus
    events_2muons["XiMuMuMinus"] = xi_mumu_minus

    pfCands_ = events_2muons.PfCand

    pfCands_["dR_0"] = np.sqrt( ( pfCands_.eta - events_2muons.MuonCand.eta[:,0] )**2 + ( pfCands_.phi - events_2muons.MuonCand.phi[:,0] )**2 )
    pfCands_["dR_1"] = np.sqrt( ( pfCands_.eta - events_2muons.MuonCand.eta[:,1] )**2 + ( pfCands_.phi - events_2muons.MuonCand.phi[:,1] )**2 )

    pfCands_sel1_ = pfCands_[
                    pfCands_.fromPV == 3.0 
                    ]
    pfCands_sel2_ = pfCands_sel1_[
                    pfCands_sel1_.dR_0 > 0.3 
                    ]
    pfCands_sel3_ = pfCands_sel2_[
                    pfCands_sel2_.dR_1 > 0.3 
                    ]
    events_2muons[ "nExtraPfCandPV3" ] = ak.num( pfCands_sel3_ )
    
    msk_muon = ( np.array( events_2muons.MuonCand.pt[:,0] >= 50. ) & np.array( events_2muons.MuonCand.pt[:,1] >= 50. ) &
                 np.array( events_2muons.MuonCand.istight[:,0] == 1 ) & np.array( events_2muons.MuonCand.istight[:,1] == 1 ) &
                 np.array( ( events_2muons.MuonCand.charge[:,0] * events_2muons.MuonCand.charge[:,1] ) == -1 ) )
    selections_.append( "Muon" )
    counts_.append( np.sum( msk_muon ) )
    
    msk_vtx = msk_muon & ( 
        np.array( np.abs( events_2muons.PrimVertexCand.z[:,0] ) <= 15. ) &
        np.array( np.abs( events_2muons.MuonCand.vtxz[:,0] - events_2muons.PrimVertexCand.z[:,0] ) <= 0.02 ) &
        np.array( np.abs( events_2muons.MuonCand.vtxz[:,1] - events_2muons.PrimVertexCand.z[:,0] ) <= 0.02 ) 
        )
    selections_.append( "Vertex" )
    counts_.append( np.sum( msk_vtx ) )
    
    events_sel = None
    if apply_exclusive:
        msk_excl = msk_vtx & ( np.array( events_2muons["InvMass"] >= 110. ) & 
                               np.array( events_2muons["Acopl"] <= 0.009 ) & 
                               np.array( events_2muons["nExtraPfCandPV3"] <= 1 ) )
        selections_.append( "Exclusive" )
        counts_.append( np.sum( msk_excl ) )

        events_sel = events_2muons[ msk_excl ]
    else:
        events_sel = events_2muons[ msk_vtx ]  

    selections_ = np.array( selections_ )
    counts_ = np.array( counts_ )
    #print ( selections_ )
    #print ( counts_ )    
    
    return ( events_sel, selections_, counts_ )
        
def select_protons(events):
    #protons_ = events.ProtCand[
    #    events.ProtCand.ismultirp == 1
    #    ]

    protons_ = events.ProtCand

    protons_["Run"] = events[ "Run" ]
    protons_["LumiSection"] = events[ "LumiSection" ]
    protons_["BX"] = events[ "BX" ]
    protons_["EventNum"] = events[ "EventNum" ]
    
    protons_["CrossingAngle"] = events[ "CrossingAngle" ]
    
    protons_["Muon0Pt"] = events.MuonCand.pt[:,0]
    protons_["Muon0Eta"] = events.MuonCand.eta[:,0]
    protons_["Muon0Phi"] = events.MuonCand.phi[:,0]
    protons_["Muon0VtxZ"] = events.MuonCand.vtxz[:,0]
    protons_["Muon1Pt"] = events.MuonCand.pt[:,1]
    protons_["Muon1Eta"] = events.MuonCand.eta[:,1]
    protons_["Muon1Phi"] = events.MuonCand.phi[:,1]
    protons_["Muon1VtxZ"] = events.MuonCand.vtxz[:,1]

    protons_["PrimVertexZ"] = events.PrimVertexCand.z[:,0]
    
    protons_["InvMass"] = events[ "InvMass" ]
    protons_["nExtraPfCandPV3"] = events[ "nExtraPfCandPV3" ]
    protons_["Acopl"] = events[ "Acopl" ]

    protons_["XiMuMuPlus"] = events[ "XiMuMuPlus" ]
    protons_["XiMuMuMinus"] = events[ "XiMuMuMinus" ]
    
    msk_num_prot = ( ak.num( protons_.xi ) > 0 )
    protons_ = protons_[ msk_num_prot ]
    
    print ( len(protons_) )
    
    return protons_

protons_Run_list = []
protons_LumiSection_list = []
protons_BX_list = []
protons_EventNum_list = []
protons_CrossingAngle_list = []
protons_xi_list = []
protons_ismultirp_list = []
protons_arm_list = []
protons_rpid1_list = []
protons_rpid2_list = []
protons_trackx1_list = []
protons_tracky1_list = []
protons_trackx2_list = []
protons_tracky2_list = []
protons_Muon0Pt_list = []
protons_Muon0Eta_list = []
protons_Muon0Phi_list = []
protons_Muon0VtxZ_list = []
protons_Muon1Pt_list = []
protons_Muon1Eta_list = []
protons_Muon1Phi_list = []
protons_Muon1VtxZ_list = []
protons_PrimVertexZ_list = []
protons_InvMass_list = []
protons_nExtraPfCandPV3_list = []
protons_Acopl_list = []
protons_XiMuMuPlus_list = []
protons_XiMuMuMinus_list = []

selections = None
counts = None

for file_ in fileNames_:
    print ( file_ ) 
    root_ = uproot4.open( file_ )
    tree_ = root_["ggll_miniaod/ntp1"]
    
    keys = ["Run", "LumiSection", "BX", "EventNum", "CrossingAngle","nHLT", "HLT_Accept", "HLT_Prescl", "HLT_Name",
        "nMuonCand", "MuonCand_pt", "MuonCand_eta", "MuonCand_phi", "MuonCand_e", "MuonCand_charge", "MuonCand_vtxz", "MuonCand_istight",
        "nPrimVertexCand", "PrimVertexCand_z", "PrimVertexCand_chi2", "PrimVertexCand_ndof", "PrimVertexCand_tracks",
        "Weight", "PUWeightTrue"]
    keys.append( "nPfCand" )
    keys.extend( tree_.keys( filter_name="PfCand*" ) ) 
    keys.append( "nRecoProtCand" )
    keys.extend( tree_.keys( filter_name="ProtCand*" ) )  
    print ( keys )
    
    for events_ in tree_.iterate( keys , library="ak", how="zip", step_size="150 MB", entry_stop=maxEvents_ ):
        print ( len(events_), events_ )
        
        #events_sel_ = select_events( events_, apply_exclusive_ )
        events_sel_, selections_, counts_ = select_events( events_, apply_exclusive=apply_exclusive_ )
        print ( selections_ )
        print ( counts_ )
        if selections is None:
            selections = selections_
            counts = counts_
        else:
            msk_selections = np.full_like( selections, False, dtype='bool' )
            for key in selections_:
                print ( key )
                print ( selections == key )
                msk_selections |= ( selections == key )
            counts[ msk_selections ] += counts_

        protons_ = select_protons( events_sel_ )
        counts_protons_ = len( protons_ )
        if not "Protons" in selections:
            selections = np.concatenate( ( selections, np.array( ["Protons"], dtype='S' ) ) )
            counts = np.concatenate( ( counts, np.array( [counts_protons_] ) ) )
        else:    
            counts[ selections == 'Protons'] += counts_protons_ 
        print ( selections )
        print ( counts )

        protons_Run = ak.flatten( protons_.Run )
        protons_LumiSection = ak.flatten( protons_.LumiSection )
        protons_BX = ak.flatten( protons_.BX )
        protons_EventNum = ak.flatten( protons_.EventNum )
        protons_CrossingAngle = ak.flatten( protons_.CrossingAngle )
        protons_xi = ak.flatten( protons_.xi )
        protons_ismultirp = ak.flatten( protons_.ismultirp )
        protons_arm = ak.flatten( protons_.arm )
        protons_rpid1 = ak.flatten( protons_.rpid1 )
        protons_rpid2 = ak.flatten( protons_.rpid2 )
        protons_trackx1 = ak.flatten( protons_.trackx1 )
        protons_tracky1 = ak.flatten( protons_.tracky1 )
        protons_trackx2 = ak.flatten( protons_.trackx2 )
        protons_tracky2 = ak.flatten( protons_.tracky2 )   
        protons_Muon0Pt = ak.flatten( protons_.Muon0Pt )
        protons_Muon0Eta = ak.flatten( protons_.Muon0Eta )
        protons_Muon0Phi = ak.flatten( protons_.Muon0Phi )
        protons_Muon0VtxZ = ak.flatten( protons_.Muon0VtxZ )
        protons_Muon1Pt = ak.flatten( protons_.Muon1Pt )
        protons_Muon1Eta = ak.flatten( protons_.Muon1Eta )
        protons_Muon1Phi = ak.flatten( protons_.Muon1Phi )
        protons_Muon1VtxZ = ak.flatten( protons_.Muon1VtxZ )
        protons_PrimVertexZ = ak.flatten( protons_.PrimVertexZ )
        protons_InvMass = ak.flatten( protons_.InvMass )
        protons_nExtraPfCandPV3 = ak.flatten( protons_.nExtraPfCandPV3 )
        protons_Acopl = ak.flatten( protons_.Acopl )
        protons_XiMuMuPlus = ak.flatten( protons_.XiMuMuPlus )
        protons_XiMuMuMinus = ak.flatten( protons_.XiMuMuMinus )
        
        print ( "Protons (flattened): {}".format( len(protons_xi) ) )
        
        protons_Run_list.append( protons_Run )
        protons_LumiSection_list.append( protons_LumiSection )
        protons_BX_list.append( protons_BX )
        protons_EventNum_list.append( protons_EventNum )
        protons_CrossingAngle_list.append( protons_CrossingAngle )
        protons_xi_list.append( protons_xi )
        protons_ismultirp_list.append( protons_ismultirp )
        protons_arm_list.append( protons_arm )
        protons_rpid1_list.append( protons_rpid1 )
        protons_rpid2_list.append( protons_rpid2 )
        protons_trackx1_list.append( protons_trackx1 )
        protons_tracky1_list.append( protons_tracky1 )
        protons_trackx2_list.append( protons_trackx2 )
        protons_tracky2_list.append( protons_tracky2 )
        protons_Muon0Pt_list.append( protons_Muon0Pt )
        protons_Muon0Eta_list.append( protons_Muon0Eta )
        protons_Muon0Phi_list.append( protons_Muon0Phi )
        protons_Muon0VtxZ_list.append( protons_Muon0VtxZ )
        protons_Muon1Pt_list.append( protons_Muon1Pt )
        protons_Muon1Eta_list.append( protons_Muon1Eta )
        protons_Muon1Phi_list.append( protons_Muon1Phi )
        protons_Muon1VtxZ_list.append( protons_Muon1VtxZ )
        protons_PrimVertexZ_list.append( protons_PrimVertexZ )
        protons_InvMass_list.append( protons_InvMass )
        protons_nExtraPfCandPV3_list.append( protons_nExtraPfCandPV3 )
        protons_Acopl_list.append( protons_Acopl )
        protons_XiMuMuPlus_list.append( protons_XiMuMuPlus )
        protons_XiMuMuMinus_list.append( protons_XiMuMuMinus )
        
    print ( selections )
    print ( counts )    
    root_.close()

protons_Run_all             = np.array( np.concatenate( protons_Run_list ) )
protons_LumiSection_all     = np.array( np.concatenate( protons_LumiSection_list ) )
protons_BX_all              = np.array( np.concatenate( protons_BX_list ) )
protons_EventNum_all        = np.array( np.concatenate( protons_EventNum_list ) )
protons_CrossingAngle_all   = np.array( np.concatenate( protons_CrossingAngle_list ) )
protons_xi_all              = np.array( np.concatenate( protons_xi_list ) )
protons_ismultirp_all       = np.array( np.concatenate( protons_ismultirp_list ) )
protons_arm_all             = np.array( np.concatenate( protons_arm_list ) )
protons_rpid1_all           = np.array( np.concatenate( protons_rpid1_list ) )
protons_rpid2_all           = np.array( np.concatenate( protons_rpid2_list ) )
protons_trackx1_all         = np.array( np.concatenate( protons_trackx1_list ) )
protons_tracky1_all         = np.array( np.concatenate( protons_tracky1_list ) )
protons_trackx2_all         = np.array( np.concatenate( protons_trackx2_list ) )
protons_tracky2_all         = np.array( np.concatenate( protons_tracky2_list ) )
protons_Muon0Pt_all         = np.array( np.concatenate( protons_Muon0Pt_list ) )
protons_Muon0Eta_all        = np.array( np.concatenate( protons_Muon0Eta_list ) )
protons_Muon0Phi_all        = np.array( np.concatenate( protons_Muon0Phi_list ) )
protons_Muon0VtxZ_all       = np.array( np.concatenate( protons_Muon0VtxZ_list ) )
protons_Muon1Pt_all         = np.array( np.concatenate( protons_Muon1Pt_list ) )
protons_Muon1Eta_all        = np.array( np.concatenate( protons_Muon1Eta_list ) )
protons_Muon1Phi_all        = np.array( np.concatenate( protons_Muon1Phi_list ) )
protons_Muon1VtxZ_all       = np.array( np.concatenate( protons_Muon1VtxZ_list ) )
protons_PrimVertexZ_all     = np.array( np.concatenate( protons_PrimVertexZ_list ) )
protons_InvMass_all         = np.array( np.concatenate( protons_InvMass_list ) )
protons_nExtraPfCandPV3_all = np.array( np.concatenate( protons_nExtraPfCandPV3_list ) )
protons_Acopl_all           = np.array( np.concatenate( protons_Acopl_list ) )
protons_XiMuMuPlus_all      = np.array( np.concatenate( protons_XiMuMuPlus_list ) )
protons_XiMuMuMinus_all     = np.array( np.concatenate( protons_XiMuMuMinus_list ) )    
    
print ( "Protons (flattened): {}".format( len(protons_xi_all) ) )

print ( protons_Run_all )
print ( protons_LumiSection_all )
print ( protons_BX_all )
print ( protons_EventNum_all )
print ( protons_CrossingAngle_all )
print ( protons_xi_all )
print ( protons_ismultirp_all )
print ( protons_arm_all )
print ( protons_rpid1_all )
print ( protons_rpid2_all )
print ( protons_trackx1_all )
print ( protons_tracky1_all )
print ( protons_trackx2_all )
print ( protons_tracky2_all )
print ( protons_Muon0Pt_all )
print ( protons_Muon0Eta_all )
print ( protons_Muon0Phi_all )
print ( protons_Muon0VtxZ_all )
print ( protons_Muon1Pt_all )
print ( protons_Muon1Eta_all )
print ( protons_Muon1Phi_all )
print ( protons_Muon1VtxZ_all )
print ( protons_PrimVertexZ_all )
print ( protons_InvMass_all )
print ( protons_nExtraPfCandPV3_all )
print ( protons_Acopl_all )
print ( protons_XiMuMuPlus_all )
print ( protons_XiMuMuMinus_all )

data_ = np.c_[
    protons_Run_all,
    protons_LumiSection_all,
    protons_BX_all,
    protons_EventNum_all,
    protons_CrossingAngle_all,
    protons_xi_all,
    protons_ismultirp_all,
    protons_arm_all,
    protons_rpid1_all,
    protons_rpid2_all,
    protons_trackx1_all,
    protons_tracky1_all,
    protons_trackx2_all,
    protons_tracky2_all,
    protons_Muon0Pt_all,
    protons_Muon0Eta_all,
    protons_Muon0Phi_all,
    protons_Muon0VtxZ_all,
    protons_Muon1Pt_all,
    protons_Muon1Eta_all,
    protons_Muon1Phi_all,
    protons_Muon1VtxZ_all,
    protons_PrimVertexZ_all,
    protons_InvMass_all,
    protons_nExtraPfCandPV3_all,
    protons_Acopl_all,
    protons_XiMuMuPlus_all,
    protons_XiMuMuMinus_all
    ]

print ( data_.shape )

columns_ = np.array( ("Run", "LumiSection", "BX", "EventNum", "CrossingAngle",
                      "Xi", "MultiRP", "Arm", "RPId1", "RPId2", "TrackX1", "TrackY1", "TrackX2", "TrackY2",
                      "Muon0Pt", "Muon0Eta", "Muon0Phi", "Muon0VtxZ", "Muon1Pt", "Muon1Eta", "Muon1Phi", "Muon1VtxZ",
                      "PrimVertexZ", "InvMass", "ExtraPfCands", "Acopl", "XiMuMuPlus", "XiMuMuMinus"), dtype='S' )
print ( columns_ )

event_counts_ = counts
print ( event_counts_ )

selections_ = np.array( selections, dtype='S' )
print ( selections_ )

with h5py.File( 'output-' + label_ + '.h5', 'w') as f:
    dset = f.create_dataset( 'protons', data=data_ )
    dset_columns = f.create_dataset( 'columns', data=columns_ )
    dset_counts = f.create_dataset( 'event_counts', data=event_counts_ )
    dset_selections = f.create_dataset( 'selections', data=selections_ )

    print ( dset )
    print ( dset[-1] )   
    print ( dset_columns )
    print ( list( dset_columns ) )   
    print ( dset_counts )
    print ( list( dset_counts ) )
    print ( dset_selections )
    print ( list( dset_selections ) )
