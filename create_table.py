import uproot
import awkward as ak
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mplhep
import numba as nb
import scipy.constants
import h5py
import argparse

from select_events import *
from processing import df_run_ranges_2017, df_run_ranges_2018, df_run_ranges_mixing_2017, df_run_ranges_mixing_2018, lumi_periods_2017, lumi_periods_2018

parser = argparse.ArgumentParser(description = 'Creates data table from ntuple.')
parser.add_argument('--files', help = 'File paths.' )
parser.add_argument('--label', help = 'Label suffix.' )
parser.add_argument('--data_sample', help = 'Data sample.' )
parser.add_argument('--runOnMC', dest = 'runOnMC', action = 'store_true', required = False, help = '' )
parser.add_argument('--apply_exclusive', dest = 'apply_exclusive', action = 'store_true', required = False, help = '' )
parser.add_argument('--apply_doublearm', dest = 'apply_doublearm', action = 'store_true', required = False, help = '' )
parser.add_argument('--min_pt_1', dest = 'min_pt_1', type=float, required = False, default = 50., help = '' )
parser.add_argument('--min_pt_2', dest = 'min_pt_2', type=float, required = False, default = 0., help = '' )
parser.add_argument('--random_protons', dest = 'random_protons', action = 'store_true', required = False, help = '' )
parser.add_argument('--resample_factor', dest = 'resample_factor', type = int, required = False, default = -1, help = '' )
parser.add_argument('--mix_protons', dest = 'mix_protons', action = 'store_true', required = False, help = '' )
parser.add_argument('-s', '--start', dest = 'start', type = int, required = False, default = -1, help = 'First event to process.' )
parser.add_argument('-n', '--events', dest = 'events', type = int, required = False, default = -1, help = 'Number of events to process.' )
parser.add_argument('--read_size', dest = 'read_size', required = False, default = "500MB" , help = 'Input buffer size.' )
parser.add_argument('--version', dest = 'version', required = False, default = "V1" , help = 'Version of data tables.' )
#parser.add_argument('-v', '--verbose', action = 'store_true', dest = 'verbose', required = False, help = 'Enable verbose' )
args = parser.parse_args()

debug_ = False

fileNames_ = args.files.split(",")
print( "Reading files: " )
for item in fileNames_: print ( item )

label_ = args.label
print ( "Label: " + label_ ) 

data_sample_ = args.data_sample
print ( "Data sample: " + data_sample_ )

lepton_type_ = 'muon'
print ( "Lepton type: {}".format( lepton_type_ ) )

runOnMC_ = False
if hasattr( args, 'runOnMC') and args.runOnMC: runOnMC_ = args.runOnMC
print ( "Run on MC: {}".format( runOnMC_ ) )

apply_exclusive_ = False
if hasattr( args, 'apply_exclusive') and args.apply_exclusive: apply_exclusive_ = args.apply_exclusive
print ( "Apply exclusive selection: {}".format( apply_exclusive_ ) )

apply_doublearm_ = False
if hasattr( args, 'apply_doublearm') and args.apply_doublearm: apply_doublearm_ = args.apply_doublearm
print ( "Apply double arm selection: {}".format( apply_doublearm_ ) )

min_pt_1_ = 50.0
if hasattr( args, 'min_pt_1') and args.min_pt_1 > 0.: min_pt_1_ = args.min_pt_1
print ( "Min. p_T (1)={}".format( min_pt_1_ ) )

min_pt_2_ = min_pt_1_
if hasattr( args, 'min_pt_2') and args.min_pt_2 > 0.: min_pt_2_ = args.min_pt_2
print ( "Min. p_T (2)={}".format( min_pt_2_ ) )

random_protons_ = False
if hasattr( args, 'random_protons') and args.random_protons: random_protons_ = args.random_protons
print ( "Random protons: {}".format( random_protons_ ) )

resample_factor_ = -1
if hasattr( args, 'resample_factor'): resample_factor_ = args.resample_factor
print ( "Resample factor: {}".format( resample_factor_ ) )

mix_protons_ = False
if hasattr( args, 'mix_protons') and args.mix_protons: mix_protons_ = args.mix_protons
print ( "Mix protons: {}".format( mix_protons_ ) )

prescale_mix_protons_ = None
if mix_protons_:
    prescale_mix_protons_ = 50
    print ( "Prescale of proton files: {}".format( prescale_mix_protons_ ) )

firstEvent_ = None
if hasattr( args, 'start' ) and args.start > 0: firstEvent_ = args.start
print ( "First event to process: {}".format( "from first" if firstEvent_ is None else firstEvent_ ) )

maxEvents_ = None
if hasattr( args, 'events' ) and args.events > 0: maxEvents_ = args.events
print ( "Number of events to process: {}".format( "to end" if maxEvents_ is None else maxEvents_ ) )

#entrystop_ = maxEvents_ if firstEvent_ is None else ( firstEvent_ + maxEvents_ )
entrystop_ = None
if firstEvent_ is None:
    entrystop_ = maxEvents_
else:
    if not maxEvents_ is None:
        entrystop_  = ( firstEvent_ + maxEvents_ )

# read_size_ = "150MB"
read_size_ = None
if hasattr( args, 'read_size' ): read_size_ = args.read_size
print ( "Input buffer size: {}".format( read_size_ ) )

version_ = "V1"
if hasattr( args, 'version' ): version_ = args.version
if not version_ in ("V1", "V2"):
    print ( "Unsupported parameter value: --{}={}".format( "version", version_ ) )
    exit()
print ( "Data tables version: {}".format( version_ ) )

resample_ = False
if resample_factor_ > 1: resample_ = True

