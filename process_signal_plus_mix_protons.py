import numpy as np
import pandas as pd
import h5py

from processing import *

def process_signal_plus_mix_protons( data_sample, labels_signals, labels_signals_mix_protons, label_signal_to_mix_protons, base_path='output', output_dir='output', use_hash_index=True, select2protons=False, nprot_value=3 ):

    base_path_ = base_path
    output_dir_ = output_dir

    # df_counts_signals = {}
    df_signals_protons_multiRP_index = {}
    # df_signals_protons_multiRP_events = {}
    for label_ in labels_signals:
        print ( label_ )
        file_path_ = "{}/data-store-test-{}.h5".format( base_path_, label_ )
        print ( file_path_ )
        with pd.HDFStore( file_path_, 'r' ) as store_:
            print ( list( store_ ) )
            # df_counts_signals[ label_ ] = store_[ "counts" ]
            df_signals_protons_multiRP_index[ label_ ] = store_[ "protons_multiRP" ]
            # df_signals_protons_multiRP_events[ label_ ] = store_[ "events_multiRP" ]

    # df_counts_signals_mix_protons = {}
    df_signals_protons_multiRP_mix_protons_index = {}
    # df_signals_protons_multiRP_mix_protons_events = {}
    for label_ in labels_signals_mix_protons:
        print ( label_ )
        file_path_ = "{}/data-store-test-{}.h5".format( base_path_, label_ )
        print ( file_path_ )
        with pd.HDFStore( file_path_, 'r' ) as store_:
            print ( list( store_ ) )
            # df_counts_signals_mix_protons[ label_ ] = store_[ "counts" ]
            df_signals_protons_multiRP_mix_protons_index[ label_ ] = store_[ "protons_multiRP" ]
            # df_signals_protons_multiRP_mix_protons_events[ label_ ] = store_[ "events_multiRP" ]

    # Signal with event mixing

    df_signals_protons_multiRP_eff_sel_index = {}
    df_signals_protons_multiRP_sig_plus_mix_index = {}

    np.random.seed( 12345 )

    index_vars_ = None
    if not use_hash_index:
        index_vars_ = [ 'Run', 'LumiSection', 'EventNum', 'Slice' ]
    else:
        index_vars_ = [ 'Run', 'LumiSection', 'EventNum', 'hash_id', 'Slice' ]
    print ( index_vars_ )

    df_signals_protons_multiRP_sig_plus_mix_xi_max = {}
    df_signals_protons_multiRP_sig_plus_mix_2protons = {}
    df_signals_protons_multiRP_sig_plus_mix_2protons_sig = {}
    df_signals_protons_multiRP_sig_plus_mix_1proton_sig_Arm0 = {}
    df_signals_protons_multiRP_sig_plus_mix_1proton_sig_Arm1 = {}
    df_signals_protons_multiRP_sig_plus_mix_2protons_mix = {}
    df_signals_protons_multiRP_sig_plus_mix_2protons_events = {}
    df_signals_protons_multiRP_sig_plus_mix_events_categories = {}
    for label_ in labels_signals:
        print ( label_ )
        
        file_path_ = None
        file_name_label_ = "data-store-test-signal-plus-mix-events-{}.h5".format( label_ )
        if output_dir_ is not None and output_dir_ != "":
            file_path_ = "{}/{}".format( output_dir_, file_name_label_ )
        else:
            file_path_ = file_name_label_
        print ( file_path_ )

        columns_protons_multiRP_ = df_signals_protons_multiRP_index[ label_ ].columns.values
        columns_ = columns_protons_multiRP_
        columns_eff_ = columns_[ [ key_[ : len('eff') ] == 'eff' for key_ in columns_ ] ]
        # columns_xi_  = columns_[ [ key_[ : len('xi_') ] == 'xi_' for key_ in columns_ ] ]

        columns_drop_ = [
            'MultiRP', 'Arm', 'RPId1', 'RPId2',
            'TrackX1', 'TrackY1', 'TrackX2', 'TrackY2',
            'TrackThX_SingleRP', 'TrackThY_SingleRP', 'Track1ThX_MultiRP', 'Track1ThY_MultiRP', 'Track2ThX_MultiRP', 'Track2ThY_MultiRP',
            'TrackPixShift_SingleRP', 'Track1PixShift_MultiRP', 'Track2PixShift_MultiRP',
            'Xi', 'T', 'ThX', 'ThY', 'Time'
        ]
        columns_drop_eff_xi_ = columns_drop_.copy()
        columns_drop_eff_xi_.extend( columns_eff_ )
        # columns_drop_eff_xi_.extend( columns_xi_ )

        # df_signals_protons_multiRP_mix_protons_index[ label_signal_to_mix_protons[ label_ ] ].loc[ :, "eff_proton_all" ] = 1.0
        # df_signals_protons_multiRP_mix_protons_index[ label_signal_to_mix_protons[ label_ ] ].loc[ :, "eff_proton_all_weighted" ] = 1.0
        # df_signals_protons_multiRP_mix_protons_index[ label_signal_to_mix_protons[ label_ ] ].loc[ :, "eff_proton_unc" ] = 0.0
        # if data_sample == '2017':
        #     df_signals_protons_multiRP_mix_protons_index[ label_signal_to_mix_protons[ label_ ] ].loc[ :, "eff_multitrack" ] = 1.0
        #     df_signals_protons_multiRP_mix_protons_index[ label_signal_to_mix_protons[ label_ ] ].loc[ :, "eff_strictzero" ] = 1.0
        #     df_signals_protons_multiRP_mix_protons_index[ label_signal_to_mix_protons[ label_ ] ].loc[ :, "eff_multitrack_weighted" ] = 1.0
        #     df_signals_protons_multiRP_mix_protons_index[ label_signal_to_mix_protons[ label_ ] ].loc[ :, "eff_strictzero_weighted" ] = 1.0

        # Random selection by efficiency weights
        msk_eff_proton_ = np.random.rand( df_signals_protons_multiRP_index[ label_ ].shape[0] ) < df_signals_protons_multiRP_index[ label_ ].loc[ :, "eff_proton_all" ]
        print ( msk_eff_proton_ )
        df_signals_protons_multiRP_eff_sel_index[ label_ ] = df_signals_protons_multiRP_index[ label_ ].loc[ msk_eff_proton_ ]
        df_signals_protons_multiRP_eff_sel_index[ label_ ][ 'random' ] = 1

        df_signals_protons_multiRP_sig_plus_mix_index[ label_ ] = pd.concat(
            [ df_signals_protons_multiRP_eff_sel_index[ label_ ],
              df_signals_protons_multiRP_mix_protons_index[ label_signal_to_mix_protons[ label_ ] ] ] ).sort_index()

        df_protons_multiRP_index_xi_max_ = process_events( data_sample, df_signals_protons_multiRP_sig_plus_mix_index[ label_ ], select2protons=False, runOnMC=True, columns_drop=columns_drop_eff_xi_, use_hash_index=use_hash_index, nprot_value=nprot_value )
        df_signals_protons_multiRP_sig_plus_mix_xi_max[ label_ ] = df_protons_multiRP_index_xi_max_

        if select2protons:

            if data_sample == '2017':
                df_protons_multiRP_groupby_arm_ = df_signals_protons_multiRP_sig_plus_mix_index[ label_ ][ [ "Arm" ] ].groupby( index_vars_ )
                msk_2protons_single_proton_ = df_protons_multiRP_groupby_arm_[ "Arm" ].transform( lambda s_: ( np.sum( s_ == 0 ) == 1 ) & ( np.sum( s_ == 1 ) == 1 ) )
                print ( msk_2protons_single_proton_, np.sum( msk_2protons_single_proton_ ) )
                df_signals_protons_multiRP_sig_plus_mix_2protons[ label_ ] = df_signals_protons_multiRP_sig_plus_mix_index[ label_ ].loc[ msk_2protons_single_proton_ ]
            elif data_sample == '2018':
                df_protons_multiRP_groupby_arm_ = df_signals_protons_multiRP_sig_plus_mix_index[ label_ ][ [ "Arm" ] ].groupby( index_vars_ )
                msk_2protons_ = df_protons_multiRP_groupby_arm_[ "Arm" ].transform( lambda s_: ( np.sum( s_ == 0 ) >= 1 ) & ( np.sum( s_ == 1 ) >= 1 ) )
                print ( msk_2protons_, np.sum( msk_2protons_ ) )
                df_signals_protons_multiRP_sig_plus_mix_2protons[ label_ ] = df_signals_protons_multiRP_sig_plus_mix_index[ label_ ].loc[ msk_2protons_ ]

            # Divide in categories
            df__ = df_signals_protons_multiRP_sig_plus_mix_2protons[ label_ ]
            df_protons_multiRP_groupby__ = df__[ [ "Arm", "random" ] ].groupby( index_vars_ )
            msk_sig_Arm0_ = df_protons_multiRP_groupby__.apply( lambda __df: np.sum( ( __df[ 'Arm' ] == 0 ) & ( __df[ 'random' ] == 0 ) ) == 1 )
            msk_sig_Arm1_ = df_protons_multiRP_groupby__.apply( lambda __df: np.sum( ( __df[ 'Arm' ] == 1 ) & ( __df[ 'random' ] == 0 ) ) == 1 )
            msk_2protons_ = ( msk_sig_Arm0_ & msk_sig_Arm1_ )
            msk_1proton_sig_Arm0_ = ( msk_sig_Arm0_ & ~msk_sig_Arm1_ )
            msk_1proton_sig_Arm1_ = ( ~msk_sig_Arm0_ & msk_sig_Arm1_ )
            msk_2protons_mix_ = ( ~msk_sig_Arm0_ & ~msk_sig_Arm1_ )
            print ( msk_2protons_, np.sum( msk_2protons_ ) )
            print ( msk_1proton_sig_Arm0_, np.sum( msk_1proton_sig_Arm0_ ) )
            print ( msk_1proton_sig_Arm1_, np.sum( msk_1proton_sig_Arm1_ ) )
            print ( msk_2protons_mix_, np.sum( msk_2protons_mix_ ) )

            if np.sum( msk_2protons_ ) > 0:
                df_signals_protons_multiRP_sig_plus_mix_2protons_sig[ label_ ] = df__.loc[ msk_2protons_ ]
            if np.sum( msk_1proton_sig_Arm0_ ) > 0:
                df_signals_protons_multiRP_sig_plus_mix_1proton_sig_Arm0[ label_ ] = df__.loc[ msk_1proton_sig_Arm0_ ]
            if np.sum( msk_1proton_sig_Arm1_ ) > 0:
                df_signals_protons_multiRP_sig_plus_mix_1proton_sig_Arm1[ label_ ] = df__.loc[ msk_1proton_sig_Arm1_ ]
            if np.sum( msk_2protons_mix_ ) > 0:
                df_signals_protons_multiRP_sig_plus_mix_2protons_mix[ label_ ] = df__.loc[ msk_2protons_mix_ ]

            
            df__ = df_signals_protons_multiRP_sig_plus_mix_2protons[ label_ ]
            df_xi_max__, df_protons_multiRP_events__, df_protons_multiRP_index_2protons__ = process_events( data_sample, df__, select2protons=True, runOnMC=True, columns_drop=columns_drop_eff_xi_, use_hash_index=use_hash_index, nprot_value=nprot_value )
            df_signals_protons_multiRP_sig_plus_mix_2protons_events[ label_ ] = df_protons_multiRP_events__

            df_signals_protons_multiRP_sig_plus_mix_events_categories[ label_ ] = {}
            if label_ in df_signals_protons_multiRP_sig_plus_mix_2protons_sig.keys():
                print ( "2protons_sig" )
                df__ = df_signals_protons_multiRP_sig_plus_mix_2protons_sig[ label_ ]
                df_xi_max__, df_protons_multiRP_events__, df_protons_multiRP_index_2protons__ = process_events( data_sample, df__, select2protons=True, runOnMC=True, columns_drop=columns_drop_eff_xi_, use_hash_index=use_hash_index, nprot_value=nprot_value )
                # df_signals_protons_multiRP_sig_plus_mix_2protons_sig_events[ label_ ] = df_protons_multiRP_events__
                df_signals_protons_multiRP_sig_plus_mix_events_categories[ label_ ][ '2protons_sig' ] = df_protons_multiRP_events__
            
            if label_ in df_signals_protons_multiRP_sig_plus_mix_1proton_sig_Arm0.keys():
                print ( "1proton_sig_Arm0" )
                df__ = df_signals_protons_multiRP_sig_plus_mix_1proton_sig_Arm0[ label_ ]
                df_xi_max__, df_protons_multiRP_events__, df_protons_multiRP_index_2protons__ = process_events( data_sample, df__, select2protons=True, runOnMC=True, columns_drop=columns_drop_eff_xi_, use_hash_index=use_hash_index, nprot_value=nprot_value )
                # df_signals_protons_multiRP_sig_plus_mix_1proton_sig_Arm0_events[ label_ ] = df_protons_multiRP_events__
                df_signals_protons_multiRP_sig_plus_mix_events_categories[ label_ ][ '1proton_sig_Arm0' ] = df_protons_multiRP_events__
            
            if label_ in df_signals_protons_multiRP_sig_plus_mix_1proton_sig_Arm1.keys():
                print ( "1proton_sig_Arm1" )
                df__ = df_signals_protons_multiRP_sig_plus_mix_1proton_sig_Arm1[ label_ ]
                df_xi_max__, df_protons_multiRP_events__, df_protons_multiRP_index_2protons__ = process_events( data_sample, df__, select2protons=True, runOnMC=True, columns_drop=columns_drop_eff_xi_, use_hash_index=use_hash_index, nprot_value=nprot_value )
                # df_signals_protons_multiRP_sig_plus_mix_1proton_sig_Arm1_events[ label_ ] = df_protons_multiRP_events__
                df_signals_protons_multiRP_sig_plus_mix_events_categories[ label_ ][ '1proton_sig_Arm1' ] = df_protons_multiRP_events__
            
            if label_ in df_signals_protons_multiRP_sig_plus_mix_2protons_mix.keys():
                print ( "2protons_mix" )
                df__ = df_signals_protons_multiRP_sig_plus_mix_2protons_mix[ label_ ]
                df_xi_max__, df_protons_multiRP_events__, df_protons_multiRP_index_2protons__ = process_events( data_sample, df__, select2protons=True, runOnMC=True, columns_drop=columns_drop_eff_xi_, use_hash_index=use_hash_index, nprot_value=nprot_value )
                # df_signals_protons_multiRP_sig_plus_mix_2protons_mix_events[ label_ ] = df_protons_multiRP_events__
                df_signals_protons_multiRP_sig_plus_mix_events_categories[ label_ ][ '2protons_mix' ] = df_protons_multiRP_events__

        with pd.HDFStore( file_path_, 'w', complevel=5 ) as store_:
            store_[ "protons_multiRP" ] = df_signals_protons_multiRP_sig_plus_mix_index[ label_ ]
            store_[ "protons_xiMax_multiRP" ] = df_signals_protons_multiRP_sig_plus_mix_xi_max[ label_ ]
            if select2protons:
                store_[ "events_multiRP/all" ] = df_signals_protons_multiRP_sig_plus_mix_2protons_events[ label_ ]
                for key_ in df_signals_protons_multiRP_sig_plus_mix_events_categories[ label_ ]:
                    store_[ "events_multiRP/{}".format( key_ ) ] = df_signals_protons_multiRP_sig_plus_mix_events_categories[ label_ ][ key_ ]
            print ( list( store_ ) )


