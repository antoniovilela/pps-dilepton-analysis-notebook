from processing import *

lepton_type = "muon"
data_sample = '2018'
base_path = "output"
output_dir = "output"

labels_signals = [ "GGToMuMu_Pt-25_Elastic", "GGToMuMu_Pt-25_Inel-El" ]

fileNames_signals_mix_protons = {
    'GGToMuMu_Pt-25_Elastic': [ 'output-test-GGToMuMu_Pt-25_Elastic-mix_protons-PreSel-Pt1_30-Pt2_20.h5' ],
    'GGToMuMu_Pt-25_Inel-El': [ 'output-test-GGToMuMu_Pt-25_Inel-El-mix_protons-PreSel-Pt1_30-Pt2_20.h5' ],
    }

for key_ in fileNames_signals_mix_protons:
    if base_path is not None and base_path != "":
        fileNames_signals_mix_protons[ key_ ] = [ "{}/{}".format( base_path, item_ ) for item_ in fileNames_signals_mix_protons[ key_ ] ]
print ( labels_signals )
print ( fileNames_signals_mix_protons )

for label_ in labels_signals:
    import time
    print( time.strftime("%Y/%m/%d %H:%M:%S", time.localtime() ) )
    time_s_ = time.time()

    file_path_ = None
    file_name_label_ =  "data-store-test-{}-mix_protons.h5".format( label_ )
    if output_dir is not None and output_dir != "":
        file_path_ = "{}/{}".format( output_dir, file_name_label_ )
    else:
        file_path_ = file_name_label_
    print ( file_path_ )
    with pd.HDFStore( file_path_, 'w', complevel=5 ) as store_:
        df_counts_, df_protons_multiRP_, df_protons_singleRP_ = get_data( fileNames_signals_mix_protons[ label_ ], version='V2' )
        df_protons_multiRP_index_, df_protons_multiRP_events_, df_protons_multiRP_2protons_ = process_data(
            df_protons_multiRP_,
            data_sample=data_sample,
            lepton_type=lepton_type,
            proton_selection='MultiRP',
            apply_fiducial=True,
            within_aperture=True,
            random_protons=False,
            mix_protons=True,
            runOnMC=True,
            select2protons=True
            )

        print ( df_protons_multiRP_2protons_ )
        store_[ "counts" ] = df_counts_
        store_[ "protons_multiRP"] = df_protons_multiRP_index_
        store_[ "events_multiRP" ] = df_protons_multiRP_events_
            
    time_e_ = time.time()
    print ( "Total time elapsed: {:.0f}".format( time_e_ - time_s_ ) )

    with pd.HDFStore( file_path_, 'r' ) as store_:
        print ( list( store_ ) )