proton_files = None
if mix_protons_:
    proton_files = [
        "/eos/cms/store/group/phys_pps/miguelgallo/Dilepton/2018/Muon/Data/DoubleMuon_Run2018A-UL2018_0.root",
        "/eos/cms/store/group/phys_pps/miguelgallo/Dilepton/2018/Muon/Data/DoubleMuon_Run2018A-UL2018_1.root",
        "/eos/cms/store/group/phys_pps/miguelgallo/Dilepton/2018/Muon/Data/DoubleMuon_Run2018B-UL2018.root",
        "/eos/cms/store/group/phys_pps/miguelgallo/Dilepton/2018/Muon/Data/DoubleMuon_Run2018C-UL2018.root",
        "/eos/cms/store/group/phys_pps/miguelgallo/Dilepton/2018/Muon/Data/DoubleMuon_Run2018D-UL2018_0.root",
        "/eos/cms/store/group/phys_pps/miguelgallo/Dilepton/2018/Muon/Data/DoubleMuon_Run2018D-UL2018_1.root",
        "/eos/cms/store/group/phys_pps/miguelgallo/Dilepton/2018/Muon/Data/DoubleMuon_Run2018D-UL2018_2.root",
        "/eos/cms/store/group/phys_pps/miguelgallo/Dilepton/2018/Muon/Data/DoubleMuon_Run2018D-UL2018_3.root"
        ]

tree_path_ = "ggll_miniaod/ntp1"
tree_path_proton_files_ = "ggll_miniaod/ntp1"

df_run_ranges_ = None
df_run_ranges_mixing_ = None
if data_sample_ == '2017':
    df_run_ranges_ = df_run_ranges_2017
    df_run_ranges_mixing_ = df_run_ranges_mixing_2017
elif data_sample_ == '2018':
    df_run_ranges_ = df_run_ranges_2018
    df_run_ranges_mixing_ = df_run_ranges_mixing_2018
print ( df_run_ranges_ )
print ( df_run_ranges_mixing_ )

data_periods_ = None
if runOnMC_:
    data_periods_ = list( df_run_ranges_.index )

lumi_periods_ = None
if data_sample_ == '2017':
    if lepton_type_ == 'muon':
        lumi_periods_ = lumi_periods_2017[ 'muon' ]
    elif lepton_type_ == 'electron':
        lumi_periods_ = lumi_periods_2017[ 'electron' ]
elif data_sample_ == '2018':
    if lepton_type_ == 'muon':
        lumi_periods_ = lumi_periods_2018[ 'muon' ]
    elif lepton_type_ == 'electron':
        lumi_periods_ = lumi_periods_2018[ 'electron' ]

lumi_weights_ = None
probs_lumi_ = None
if runOnMC_:
    print ( "Data periods: ", data_periods_ )
    lumi_weights_ = pd.Series( lumi_periods_ )
    lumi_weights_ = lumi_weights_.loc[ data_periods_ ]
    probs_lumi_ = lumi_weights_ / lumi_weights_.sum()
    print ( "Data periods: ", data_periods_ )
    print ( "Lumi values: ", lumi_weights_)
    probs_lumi_ = lumi_weights_ / np.sum( lumi_weights_ )
    print ( "Prob. lumi: ", probs_lumi_ )

ranges_crossing_angles_ = None
if data_sample_ == '2017':
    ranges_crossing_angles_ = [ 100., 130., 140., 150., 200. ]
elif data_sample_ == '2018':
    ranges_crossing_angles_ = [ 120., 140., 150., 170. ]

how_ = None