if __name__ == '__main__':

    lepton_type = 'muon'

    data_sample = '2018'

    nprot_value = 3
     
    use_hash_index_ = True

    base_path_ = 'output'
    output_dir_ = 'output'

    # Signal
    labels_signals = []
    if data_sample == '2017':
        if lepton_type == 'muon':
            labels_signals = [ "GGToMuMu_Pt-25_Elastic", "GGToMuMu_Pt-25_Inel-El", "GGToMuMu_Pt-25_Inel-Inel" ]
        elif lepton_type == 'electron': pass
            # labels_signals = 
    elif data_sample == '2018':
        if lepton_type == 'muon':
            # labels_signals = [ "GGToMuMu_Pt-25_Elastic", "GGToMuMu_Pt-25_Inel-El", "GGToMuMu_Pt-25_Inel-Inel" ]
            labels_signals = [ "GGToMuMu_Pt-25_Inel-Inel" ]
        elif lepton_type == 'electron': pass
            # labels_signals = 

    labels_signals_mix_protons = []
    if data_sample == '2017':
        if lepton_type == 'muon':
            labels_signals_mix_protons = [ "GGToMuMu_Pt-25_Elastic-mix_protons", "GGToMuMu_Pt-25_Inel-El-mix_protons", "GGToMuMu_Pt-25_Inel-Inel-mix_protons" ]
        elif lepton_type == 'electron': pass
            # labels_signals_mix_protons = 
    elif data_sample == '2018':
        if lepton_type == 'muon':
            # labels_signals_mix_protons = [ "GGToMuMu_Pt-25_Elastic-mix_protons", "GGToMuMu_Pt-25_Inel-El-mix_protons", "GGToMuMu_Pt-25_Inel-Inel-mix_protons" ]
            labels_signals_mix_protons = [ "GGToMuMu_Pt-25_Inel-Inel-mix_protons" ]
        elif lepton_type == 'electron': pass
            # labels_signals_mix_protons = 

    label_signal_to_mix_protons = {}
    if data_sample == '2017':
        if lepton_type == 'muon':
            label_signal_to_mix_protons = {
                 "GGToMuMu_Pt-25_Elastic" : "GGToMuMu_Pt-25_Elastic-mix_protons",
                 "GGToMuMu_Pt-25_Inel-El" : "GGToMuMu_Pt-25_Inel-El-mix_protons",
                 "GGToMuMu_Pt-25_Inel-Inel" : "GGToMuMu_Pt-25_Inel-Inel-mix_protons"
            }
        elif lepton_type == 'electron': pass
            # label_signal_to_mix_protons = {}
    elif data_sample == '2018':
        if lepton_type == 'muon':
            label_signal_to_mix_protons = {
                 "GGToMuMu_Pt-25_Elastic" : "GGToMuMu_Pt-25_Elastic-mix_protons",
                 "GGToMuMu_Pt-25_Inel-El" : "GGToMuMu_Pt-25_Inel-El-mix_protons",
                 "GGToMuMu_Pt-25_Inel-Inel" : "GGToMuMu_Pt-25_Inel-Inel-mix_protons"
            }
        elif lepton_type == 'electron': pass
            # label_signal_to_mix_protons = {}

    process_signal_plus_mix_protons( data_sample=data_sample, labels_signals=labels_signals, labels_signals_mix_protons=labels_signals_mix_protons, label_signal_to_mix_protons=label_signal_to_mix_protons, base_path=base_path_, output_dir=output_dir_, use_hash_index=use_hash_index_, select2protons=True, nprot_value=nprot_value )

