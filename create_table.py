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

parser = argparse.ArgumentParser(description = 'Creates data table from ntuple.')
parser.add_argument('--files', help = 'File paths.' )
parser.add_argument('--label', help = 'Label suffix.' )
parser.add_argument('--apply_exclusive', dest = 'apply_exclusive', action = 'store_true', required = False, help = '' )
parser.add_argument('--apply_doublearm', dest = 'apply_doublearm', action = 'store_true', required = False, help = '' )
parser.add_argument('--min_pt_1', dest = 'min_pt_1', type=float, required = False, default = 50., help = '' )
parser.add_argument('--min_pt_2', dest = 'min_pt_2', type=float, required = False, default = 0., help = '' )
parser.add_argument('--random_protons', dest = 'random_protons', action = 'store_true', required = False, help = '' )
parser.add_argument('--resample_factor', dest = 'resample_factor', type = int, required = False, default = -1, help = '' )
parser.add_argument('-s', '--start', dest = 'start', type = int, required = False, default = -1, help = 'First event to process.' )
parser.add_argument('-n', '--events', dest = 'events', type = int, required = False, default = -1, help = 'Number of events to process.' )
parser.add_argument('--read_size', dest = 'read_size', required = False, default = "150MB" , help = 'Input buffer size.' )
parser.add_argument('--version', dest = 'version', required = False, default = "V1" , help = 'Version of data tables.' )
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

firstEvent_ = None
if hasattr( args, 'start' ) and args.start > 0: firstEvent_ = args.start
print ( "First event to process: {}".format( "from first" if firstEvent_ is None else firstEvent_ ) )

maxEvents_ = None
if hasattr( args, 'events' ) and args.events > 0: maxEvents_ = args.events
print ( "Number of events to process: {}".format( "to end" if maxEvents_ is None else maxEvents_ ) )

read_size_ = "150MB"
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

#entrystop_ = maxEvents_ if firstEvent_ is None else ( firstEvent_ + maxEvents_ )
entrystop_ = None
if firstEvent_ is None:
    entrystop_ = maxEvents_
else:
    if not maxEvents_ is None:
        entrystop_  = ( firstEvent_ + maxEvents_ )

np.random.seed( 42 )

dset_chunk_size = 50000

columns = ( "Run", "LumiSection", "BX", "EventNum", "Slice", "CrossingAngle",
            "MultiRP", "Arm", "RPId1", "RPId2", "TrackX1", "TrackY1", "TrackX2", "TrackY2",
            "Xi", "T", "ThX", "ThY", "Time",
            "TrackThX_SingleRP", "TrackThY_SingleRP",
            "Track1ThX_MultiRP", "Track1ThY_MultiRP", "Track2ThX_MultiRP", "Track2ThY_MultiRP",
            "TrackPixShift_SingleRP", "Track1PixShift_MultiRP", "Track2PixShift_MultiRP",
            "Muon0Pt", "Muon0Eta", "Muon0Phi", "Muon0VtxZ", "Muon1Pt", "Muon1Eta", "Muon1Phi", "Muon1VtxZ",
            "nVertices", "PrimVertexZ", "InvMass", "ExtraPfCands", "Acopl", "XiMuMuPlus", "XiMuMuMinus" )
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

        print ( "Number of events in tree: {}".format( np.array( root_["ggll_miniaod/ntp1/nMuonCand"] ).size ) )

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
        
        print ( "entry start={} entry stop={}".format( firstEvent_, entrystop_ ) )

        for events_ in tree_.iterate( keys , library="ak", how="zip", step_size=read_size_, entry_start=firstEvent_, entry_stop=entrystop_ ):
            print ( len(events_), events_ )
            
            #events_sel_ = select_events( events_, apply_exclusive_ )
            #events_sel_, selections_, counts_ = select_events( events_, apply_exclusive=apply_exclusive_ )
            events_sel_, selections_, counts_ = select_events( events_, minPt1=min_pt_1_, minPt2=min_pt_2_, apply_exclusive=apply_exclusive_ )
    
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
            slices_ = np.zeros( len( events_sel_ ), dtype=np.int32 )
            if resample_:
                events_size_ = len( events_sel_ )
                events_sel_ = ak.concatenate( ( [events_sel_] * resample_factor_ ), axis=0 )
                slices_ = np.zeros( resample_factor_ * events_size_, dtype=np.int32 )
                for idx_ in range( resample_factor_ ):
                    slices_[ ( idx_ * events_size_ ) : ( ( idx_ + 1 ) * events_size_ ) ] = idx_
            
            events_sel_[ "Slice" ] = slices_
                
            # Randomize proton arrays
            if random_protons_:
                protons_sel_ = events_sel_.ProtCand
            
                index_rnd_ = np.random.permutation( len( events_sel_ ) )
            
                protons_rnd_ = protons_sel_[ index_rnd_ ]
            
                events_sel_[ "ProtCandRnd" ] = protons_rnd_    
        
                print ( "Num protons: {}".format( ak.num( events_sel_.ProtCand ) ) )
                print ( "Num protons randomized: {}".format( ak.num( events_sel_.ProtCandRnd ) ) )
    
            #protons_ = select_protons( events_sel_ )
            protons_ = None
            protons_multiRP_ = None
            protons_singleRP_ = None
            if version_ == "V1":
                if not random_protons_: protons_ = select_protons( events_sel_, "ProtCand", version=version_ )
                else:                   protons_ = select_protons( events_sel_, "ProtCandRnd", version=version_ )    
                print ( "Num protons: {}".format( ak.num( protons_ ) ) )
            elif version_ == "V2":
                if not random_protons_: protons_multiRP_, protons_singleRP_ = select_protons( events_sel_, branchName="ProtCand", apply_doublearm=apply_doublearm_, version=version_ )
                else:                   protons_multiRP_, protons_singleRP_ = select_protons( events_sel_, branchName="ProtCandRnd", apply_doublearm=apply_doublearm_, version=version_ )    
                print ( "Num protons: {}".format( ak.num( protons_multiRP_ ) ) )
                print ( "Num protons: {}".format( ak.num( protons_singleRP_ ) ) )
  
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