######################################################################################################
# Read proton files
protons_mix_all_ = None
protons_multiRP_mix_all_ = None
protons_singleRP_mix_all_ = None
if mix_protons_:
    # if version == "V1":
    #     protons_mix_all_ = {}
    # elif version == "V2":
    #     protons_multiRP_mix_all_ = {}
    #     protons_singleRP_mix_all_ = {}
    protons_mix_all_ = {}

    for file_ in proton_files:
        print ( file_ ) 
        root_ = uproot.open( file_ )
        
        print ( "Number of events in tree: {}".format( np.array( root_[ tree_path_proton_files_ + "/EventNum" ] ).size ) )
        
        tree_ = root_[ tree_path_proton_files_ ]

        keys_nonproton_ = [ "Run", "LumiSection", "EventNum", "CrossingAngle" ]
        keys_proton_ = tree_.keys( filter_name="ProtCand*")
        keys_ = []
        keys_.extend( keys_nonproton_ )
        keys_.extend( keys_proton_ )
        print ( keys_ )
            
        for events_ in tree_.iterate( keys_ , library="ak", how=how_, step_size=2000000 ):
            events_size_ = len( events_ )
            print ( events_, events_size_ )
            print ( "Applying prescale: {}".format( prescale_mix_protons_ ) )
            index_rnd_ = np.random.randint( events_size_, size=int( events_size_ / prescale_mix_protons_ ) )
            events_ = events_[ index_rnd_ ]
            events_size_ = len( events_ )
            print ( events_, events_size_ )

            # Fetch protons
            protons_ = None
            # protons_multiRP_ = None
            # protons_singleRP_ = None
            if how_ == "zip":
                protons_ = events_["ProtCand"]
                protons_[ "random" ] = ak.ones_like( protons_[ "arm" ] )
            elif how_ is None:
                arrays_proton_ = {}
                for key_ in keys_proton_: arrays_proton_[ key_[ len("ProtCand_") : ] ] = events_[ key_ ]
                arrays_proton_[ "random" ] = ak.ones_like( arrays_proton_[ "arm" ] )
                protons_ = ak.zip( arrays_proton_ )
        
            protons_[ "Run_rnd" ] = events_[ "Run" ]
            protons_[ "LumiSection_rnd" ] = events_[ "LumiSection" ]
            protons_[ "EventNum_rnd" ] = events_[ "EventNum" ]
            protons_[ "CrossingAngle_rnd" ] = events_[ "CrossingAngle" ]
            print ( protons_, len( protons_ ), ak.num( protons_ ) )
            # if version == "V2":
            #     protons_multiRP_ = protons_[ protons_.ismultirp == 1 ]
            #     protons_singleRP_ = protons_[ protons_.ismultirp == 0 ]
            #     print ( protons_multiRP_, len( protons_multiRP_ ), ak.num( protons_multiRP_ ) )
            #     print ( protons_singleRP_, len( protons_singleRP_ ), ak.num( protons_singleRP_ ) )

            for key_ in df_run_ranges_mixing_.index:
                msk_period_ = ( ( events_[ "Run" ] >= df_run_ranges_mixing_.loc[ key_ ][ "min" ] ) & ( events_[ "Run" ] <= df_run_ranges_mixing_.loc[ key_ ][ "max" ] ) )
                print ( key_, msk_period_, np.sum( msk_period_ ) )

                if len( events_[ msk_period_ ] ) > 0:
                    # if version == "V1":
                    #     if key_ not in protons_mix_all_.keys(): protons_mix_all_[ key_ ] = {}
                    # elif version == "V2":
                    #     if key_ not in protons_multiRP_mix_all_.keys(): protons_multiRP_mix_all_[ key_ ] = {}
                    #     if key_ not in protons_singleRP_mix_all_.keys(): protons_singleRP_mix_all_[ key_ ] = {}
                    if key_ not in protons_mix_all_.keys(): protons_mix_all_[ key_ ] = {}

                    for idx_, xangle_ in enumerate( ranges_crossing_angles_[:-1] ):
                        msk_xangle_ = ( ( events_[ "CrossingAngle" ][ msk_period_ ] >= xangle_ ) &
                                        ( events_[ "CrossingAngle" ][ msk_period_ ] < ranges_crossing_angles_[ idx_ + 1 ] ) )
                        key_xangle_ = int( xangle_ )
                        print ( key_xangle_, msk_xangle_, np.sum( msk_xangle_ ) )

                        if len( events_[ msk_period_ ][ msk_xangle_ ] ) > 0:
                            key_xangle_ = int( xangle_ )

                            # if version == "V1":
                            #     if key_xangle_ not in protons_mix_all_[ key_ ].keys():
                            #         protons_mix_all_[ key_ ][ key_xangle_ ] = protons_[ msk_period_ ][ msk_xangle_ ]
                            #     else:
                            #         protons_mix_all_[ key_ ][ key_xangle_ ] = ak.concatenate( [ protons_mix_all_[ key_ ][ key_xangle_ ], protons_[ msk_period_ ][ msk_xangle_ ] ], axis=0 )
                            # elif version == "V2":
                            #     if key_xangle_ not in protons_multiRP_mix_all_[ key_ ].keys():
                            #         protons_multiRP_mix_all_[ key_ ][ key_xangle_ ] = protons_multiRP_[ msk_period_ ][ msk_xangle_ ]
                            #     else:
                            #         protons_multiRP_mix_all_[ key_ ][ key_xangle_ ] = ak.concatenate( [ protons_multiRP_mix_all_[ key_ ][ key_xangle_ ], protons_multiRP_[ msk_period_ ][ msk_xangle_ ] ], axis=0 )
                            #     if key_xangle_ not in protons_singleRP_mix_all_[ key_ ].keys():
                            #         protons_singleRP_mix_all_[ key_ ][ key_xangle_ ] = protons_singleRP_[ msk_period_ ][ msk_xangle_ ]
                            #     else:
                            #         protons_singleRP_mix_all_[ key_ ][ key_xangle_ ] = ak.concatenate( [ protons_singleRP_mix_all_[ key_ ][ key_xangle_ ], protons_singleRP_[ msk_period_ ][ msk_xangle_ ] ], axis=0 )

                            if key_xangle_ not in protons_mix_all_[ key_ ].keys():
                                protons_mix_all_[ key_ ][ key_xangle_ ] = protons_[ msk_period_ ][ msk_xangle_ ]
                            else:
                                protons_mix_all_[ key_ ][ key_xangle_ ] = ak.concatenate( [ protons_mix_all_[ key_ ][ key_xangle_ ], protons_[ msk_period_ ][ msk_xangle_ ] ], axis=0 )
        # end iterate
    # end loop files
        
    print ( "Collections concatenated:" )
    # if version == "V1":
    #     print ( protons_mix_all_ )
    # elif version == "V2":
    #     print ( protons_multiRP_mix_all_ )
    #     print ( protons_singleRP_mix_all_ )
    print ( protons_mix_all_ )

    for key_ in df_run_ranges_mixing_.index:
        print ( key_ )
        if key_ in protons_mix_all_.keys():
            for xangle_ in ranges_crossing_angles_[:-1]:
                key_xangle_ = int( xangle_ )
                print ( key_xangle_ )

                # if version == "V1":
                #     if key_xangle_ in protons_mix_all_[ key_ ].keys():
                #         print ( protons_mix_all_[ key_ ][ key_xangle_ ], len( protons_mix_all_[ key_ ][ key_xangle_ ] ), ak.num( protons_mix_all_[ key_ ][ key_xangle_ ] ) )
                # elif version == "V2":
                #     if key_xangle_ in protons_multiRP_mix_all_[ key_ ].keys():
                #         print ( protons_multiRP_mix_all_[ key_ ][ key_xangle_ ], len( protons_multiRP_mix_all_[ key_ ][ key_xangle_ ] ), ak.num( protons_multiRP_mix_all_[ key_ ][ key_xangle_ ] ) )
                #         print ( protons_singleRP_mix_all_[ key_ ][ key_xangle_ ], len( protons_singleRP_mix_all_[ key_ ][ key_xangle_ ] ), ak.num( protons_singleRP_mix_all_[ key_ ][ key_xangle_ ] ) )

                if key_xangle_ in protons_mix_all_[ key_ ].keys():
                    print ( protons_mix_all_[ key_ ][ key_xangle_ ], len( protons_mix_all_[ key_ ][ key_xangle_ ] ), ak.num( protons_mix_all_[ key_ ][ key_xangle_ ] ) )

