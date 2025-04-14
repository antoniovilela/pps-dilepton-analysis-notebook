from processing import *

lepton_type = "muon"
data_sample = '2018'
base_path = "output"
output_dir = "output"

labels_bkg = [
    "2018A-Excl-Pt1_30-Pt2_20-random-resample_50",
    "2018B-Excl-Pt1_30-Pt2_20-random-resample_50",
    "2018C-Excl-Pt1_30-Pt2_20-random-resample_50",
    "2018D-Excl-Pt1_30-Pt2_20-random-resample_50"
    ]

fileNames_bkg = {}
for key_ in labels_bkg: fileNames_bkg[ key_ ] = "output-test-{}.h5".format( key_ )
fileNames_bkg[ "2018A-Excl-Pt1_30-Pt2_20-random-resample_50" ] = [
    "output-test-2018A-Excl-Pt1_30-Pt2_20-random-resample_50_0_0.h5",
    "output-test-2018A-Excl-Pt1_30-Pt2_20-random-resample_50_0_1.h5",
    "output-test-2018A-Excl-Pt1_30-Pt2_20-random-resample_50_1_0.h5",
    "output-test-2018A-Excl-Pt1_30-Pt2_20-random-resample_50_1_1.h5",
    "output-test-2018A-Excl-Pt1_30-Pt2_20-random-resample_50_1_2.h5"
    ]
fileNames_bkg[ "2018B-Excl-Pt1_30-Pt2_20-random-resample_50" ] = [
    "output-test-2018B-Excl-Pt1_30-Pt2_20-random-resample_50_0.h5",
    "output-test-2018B-Excl-Pt1_30-Pt2_20-random-resample_50_1.h5"
    ]
fileNames_bkg[ "2018C-Excl-Pt1_30-Pt2_20-random-resample_50" ] = [
    "output-test-2018C-Excl-Pt1_30-Pt2_20-random-resample_50_0.h5",
    "output-test-2018C-Excl-Pt1_30-Pt2_20-random-resample_50_1.h5"
    ]
fileNames_bkg[ "2018D-Excl-Pt1_30-Pt2_20-random-resample_50" ] = [
    "output-test-2018D-Excl-Pt1_30-Pt2_20-random-resample_50_0_0.h5",
    "output-test-2018D-Excl-Pt1_30-Pt2_20-random-resample_50_0_1.h5",
    "output-test-2018D-Excl-Pt1_30-Pt2_20-random-resample_50_1_0.h5",
    "output-test-2018D-Excl-Pt1_30-Pt2_20-random-resample_50_1_1.h5",
    "output-test-2018D-Excl-Pt1_30-Pt2_20-random-resample_50_2_0.h5",
    "output-test-2018D-Excl-Pt1_30-Pt2_20-random-resample_50_2_1.h5",
    "output-test-2018D-Excl-Pt1_30-Pt2_20-random-resample_50_2_2.h5",
    "output-test-2018D-Excl-Pt1_30-Pt2_20-random-resample_50_3_0.h5",
    "output-test-2018D-Excl-Pt1_30-Pt2_20-random-resample_50_3_1.h5",
    "output-test-2018D-Excl-Pt1_30-Pt2_20-random-resample_50_3_2.h5"
    ]

for key_ in fileNames_bkg:
    if base_path is not None and base_path != "":
        fileNames_bkg[ key_ ] = [ "{}/{}".format( base_path, item_ ) for item_ in fileNames_bkg[ key_ ] ]
print ( labels_bkg )
print ( fileNames_bkg )

for label_ in labels_bkg:
    import time
    print( time.strftime("%Y/%m/%d %H:%M:%S", time.localtime() ) )
    time_s_ = time.time()

    file_path_ = None
    file_name_label_ =  "data-store-test-{}.h5".format( label_ )
    if output_dir is not None and output_dir != "":
        file_path_ = "{}/{}".format( output_dir, file_name_label_ )
    else:
        file_path_ = file_name_label_
    print ( file_path_ )
    with pd.HDFStore( file_path_, 'w', complevel=5 ) as store_:
        df_counts_, df_protons_multiRP_, df_protons_singleRP_ = get_data( fileNames_bkg[ label_ ], version='V2' )
        df_protons_multiRP_index_, df_protons_multiRP_events_, df_protons_multiRP_2protons_ = process_data(
            df_protons_multiRP_,
            data_sample=data_sample,
            lepton_type=lepton_type,
            proton_selection='MultiRP',
            apply_fiducial=True,
            within_aperture=True,
            random_protons=True,
            mix_protons=False,
            runOnMC=False,
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