######################################################################################################

#entrystop_ = maxEvents_ if firstEvent_ is None else ( firstEvent_ + maxEvents_ )
entrystop_ = None
if firstEvent_ is None:
    entrystop_ = maxEvents_
else:
    if not maxEvents_ is None:
        entrystop_  = ( firstEvent_ + maxEvents_ )

np.random.seed( 42 )

dset_chunk_size = 200000

columns = [ "Run", "LumiSection", "BX", "EventNum", "Slice", "CrossingAngle", "random",
            "MultiRP", "Arm", "RPId1", "RPId2", "TrackX1", "TrackY1", "TrackX2", "TrackY2",
            "Xi", "T", "ThX", "ThY", "Time",
            "TrackThX_SingleRP", "TrackThY_SingleRP",
            "Track1ThX_MultiRP", "Track1ThY_MultiRP", "Track2ThX_MultiRP", "Track2ThY_MultiRP",
            "TrackPixShift_SingleRP", "Track1PixShift_MultiRP", "Track2PixShift_MultiRP",
            "Muon0Pt", "Muon0Eta", "Muon0Phi", "Muon0VtxZ", "Muon1Pt", "Muon1Eta", "Muon1Phi", "Muon1VtxZ",
            "nVertices", "PrimVertexZ", "InvMass", "ExtraPfCands", "Acopl", "XiMuMuPlus", "XiMuMuMinus" ]

if random_protons_ or mix_protons_:
    columns.extend( [ "Run_rnd", "LumiSection_rnd", "EventNum_rnd", "CrossingAngle_rnd" ] )

if runOnMC_:
    columns.extend( [ "Run_mc" ] )

protons_keys = {}
for col_ in columns:
    protons_keys[ col_ ] = col_
protons_keys[ "MultiRP" ] = "ismultirp"
protons_keys[ "Arm" ] = "arm"
protons_keys[ "RPId1" ] = "rpid1"
protons_keys[ "RPId2" ] = "rpid2"
protons_keys[ "TrackX1" ] = "trackx1"
protons_keys[ "TrackY1" ] = "tracky1"
protons_keys[ "TrackX2" ] = "trackx2"
protons_keys[ "TrackY2" ] = "tracky2"
protons_keys[ "Xi" ] = "xi"
protons_keys[ "T" ] = "t"
protons_keys[ "Time" ] = "time"
protons_keys[ "TrackThX_SingleRP" ] = "trackthx_single"
protons_keys[ "TrackThY_SingleRP" ] = "trackthy_single"
protons_keys[ "Track1ThX_MultiRP" ] = "trackthx_multi1"
protons_keys[ "Track1ThY_MultiRP" ] = "trackthy_multi1"
protons_keys[ "Track2ThX_MultiRP" ] = "trackthx_multi2"
protons_keys[ "Track2ThY_MultiRP" ] = "trackthy_multi2"
protons_keys[ "TrackPixShift_SingleRP" ] = "trackpixshift_single"
protons_keys[ "Track1PixShift_MultiRP" ] = "trackpixshift_multi1"
protons_keys[ "Track2PixShift_MultiRP" ] = "trackpixshift_multi2"
protons_keys[ "ExtraPfCands" ] = "nExtraPfCandPV3"

counts_label_protons_ = "Protons" if not random_protons_ else "ProtonsRnd"

with h5py.File( 'output-' + label_ + '.h5', 'w') as f:

    dset = None
    dset_protons_multiRP = None
    dset_protons_singleRP = None
    if version_ == "V1":
        dset = f.create_dataset( 'protons', ( dset_chunk_size, len( columns ) ), compression="gzip", chunks=True, maxshape=( None , len( columns ) ) )
        print ( "Initial dataset shape: {}".format( dset.shape ) )
    elif version_ == "V2":
        dset_protons_multiRP = f.create_dataset( 'protons_multiRP', ( dset_chunk_size, len( columns ) ), compression="gzip", chunks=True, maxshape=( None , len( columns ) ) )
        print ( "Initial dataset shape: {}".format( dset_protons_multiRP.shape ) )
    
        dset_protons_singleRP = f.create_dataset( 'protons_singleRP', ( dset_chunk_size, len( columns ) ), compression="gzip", chunks=True, maxshape=( None , len( columns ) ) )
        print ( "Initial dataset shape: {}".format( dset_protons_singleRP.shape ) )

    protons_list = None
    protons_multiRP_list = None
    protons_singleRP_list = None
    if version_ == "V1":
        protons_list = {}
        for col_ in columns:
            protons_list[ col_ ] = []
    elif version_ == "V2":
        protons_multiRP_list = {}
        for col_ in columns:
            protons_multiRP_list[ col_ ] = []           
    
        protons_singleRP_list = {}
        for col_ in columns:
            protons_singleRP_list[ col_ ] = []           

    
    selections = None
    counts = None
    
    dset_slice = 0
    dset_idx = 0
    dset_entries = 0

    dset_multiRP_slice = 0
    dset_multiRP_idx = 0
    dset_multiRP_entries = 0

    dset_singleRP_slice = 0
    dset_singleRP_idx = 0
    dset_singleRP_entries = 0

    for file_ in fileNames_:
        print ( file_ ) 
        root_ = uproot.open( file_ )

        print ( "Number of events in tree: {}".format( np.array( root_[ tree_path_ + "/EventNum" ] ).size ) )

        tree_ = root_[ tree_path_ ]
 
        keys = ["Run", "LumiSection", "BX", "EventNum", "CrossingAngle","nHLT", "HLT_Accept", "HLT_Prescl", "HLT_Name",
            "nMuonCand", "MuonCand_pt", "MuonCand_eta", "MuonCand_phi", "MuonCand_e", "MuonCand_charge", "MuonCand_vtxz", "MuonCand_istight",
            "nPrimVertexCand", "PrimVertexCand_z", "PrimVertexCand_chi2", "PrimVertexCand_ndof", "PrimVertexCand_tracks",
            "Weight", "PUWeightTrue"]
        keys.append( "nPfCand" )
        keys.extend( tree_.keys( filter_name="PfCand*" ) ) 
        keys.append( "nRecoProtCand" )
        keys_proton = tree_.keys( filter_name="ProtCand*" )
        keys.extend( keys_proton )  
        print ( keys )
        
        print ( "entry start={} entry stop={}".format( firstEvent_, entrystop_ ) )

        for events_ in tree_.iterate( keys , library="ak", how=how_, step_size=read_size_, entry_start=firstEvent_, entry_stop=entrystop_ ):
            print ( len(events_), events_ )
            
            if runOnMC_:
                sample_idx_arr_ = np.random.choice( np.arange( probs_lumi_.index.size ), len( events_ ), p=probs_lumi_ )
                print ( "Sampled index: ", sample_idx_arr_ )
                run_arr_ = np.apply_along_axis( lambda idx_: df_run_ranges_.loc[ probs_lumi_.index[ idx_ ] ][ "min" ], 0, sample_idx_arr_ )
                print ( "Run numbers: ", run_arr_ )
                events_[ "Run_mc" ] = run_arr_

            events_sel_, selections_, counts_ = select_events( events_, how=how_, keys=keys, minPt1=min_pt_1_, minPt2=min_pt_2_, apply_exclusive=apply_exclusive_ )
            events_ = events_sel_

            # Repeat events by resample factor
            if resample_:
                counts_ = counts_ * resample_factor_
    
            if selections is None:
                selections = selections_
                counts = counts_
            else:
                msk_selections = np.full_like( selections, False, dtype='bool' )
                for key in selections_:
                    msk_selections |= ( selections == key )
                counts[ msk_selections ] += counts_
    
            # Repeat events by resample factor
            slices_ = np.zeros( len( events_ ), dtype=np.int32 )
            if resample_:
                events_size_ = len( events_ )
                events_ = ak.concatenate( ( [events_] * resample_factor_ ), axis=0 )
                slices_ = np.zeros( resample_factor_ * events_size_, dtype=np.int32 )
                for idx_ in range( resample_factor_ ):
                    slices_[ ( idx_ * events_size_ ) : ( ( idx_ + 1 ) * events_size_ ) ] = idx_
            
            events_[ "Slice" ] = slices_
            
            protons_ = None
            if how_ == "zip":
                protons_ = events_["ProtCand"]
                if random_protons_:
                    protons_[ "random" ] = ak.ones_like( arrays_proton[ "arm" ] )
                else:
                    protons_[ "random" ] = ak.zeros_like( arrays_proton[ "arm" ] )
            elif how_ is None:
                arrays_proton = {}
                for key_ in keys_proton: arrays_proton[ key_[ len("ProtCand_") : ] ] = events_[ key_ ]
                if random_protons_:
                    arrays_proton[ "random" ] = ak.ones_like( arrays_proton[ "arm" ] )
                else:
                    arrays_proton[ "random" ] = ak.zeros_like( arrays_proton[ "arm" ] )
                protons_ = ak.zip( arrays_proton )

            # Randomize proton arrays
            run_rnd_ = None
            lumiblock_rnd_ = None
            event_rnd_ = None
            crossingAngle_rnd_ = None
            if random_protons_:
                # protons_sel_ = events_sel_.ProtCand
                # index_rnd_ = np.random.permutation( len( events_sel_ ) )
                # protons_rnd_ = protons_sel_[ index_rnd_ ]
                # events_sel_[ "ProtCandRnd" ] = protons_rnd_    
                # print ( "Num protons: {}".format( ak.num( events_sel_.ProtCand ) ) )
                # print ( "Num protons randomized: {}".format( ak.num( events_sel_.ProtCandRnd ) ) )
                # index_rnd_ = np.random.permutation( len( events_sel_ ) )

                index_rnd_ = np.random.permutation( len( events_ ) )
                print ( index_rnd_ )
                
                events_run_ = events_[ "Run" ]
                events_lumiblock_ = events_[ "LumiSection" ]
                events_event_ = events_[ "EventNum" ]
                events_crossingAngle_ = events_[ "CrossingAngle" ]

                run_rnd_ = events_run_[ index_rnd_ ]
                lumiblock_rnd_ = events_lumiblock_[ index_rnd_ ]
                event_rnd_ = events_event_[ index_rnd_ ]
                crossingAngle_rnd_ = events_crossingAngle_[ index_rnd_ ]

                protons_rnd_ = protons_[ index_rnd_ ]

                print ( "Run: {}".format( events_run_ ) ) 
                print ( "Run randomized: {}".format( run_rnd_ ) ) 
                print ( "Lumi: {}".format( events_lumiblock_ ) ) 
                print ( "Lumi randomized: {}".format( lumiblock_rnd_ ) ) 
                print ( "Event: {}".format( events_event_ ) ) 
                print ( "Event randomized: {}".format( event_rnd_ ) ) 
                print ( "Crossing angle: {}".format( events_crossingAngle_ ) ) 
                print ( "Crossing angle randomized: {}".format( crossingAngle_rnd_ ) ) 
                print ( "Num protons: {}".format( ak.num( protons_ ) ) )
                print ( "Num protons randomized: {}".format( ak.num( protons_rnd_ ) ) )
    
                protons_ = protons_rnd_

            elif mix_protons_:
                print ( "Num protons: {}".format( ak.num( protons_ ) ) )
                run_str_ = "Run_mc" if runOnMC_ else "Run"
                events_mix_ = {}
                protons_mix_ = {}
                 
                for key_ in df_run_ranges_mixing_.index:
                    msk_period_ = ( ( events_[ run_str_ ] >= df_run_ranges_mixing_.loc[ key_ ][ "min" ] ) & ( events_[ run_str_ ] <= df_run_ranges_mixing_.loc[ key_ ][ "max" ] ) )
                    print ( key_, msk_period_, np.sum( msk_period_ ) )

                    if len( events_[ msk_period_ ] ) > 0:
                        if key_ not in events_mix_.keys(): events_mix_[ key_ ] = {}
                        if key_ not in protons_mix_.keys(): protons_mix_[ key_ ] = {}

                        for idx_, xangle_ in enumerate( ranges_crossing_angles_[:-1] ):
                            msk_xangle_ = ( ( events_[ "CrossingAngle" ][ msk_period_ ] >= xangle_ ) &
                                            ( events_[ "CrossingAngle" ][ msk_period_ ] < ranges_crossing_angles_[ idx_ + 1 ] ) )
                            key_xangle_ = int( xangle_ )
                            print ( key_xangle_, msk_xangle_, np.sum( msk_xangle_ ) )

                            events_size_ = len( events_[ msk_period_ ][ msk_xangle_ ] )
                            if events_size_ > 0:
                                protons_mix_size_ = len( protons_mix_all_[ key_ ][ key_xangle_ ] )
                                index_rnd_ = np.random.randint( protons_mix_size_, size=events_size_ )

                                events_mix__ = events_[ msk_period_ ][ msk_xangle_ ]
                                if key_xangle_ not in events_mix_[ key_ ].keys():
                                    events_mix_[ key_ ][ key_xangle_ ] = events_mix__
                                else:
                                    events_mix_[ key_ ][ key_xangle_ ] = ak.concatenate( [ events_mix_[ key_ ][ key_xangle_ ], events_mix__ ], axis=0 )

                                protons_mix__ = protons_mix_all_[ key_ ][ key_xangle_ ][ index_rnd_ ] 
                                if key_xangle_ not in protons_mix_[ key_ ].keys():
                                    protons_mix_[ key_ ][ key_xangle_ ] = protons_mix__
                                else:
                                    protons_mix_[ key_ ][ key_xangle_ ] = ak.concatenate( [ protons_mix_[ key_ ][ key_xangle_ ], protons_mix__ ], axis=0 )

                events_mix_all_periods_ = None
                protons_mix_all_periods_ = None
                for key_ in df_run_ranges_mixing_.index:
                    for xangle_ in ranges_crossing_angles_[:-1]:
                        key_xangle_ = int( xangle_ )
                        print ( key_xangle_ ) 
                        if key_xangle_ in events_mix_[ key_ ].keys():
                            events_mix__ = events_mix_[ key_ ][ key_xangle_ ]
                            if events_mix_all_periods_ is None:
                                events_mix_all_periods_ = events_mix__
                            else:
                                events_mix_all_periods_ = ak.concatenate( [ events_mix_all_periods_, events_mix__ ], axis=0 ) 

                            protons_mix__ = protons_mix_[ key_ ][ key_xangle_ ]
                            if protons_mix_all_periods_ is None:
                                protons_mix_all_periods_ = protons_mix__
                            else:
                                protons_mix_all_periods_ = ak.concatenate( [ protons_mix_all_periods_, protons_mix__ ], axis=0 )

                events_ = events_mix_all_periods_
                protons_ = protons_mix_all_periods_

                if runOnMC_:
                    print ( "Run MC: {}".format( events_[ "Run_mc" ] ) )
                else:
                    print ( "Run: {}".format( events_[ "Run" ] ) )
                print ( "Run mixed: {}".format( protons_[ "Run_rnd" ] ) ) 

                print ( "Num protons mixed: {}".format( ak.num( protons_ ) ) )

            # end if

            print ( "Num protons: {}".format( ak.num( protons_ ) ) )

            # protons_ = None
            # protons_multiRP_ = None
            # protons_singleRP_ = None
            # if version_ == "V1":
            #     if not random_protons_: protons_ = select_protons( events_sel_, "ProtCand", version=version_ )
            #     else:                   protons_ = select_protons( events_sel_, "ProtCandRnd", version=version_ )    
            #     print ( "Num protons: {}".format( ak.num( protons_ ) ) )
            # elif version_ == "V2":
            #     if not random_protons_: protons_multiRP_, protons_singleRP_ = select_protons( events_sel_, branchName="ProtCand", apply_doublearm=apply_doublearm_, version=version_ )
            #     else:                   protons_multiRP_, protons_singleRP_ = select_protons( events_sel_, branchName="ProtCandRnd", apply_doublearm=apply_doublearm_, version=version_ )    
            #     print ( "Num protons: {}".format( ak.num( protons_multiRP_ ) ) )
            #     print ( "Num protons: {}".format( ak.num( protons_singleRP_ ) ) )

            protons_["Run"] = events_[ "Run" ]
            protons_["LumiSection"] = events_[ "LumiSection" ]
            protons_["BX"] = events_[ "BX" ]
            protons_["EventNum"] = events_[ "EventNum" ]
            protons_["Slice"] = events_[ "Slice" ]
            protons_["CrossingAngle"] = events_[ "CrossingAngle" ]
            if runOnMC_:
                protons_["Run_mc"] = events_["Run_mc"]

            if random_protons_:
                protons_["Run_rnd"] = run_rnd_
                protons_["LumiSection_rnd"] = lumiblock_rnd_
                protons_["EventNum_rnd"] = event_rnd_
                protons_["CrossingAngle_rnd"] = crossingAngle_rnd_

            if how_ == 'zip':
                protons_["Muon0Pt"] = events_.MuonCand.pt[:,0]
                protons_["Muon0Eta"] = events_.MuonCand.eta[:,0]
                protons_["Muon0Phi"] = events_.MuonCand.phi[:,0]
                protons_["Muon0VtxZ"] = events_.MuonCand.vtxz[:,0]
                protons_["Muon1Pt"] = events_.MuonCand.pt[:,1]
                protons_["Muon1Eta"] = events_.MuonCand.eta[:,1]
                protons_["Muon1Phi"] = events_.MuonCand.phi[:,1]
                protons_["Muon1VtxZ"] = events_.MuonCand.vtxz[:,1]
                protons_["PrimVertexZ"] = events_.PrimVertexCand.z[:,0]
            else:
                protons_["Muon0Pt"] = events_.MuonCand_pt[:,0]
                protons_["Muon0Eta"] = events_.MuonCand_eta[:,0]
                protons_["Muon0Phi"] = events_.MuonCand_phi[:,0]
                protons_["Muon0VtxZ"] = events_.MuonCand_vtxz[:,0]
                protons_["Muon1Pt"] = events_.MuonCand_pt[:,1]
                protons_["Muon1Eta"] = events_.MuonCand_eta[:,1]
                protons_["Muon1Phi"] = events_.MuonCand_phi[:,1]
                protons_["Muon1VtxZ"] = events_.MuonCand_vtxz[:,1]
                protons_["PrimVertexZ"] = events_.PrimVertexCand_z[:,0]

            protons_["nVertices"] = events_[ "nVertices" ]
            protons_["InvMass"] = events_[ "InvMass" ]
            protons_["nExtraPfCandPV3"] = events_[ "nExtraPfCandPV3" ]
            protons_["Acopl"] = events_[ "Acopl" ]
            protons_["XiMuMuPlus"] = events_[ "XiMuMuPlus" ]
            protons_["XiMuMuMinus"] = events_[ "XiMuMuMinus" ]

            check_none_ = ak.is_none( protons_ )
            arr_check_none_ = np.array( check_none_ ).astype("int32")
            print( "check_none", np.sum( arr_check_none_ ), check_none_ )
            msk_check_none_ = np.invert( check_none_ )
            print( msk_check_none_ )
            protons_ = protons_[ msk_check_none_ ]

            counts_protons_check_none_ = len( protons_ )
            counts_label__ = counts_label_protons_ + "_check_none"
            if not counts_label__ in selections:
                selections = np.concatenate( ( selections, np.array( [ counts_label__ ] ) ) )
                counts = np.concatenate( ( counts, np.array( [ counts_protons_check_none_ ] ) ) )
            else:    
                counts[ selections == counts_label__ ] += counts_protons_check_none_

            protons_singleRP_ = None
            protons_multiRP_ = None
            if version_ == "V1":
                msk_num_prot = ( ak.num( protons_ ) > 0 )
                protons_ = protons_[ msk_num_prot ]
            elif version_ == "V2":
                protons_singleRP_ = protons_[ protons_.ismultirp == 0 ]
                protons_multiRP_ = protons_[ protons_.ismultirp == 1 ]
                
                protons_multiRP_byArm_ = {}
                for arm in ( 0, 1 ):
                    protons_multiRP_byArm_[ arm ] = protons_multiRP_[ protons_multiRP_.arm == arm ]

                    print ( "Num multi-RP protons Arm {}: {}".format( arm, ak.num( protons_multiRP_byArm_[ arm ] ) ) )
                    if debug_:
                        print ( ak.to_list( protons_multiRP_byArm_[ arm ] ) )

                msk_  = np.array( ak.num( protons_multiRP_byArm_[ 0 ] ) > 0 )
                if apply_doublearm_:
                    msk_ &= np.array( ak.num( protons_multiRP_byArm_[ 1 ] ) > 0 )
                else:
                    msk_ |= np.array( ak.num( protons_multiRP_byArm_[ 1 ] ) > 0 )

                protons_multiRP_ = protons_multiRP_[ msk_ ]
                protons_singleRP_ = protons_singleRP_[ msk_ ]

            counts_protons_= -1
            if version_ == "V1":
                counts_protons_ = len( protons_ )
            elif version_ == "V2":
                counts_protons_ = len( protons_multiRP_ )

            if not counts_label_protons_ in selections:
                selections = np.concatenate( ( selections, np.array( [ counts_label_protons_ ] ) ) )
                counts = np.concatenate( ( counts, np.array( [counts_protons_] ) ) )
            else:    
                counts[ selections == counts_label_protons_ ] += counts_protons_ 

            print ( selections )
            print ( counts )

            if version_ == "V1":
                for col_ in columns:
                    protons_list[ col_ ] = np.array( ak.flatten( protons_[ protons_keys[ col_ ] ] ) )
                arr_size_ = len( protons_list[ "Xi" ] )
                print ( "Flattened array size: {}".format( arr_size_ ) )

                dset_entries += arr_size_

                if dset_entries > dset_chunk_size:
                    resize_factor_ = ( dset_entries // dset_chunk_size )
                    chunk_resize_  = resize_factor_ * dset_chunk_size

                    print ( "Resizing output dataset by {} entries.".format( chunk_resize_ ) )
                    dset.resize( ( dset.shape[0] + chunk_resize_ ), axis=0 )
                    print ( "Dataset shape: {}".format( dset.shape ) )
                            
                    dset_slice += resize_factor_
                    # Count the rest to the chunk size 
                    dset_entries = ( dset_entries % dset_chunk_size )

                print ( "Stacking data." )
                data_ = np.stack( list( protons_list.values() ), axis=1 )
                print ( data_.shape )
                print ( data_ )

                dset_idx_next_ = dset_idx + arr_size_
                print ( "Slice: {}".format( dset_slice ) )
                print ( "Writing in positions ({},{})".format( dset_idx, dset_idx_next_ ) )
                dset[ dset_idx : dset_idx_next_ ] = data_
                dset_idx = dset_idx_next_ 
            elif version_ == "V2":
                for col_ in columns:
                    protons_multiRP_list[ col_ ] = np.array( ak.flatten( protons_multiRP_[ protons_keys[ col_ ] ] ) )
                arr_size_multiRP_ = len( protons_multiRP_list[ "Xi" ] )
                print ( "Flattened array size multi-RP: {}".format( arr_size_multiRP_ ) )

                for col_ in columns:
                    protons_singleRP_list[ col_ ] = np.array( ak.flatten( protons_singleRP_[ protons_keys[ col_ ] ] ) )
                arr_size_singleRP_ = len( protons_singleRP_list[ "Xi" ] )
                print ( "Flattened array size single-RP: {}".format( arr_size_singleRP_ ) )

                dset_multiRP_entries += arr_size_multiRP_
                dset_singleRP_entries += arr_size_singleRP_

                if dset_multiRP_entries > dset_chunk_size:
                    resize_factor_ = ( dset_multiRP_entries // dset_chunk_size )
                    chunk_resize_  = resize_factor_ * dset_chunk_size

                    print ( "Resizing output dataset by {} entries.".format( chunk_resize_ ) )
                    dset_protons_multiRP.resize( ( dset_protons_multiRP.shape[0] + chunk_resize_ ), axis=0 )
                    print ( "Dataset shape: {}".format( dset_protons_multiRP.shape ) )
                            
                    dset_multiRP_slice += resize_factor_
                    # Count the rest to the chunk size 
                    dset_multiRP_entries = ( dset_multiRP_entries % dset_chunk_size )
                                 
                if dset_singleRP_entries > dset_chunk_size:
                    resize_factor_ = ( dset_singleRP_entries // dset_chunk_size )
                    chunk_resize_  = resize_factor_ * dset_chunk_size

                    print ( "Resizing output dataset by {} entries.".format( chunk_resize_ ) )
                    dset_protons_singleRP.resize( ( dset_protons_singleRP.shape[0] + chunk_resize_ ), axis=0 )
                    print ( "Dataset shape: {}".format( dset_protons_singleRP.shape ) )
                            
                    dset_singleRP_slice += resize_factor_
                    # Count the rest to the chunk size 
                    dset_singleRP_entries = ( dset_singleRP_entries % dset_chunk_size )
                                 
                print ( "Stacking data." )
                data_protons_multiRP_ = np.stack( list( protons_multiRP_list.values() ), axis=1 )
                print ( data_protons_multiRP_.shape )
                print ( data_protons_multiRP_ )

                data_protons_singleRP_ = np.stack( list( protons_singleRP_list.values() ), axis=1 )
                print ( data_protons_singleRP_.shape )
                print ( data_protons_singleRP_ )

                dset_idx_next_ = dset_multiRP_idx + arr_size_multiRP_
                print ( "Slice: {}".format( dset_multiRP_slice ) )
                print ( "Writing in positions ({},{})".format( dset_multiRP_idx, dset_idx_next_ ) )
                dset_protons_multiRP[ dset_multiRP_idx : dset_idx_next_ ] = data_protons_multiRP_
                dset_multiRP_idx = dset_idx_next_ 

                dset_idx_next_ = dset_singleRP_idx + arr_size_singleRP_
                print ( "Slice: {}".format( dset_singleRP_slice ) )
                print ( "Writing in positions ({},{})".format( dset_singleRP_idx, dset_idx_next_ ) )
                dset_protons_singleRP[ dset_singleRP_idx : dset_idx_next_ ] = data_protons_singleRP_
                dset_singleRP_idx = dset_idx_next_ 

        # Iteration on input files
        root_.close()

    if version_ == "V1":
        # Reduce dataset to its final size 
        print ( "Reduce dataset." )
        dset.resize( ( dset_idx ), axis=0 ) 
        print ( "Dataset shape: {}".format( dset.shape ) )

        print ( dset )
        print ( dset[-1] )   
    elif version_ == "V2":
        # Reduce dataset to its final size 
        print ( "Reduce dataset." )
        dset_protons_multiRP.resize( ( dset_multiRP_idx ), axis=0 ) 
        print ( "Dataset shape: {}".format( dset_protons_multiRP.shape ) )

        dset_protons_singleRP.resize( ( dset_singleRP_idx ), axis=0 ) 
        print ( "Dataset shape: {}".format( dset_protons_singleRP.shape ) )

        print ( dset_protons_multiRP )
        print ( dset_protons_multiRP[-1] )
        print ( dset_protons_singleRP )
        print ( dset_protons_singleRP[-1] )   

    print ( "Writing column names and event counts.")

    columns_ = np.array( columns, dtype='S' )
    print ( columns_ )

    event_counts_ = counts
    print ( event_counts_ )

    selections_ = np.array( selections, dtype='S' )
    print ( selections_ )

    dset_columns = f.create_dataset( 'columns', data=columns_ )
    dset_counts = f.create_dataset( 'event_counts', data=event_counts_ )
    dset_selections = f.create_dataset( 'selections', data=selections_ )

    print ( dset_columns )
    print ( list( dset_columns ) )   
    print ( dset_counts )
    print ( list( dset_counts ) )
    print ( dset_selections )
    print ( list( dset_selections ) )
