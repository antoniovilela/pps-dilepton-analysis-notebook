
import numpy as np
import pandas as pd
import h5py

# run_ranges_periods = {}
# run_ranges_periods[ "2017B" ]  = (297020,299329)
# run_ranges_periods[ "2017C1" ] = (299337,300785)
# run_ranges_periods[ "2017C2" ] = (300806,302029)
# run_ranges_periods[ "2017D" ]  = (302030,303434)
# run_ranges_periods[ "2017E" ]  = (303435,304826)
# run_ranges_periods[ "2017F1" ] = (304911,305114)
# run_ranges_periods[ "2017F2" ] = (305178,305902)
# run_ranges_periods[ "2017F3" ] = (305965,306462)
# df_run_ranges = pd.DataFrame( run_ranges_periods, index=("min","max") ).transpose()

run_ranges_periods_2017 = {}
run_ranges_periods_2017[ "2017B" ]  = (297020,299329)
run_ranges_periods_2017[ "2017C1" ] = (299337,300785)
run_ranges_periods_2017[ "2017C2" ] = (300806,302029)
run_ranges_periods_2017[ "2017D" ]  = (302030,303434)
run_ranges_periods_2017[ "2017E" ]  = (303435,304826)
run_ranges_periods_2017[ "2017F1" ] = (304911,305114)
run_ranges_periods_2017[ "2017F2" ] = (305178,305902)
run_ranges_periods_2017[ "2017F3" ] = (305965,306462)
df_run_ranges_2017 = pd.DataFrame( run_ranges_periods_2017, index=("min","max") ).transpose()
run_ranges_periods_mixing_2017 = run_ranges_periods_2017
df_run_ranges_mixing_2017 = df_run_ranges_2017
run_ranges_periods_2018 = {}
run_ranges_periods_2018[ "2018A" ]  = (315252,316995)
run_ranges_periods_2018[ "2018B1" ] = (316998,317696)
run_ranges_periods_2018[ "2018B2" ] = (318622,319312)
run_ranges_periods_2018[ "2018C" ]  = (319313,320393)
run_ranges_periods_2018[ "2018D1" ] = (320394,322633)
run_ranges_periods_2018[ "2018D2" ] = (323363,325273)
df_run_ranges_2018 = pd.DataFrame( run_ranges_periods_2018, index=("min","max") ).transpose()
run_ranges_periods_mixing_2018 = {}
run_ranges_periods_mixing_2018[ "2018A" ]  = (315252,316995)
run_ranges_periods_mixing_2018[ "2018B" ]  = (316998,319312)
run_ranges_periods_mixing_2018[ "2018C" ]  = (319313,320393)
run_ranges_periods_mixing_2018[ "2018D1" ] = (320394,322633)
run_ranges_periods_mixing_2018[ "2018D2" ] = (323363,325273)
df_run_ranges_mixing_2018 = pd.DataFrame( run_ranges_periods_mixing_2018, index=("min","max") ).transpose()

# L_2017B = 2.360904801;
# L_2017C1 = 5.313012839;
# L_2017E = 8.958810514;
# L_2017F1 = 1.708478656;
# L_2017C2 = 3.264135878;
# L_2017D = 4.074723964;
# L_2017F2 = 7.877903151;
# L_2017F3 = 3.632463163;
L_2017B = 4.799881474;
L_2017C1 = 5.785813941;
L_2017E = 9.312832062;
L_2017F1 = 1.738905587;
L_2017C2 = 3.786684323;
L_2017D = 4.247682053;
L_2017F2 = 8.125575961;
L_2017F3 = 3.674404546;
lumi_periods_2017 = {}
lumi_periods_2017[ 'muon' ] = {}
lumi_periods_2017[ 'muon' ][ "2017B" ]  = L_2017B
lumi_periods_2017[ 'muon' ][ "2017C1" ] = L_2017C1
lumi_periods_2017[ 'muon' ][ "2017C2" ] = L_2017C2
lumi_periods_2017[ 'muon' ][ "2017D" ]  = L_2017D
lumi_periods_2017[ 'muon' ][ "2017E" ]  = L_2017E
lumi_periods_2017[ 'muon' ][ "2017F1" ] = L_2017F1
lumi_periods_2017[ 'muon' ][ "2017F2" ] = L_2017F2
lumi_periods_2017[ 'muon' ][ "2017F3" ] = L_2017F3
lumi_periods_2017[ 'electron' ] = {}
lumi_periods_2017[ 'electron' ][ "2017B" ]  = L_2017B * 0.957127
lumi_periods_2017[ 'electron' ][ "2017C1" ] = L_2017C1 * 0.954282
lumi_periods_2017[ 'electron' ][ "2017C2" ] = L_2017C2 * 0.954282
lumi_periods_2017[ 'electron' ][ "2017D" ]  = L_2017D * 0.9539
lumi_periods_2017[ 'electron' ][ "2017E" ]  = L_2017E * 0.956406
lumi_periods_2017[ 'electron' ][ "2017F1" ] = L_2017F1 * 0.953733
lumi_periods_2017[ 'electron' ][ "2017F2" ] = L_2017F2 * 0.953733
lumi_periods_2017[ 'electron' ][ "2017F3" ] = L_2017F3 * 0.953733
print ( lumi_periods_2017 )
print ( "Luminosity 2017 muon: {}".format( np.sum( list( lumi_periods_2017[ 'muon' ].values() ) ) ) )
print ( "Luminosity 2017 electron: {}".format( np.sum( list( lumi_periods_2017[ 'electron' ].values() ) ) ) )

# L_2018A  = 12.10
# L_2018B1 = 6.38
# L_2018B2 = 0.40
# L_2018C  = 6.5297
# L_2018D1 = 19.88
# L_2018D2 = 10.4157
L_2018A  = 14.027047499
L_2018B1 = 6.629673574
L_2018B2 = 0.430948924
L_2018C  = 6.891747024
L_2018D1 = 20.962647459
L_2018D2 = 10.868724698
lumi_periods_2018 = {}
lumi_periods_2018[ 'muon' ] = {}
lumi_periods_2018[ 'muon' ][ "2018A" ]  = L_2018A * 0.999913
lumi_periods_2018[ 'muon' ][ "2018B1" ] = L_2018B1 * 0.998672
lumi_periods_2018[ 'muon' ][ "2018B2" ] = L_2018B2 * 0.998672
lumi_periods_2018[ 'muon' ][ "2018C" ]  = L_2018C * 0.999991
lumi_periods_2018[ 'muon' ][ "2018D1" ] = L_2018D1 * 0.998915
lumi_periods_2018[ 'muon' ][ "2018D2" ] = L_2018D2 * 0.998915
lumi_periods_2018[ 'electron' ] = {}
lumi_periods_2018[ 'electron' ][ "2018A" ]  = L_2018A * 0.933083
lumi_periods_2018[ 'electron' ][ "2018B1" ] = L_2018B1 * 0.999977
lumi_periods_2018[ 'electron' ][ "2018B2" ] = L_2018B2 * 0.999977
lumi_periods_2018[ 'electron' ][ "2018C" ]  = L_2018C * 0.999978
lumi_periods_2018[ 'electron' ][ "2018D1" ] = L_2018D1 * 0.999389
lumi_periods_2018[ 'electron' ][ "2018D2" ] = L_2018D2 * 0.999389
print ( lumi_periods_2018 )
print ( "Luminosity 2018 muon: {}".format( np.sum( list( lumi_periods_2018[ 'muon' ].values() ) ) ) )
print ( "Luminosity 2018 electron: {}".format( np.sum( list( lumi_periods_2018[ 'electron' ].values() ) ) ) )

# aperture_period_map = {
#     "2016_preTS2"  : "2016_preTS2",
#     "2016_postTS2" : "2016_postTS2",
#     "2017B"        : "2017_preTS2",
#     "2017C1"       : "2017_preTS2",
#     "2017C2"       : "2017_preTS2",
#     "2017D"        : "2017_preTS2",
#     "2017E"        : "2017_postTS2",
#     "2017F1"       : "2017_postTS2",
#     "2017F2"       : "2017_postTS2",
#     "2017F3"       : "2017_postTS2",
#     "2018"         : "2018"
# }
aperture_period_map = {
    "2016_preTS2"  : "2016_preTS2",
    "2016_postTS2" : "2016_postTS2",
    "2017B"        : "2017_preTS2",
    "2017C1"       : "2017_preTS2",
    "2017C2"       : "2017_preTS2",
    "2017D"        : "2017_preTS2",
    "2017E"        : "2017_postTS2",
    "2017F1"       : "2017_postTS2",
    "2017F2"       : "2017_postTS2",
    "2017F3"       : "2017_postTS2",
    "2018A"        : "2018",
    "2018B1"       : "2018",
    "2018B2"       : "2018",
    "2018C"        : "2018",
    "2018D1"       : "2018",
    "2018D2"       : "2018"
}
reco_period_map = {
    "2016_preTS2"  : "2016_preTS2",
    "2016_postTS2" : "2016_postTS2",
    "2017B"        : "2017_preTS2",
    "2017C1"       : "2017_preTS2",
    "2017C2"       : "2017_preTS2",
    "2017D"        : "2017_preTS2",
    "2017E"        : "2017_postTS2",
    "2017F1"       : "2017_postTS2",
    "2017F2"       : "2017_postTS2",
    "2017F3"       : "2017_postTS2",
    "2018A"        : "2018_preTS1",
    "2018B1"       : "2018_TS1_TS2",
    "2018B2"       : "2018_TS1_TS2",
    "2018C"        : "2018_TS1_TS2",
    "2018D1"       : "2018_postTS2",
    "2018D2"       : "2018_postTS2"
}

# Fiducial cuts (UL)
# Periods: "2017B", "2017C1", "2017E", "2017F1", "2018A", "2018B1", "2018B2", "2018C", "2018D1", "2018D2"
def fiducial_cuts():
    # Per data period, arm=(0,1), station=(0,2)
    fiducialXLow_ = {}
    fiducialXHigh_ = {}
    fiducialYLow_ = {}
    fiducialYHigh_ = {}

    data_periods = [ "2017B", "2017C1", "2017E", "2017F1", "2018A", "2018B1", "2018B2", "2018C", "2018D1", "2018D2" ]
    for period_ in data_periods:
        fiducialXLow_[ period_ ] = {}
        fiducialXLow_[ period_ ][ 0 ] = {}
        fiducialXLow_[ period_ ][ 1 ] = {}
        fiducialXHigh_[ period_ ] = {}
        fiducialXHigh_[ period_ ][ 0 ] = {}
        fiducialXHigh_[ period_ ][ 1 ] = {}
        fiducialYLow_[ period_ ] = {}
        fiducialYLow_[ period_ ][ 0 ] = {}
        fiducialYLow_[ period_ ][ 1 ] = {}
        fiducialYHigh_[ period_ ] = {}
        fiducialYHigh_[ period_ ][ 0 ] = {}
        fiducialYHigh_[ period_ ][ 1 ] = {}
        
    # 2017B
    # Sector 45, RP 220
    fiducialXLow_[ "2017B" ][ 0 ][ 2 ]  =   1.995;
    fiducialXHigh_[ "2017B" ][ 0 ][ 2 ] =  24.479;
    fiducialYLow_[ "2017B" ][ 0 ][ 2 ]  = -11.098;
    fiducialYHigh_[ "2017B" ][ 0 ][ 2 ] =   4.298;
    # Sector 56, RP 220
    fiducialXLow_[ "2017B" ][ 1 ][ 2 ]  =   2.422;
    fiducialXHigh_[ "2017B" ][ 1 ][ 2 ] =  24.620;
    fiducialYLow_[ "2017B" ][ 1 ][ 2 ]  = -10.698;
    fiducialYHigh_[ "2017B" ][ 1 ][ 2 ] =   4.698;

    # 2017C1
    # Sector 45, RP 220
    fiducialXLow_[ "2017C1" ][ 0 ][ 2 ]  =   1.860;
    fiducialXHigh_[ "2017C1" ][ 0 ][ 2 ] =  24.334;
    fiducialYLow_[ "2017C1" ][ 0 ][ 2 ]  = -11.098;
    fiducialYHigh_[ "2017C1" ][ 0 ][ 2 ] =   4.298;
    # Sector 56, RP 220
    fiducialXLow_[ "2017C1" ][ 1 ][ 2 ]  =   2.422;
    fiducialXHigh_[ "2017C1" ][ 1 ][ 2 ] =  24.620;
    fiducialYLow_[ "2017C1" ][ 1 ][ 2 ]  = -10.698;
    fiducialYHigh_[ "2017C1" ][ 1 ][ 2 ] =   4.698;

    # 2017E
    # Sector 45, RP 220
    fiducialXLow_[ "2017E" ][ 0 ][ 2 ]  =   1.995;
    fiducialXHigh_[ "2017E" ][ 0 ][ 2 ] =  24.479;
    fiducialYLow_[ "2017E" ][ 0 ][ 2 ]  = -10.098;
    fiducialYHigh_[ "2017E" ][ 0 ][ 2 ] =   4.998;
    # Sector 56, RP 220
    fiducialXLow_[ "2017E" ][ 1 ][ 2 ]  =  2.422;
    fiducialXHigh_[ "2017E" ][ 1 ][ 2 ] = 24.620;
    fiducialYLow_[ "2017E" ][ 1 ][ 2 ]  = -9.698;
    fiducialYHigh_[ "2017E" ][ 1 ][ 2 ] =  5.398;

    # 2017F1
    # Sector 45, RP 220
    fiducialXLow_[ "2017F1" ][ 0 ][ 2 ]  =   1.995;
    fiducialXHigh_[ "2017F1" ][ 0 ][ 2 ] =  24.479;
    fiducialYLow_[ "2017F1" ][ 0 ][ 2 ]  = -10.098;
    fiducialYHigh_[ "2017F1" ][ 0 ][ 2 ] =   4.998;
    # Sector 56, RP 220
    fiducialXLow_[ "2017F1" ][ 1 ][ 2 ]  =  2.422;
    fiducialXHigh_[ "2017F1" ][ 1 ][ 2 ] = 24.620;
    fiducialYLow_[ "2017F1" ][ 1 ][ 2 ]  = -9.698;
    fiducialYHigh_[ "2017F1" ][ 1 ][ 2 ] =  5.398;

    # 2018A
    # Sector 45, RP 210
    fiducialXLow_[ "2018A" ][ 0 ][ 0 ]  =   2.850;
    fiducialXHigh_[ "2018A" ][ 0 ][ 0 ] =  17.927;
    fiducialYLow_[ "2018A" ][ 0 ][ 0 ]  = -11.598;
    fiducialYHigh_[ "2018A" ][ 0 ][ 0 ] =   3.698;
    # Sector 45, RP 220
    fiducialXLow_[ "2018A" ][ 0 ][ 2 ]  =   2.421;
    fiducialXHigh_[ "2018A" ][ 0 ][ 2 ] =  24.620;
    fiducialYLow_[ "2018A" ][ 0 ][ 2 ]  = -10.898;
    fiducialYHigh_[ "2018A" ][ 0 ][ 2 ] =   4.398;
    # Sector 56, RP 210
    fiducialXLow_[ "2018A" ][ 1 ][ 0 ]  =   3.275;
    fiducialXHigh_[ "2018A" ][ 1 ][ 0 ] =  18.498;
    fiducialYLow_[ "2018A" ][ 1 ][ 0 ]  = -11.298;
    fiducialYHigh_[ "2018A" ][ 1 ][ 0 ] =   3.298;
    # Sector 56, RP 220
    fiducialXLow_[ "2018A" ][ 1 ][ 2 ]  =   2.421;
    fiducialXHigh_[ "2018A" ][ 1 ][ 2 ] =  20.045;
    fiducialYLow_[ "2018A" ][ 1 ][ 2 ]  = -10.398;
    fiducialYHigh_[ "2018A" ][ 1 ][ 2 ] =   5.098;

    # 2018B1
    # Sector 45, RP 210
    fiducialXLow_[ "2018B1" ][ 0 ][ 0 ]  =   2.850;
    fiducialXHigh_[ "2018B1" ][ 0 ][ 0 ] =  17.927;
    fiducialYLow_[ "2018B1" ][ 0 ][ 0 ]  = -11.598;
    fiducialYHigh_[ "2018B1" ][ 0 ][ 0 ] =   3.698;
    # Sector 45, RP 220
    fiducialXLow_[ "2018B1" ][ 0 ][ 2 ]  =   2.421;
    fiducialXHigh_[ "2018B1" ][ 0 ][ 2 ] =  24.620;
    fiducialYLow_[ "2018B1" ][ 0 ][ 2 ]  = -10.898;
    fiducialYHigh_[ "2018B1" ][ 0 ][ 2 ] =   4.198;
    # Sector 56, RP 210
    fiducialXLow_[ "2018B1" ][ 1 ][ 0 ]  =   3.275;
    fiducialXHigh_[ "2018B1" ][ 1 ][ 0 ] =  18.070;
    fiducialYLow_[ "2018B1" ][ 1 ][ 0 ]  = -11.198;
    fiducialYHigh_[ "2018B1" ][ 1 ][ 0 ] =   4.098;
    # Sector 56, RP 220
    fiducialXLow_[ "2018B1" ][ 1 ][ 2 ]  =   2.564;
    fiducialXHigh_[ "2018B1" ][ 1 ][ 2 ] =  20.045;
    fiducialYLow_[ "2018B1" ][ 1 ][ 2 ]  = -10.398;
    fiducialYHigh_[ "2018B1" ][ 1 ][ 2 ] =   5.098;

    # 2018B2
    # Sector 45, RP 210
    fiducialXLow_[ "2018B2" ][ 0 ][ 0 ]  =   2.564;
    fiducialXHigh_[ "2018B2" ][ 0 ][ 0 ] =  17.640;
    fiducialYLow_[ "2018B2" ][ 0 ][ 0 ]  = -11.598;
    fiducialYHigh_[ "2018B2" ][ 0 ][ 0 ] =   4.198;
    # Sector 45, RP 220
    fiducialXLow_[ "2018B2" ][ 0 ][ 2 ]  =   2.140;
    fiducialXHigh_[ "2018B2" ][ 0 ][ 2 ] =  24.479;
    fiducialYLow_[ "2018B2" ][ 0 ][ 2 ]  = -11.398;
    fiducialYHigh_[ "2018B2" ][ 0 ][ 2 ] =   3.798;
    # Sector 56, RP 210
    fiducialXLow_[ "2018B2" ][ 1 ][ 0 ]  =   3.275;
    fiducialXHigh_[ "2018B2" ][ 1 ][ 0 ] =  17.931;
    fiducialYLow_[ "2018B2" ][ 1 ][ 0 ]  = -10.498;
    fiducialYHigh_[ "2018B2" ][ 1 ][ 0 ] =   4.098;
    # Sector 56, RP 220
    fiducialXLow_[ "2018B2" ][ 1 ][ 2 ]  =   2.279;
    fiducialXHigh_[ "2018B2" ][ 1 ][ 2 ] =  24.760;
    fiducialYLow_[ "2018B2" ][ 1 ][ 2 ]  = -10.598;
    fiducialYHigh_[ "2018B2" ][ 1 ][ 2 ] =   4.498;

    # 2018C
    # Sector 45, RP 210
    fiducialXLow_[ "2018C" ][ 0 ][ 0 ]  =   2.564;
    fiducialXHigh_[ "2018C" ][ 0 ][ 0 ] =  17.930;
    fiducialYLow_[ "2018C" ][ 0 ][ 0 ]  = -11.098;
    fiducialYHigh_[ "2018C" ][ 0 ][ 0 ] =   4.198;
    # Sector 45, RP 220
    fiducialXLow_[ "2018C" ][ 0 ][ 2 ]  =   2.421;
    fiducialXHigh_[ "2018C" ][ 0 ][ 2 ] =  24.620;
    fiducialYLow_[ "2018C" ][ 0 ][ 2 ]  = -11.398;
    fiducialYHigh_[ "2018C" ][ 0 ][ 2 ] =   3.698;
    # Sector 56, RP 210
    fiducialXLow_[ "2018C" ][ 1 ][ 0 ]  =   3.275;
    fiducialXHigh_[ "2018C" ][ 1 ][ 0 ] =  17.931;
    fiducialYLow_[ "2018C" ][ 1 ][ 0 ]  = -10.498;
    fiducialYHigh_[ "2018C" ][ 1 ][ 0 ] =   4.698;
    # Sector 56, RP 220
    fiducialXLow_[ "2018C" ][ 1 ][ 2 ]  =   2.279;
    fiducialXHigh_[ "2018C" ][ 1 ][ 2 ] =  24.760;
    fiducialYLow_[ "2018C" ][ 1 ][ 2 ]  = -10.598;
    fiducialYHigh_[ "2018C" ][ 1 ][ 2 ] =   4.398;

    # 2018D1
    # Sector 45, RP 210
    fiducialXLow_[ "2018D1" ][ 0 ][ 0 ]  =   2.850;
    fiducialXHigh_[ "2018D1" ][ 0 ][ 0 ] =  17.931;
    fiducialYLow_[ "2018D1" ][ 0 ][ 0 ]  = -11.098;
    fiducialYHigh_[ "2018D1" ][ 0 ][ 0 ] =   4.098;
    # Sector 45, RP 220
    fiducialXLow_[ "2018D1" ][ 0 ][ 2 ]  =   2.421;
    fiducialXHigh_[ "2018D1" ][ 0 ][ 2 ] =  24.620;
    fiducialYLow_[ "2018D1" ][ 0 ][ 2 ]  = -11.398;
    fiducialYHigh_[ "2018D1" ][ 0 ][ 2 ] =   3.698;
    # Sector 56, RP 210
    fiducialXLow_[ "2018D1" ][ 1 ][ 0 ]  =   3.275;
    fiducialXHigh_[ "2018D1" ][ 1 ][ 0 ] =  17.931;
    fiducialYLow_[ "2018D1" ][ 1 ][ 0 ]  = -10.498;
    fiducialYHigh_[ "2018D1" ][ 1 ][ 0 ] =   4.698;
    # Sector 56, RP 220
    fiducialXLow_[ "2018D1" ][ 1 ][ 2 ]  =   2.279;
    fiducialXHigh_[ "2018D1" ][ 1 ][ 2 ] =  24.760;
    fiducialYLow_[ "2018D1" ][ 1 ][ 2 ]  = -10.598;
    fiducialYHigh_[ "2018D1" ][ 1 ][ 2 ] =   4.398;

    # 2018D2
    # Sector 45, RP 210
    fiducialXLow_[ "2018D2" ][ 0 ][ 0 ]  =   2.850;
    fiducialXHigh_[ "2018D2" ][ 0 ][ 0 ] =  17.931;
    fiducialYLow_[ "2018D2" ][ 0 ][ 0 ]  = -10.598;
    fiducialYHigh_[ "2018D2" ][ 0 ][ 0 ] =   4.498;
    # Sector 45, RP 220
    fiducialXLow_[ "2018D2" ][ 0 ][ 2 ]  =   2.421;
    fiducialXHigh_[ "2018D2" ][ 0 ][ 2 ] =  24.620;
    fiducialYLow_[ "2018D2" ][ 0 ][ 2 ]  = -11.698;
    fiducialYHigh_[ "2018D2" ][ 0 ][ 2 ] =   3.298;
    # Sector 56, RP 210
    fiducialXLow_[ "2018D2" ][ 1 ][ 0 ]  =  3.275;
    fiducialXHigh_[ "2018D2" ][ 1 ][ 0 ] = 17.931;
    fiducialYLow_[ "2018D2" ][ 1 ][ 0 ]  = -9.998;
    fiducialYHigh_[ "2018D2" ][ 1 ][ 0 ] =  4.698;
    # Sector 56, RP 220
    fiducialXLow_[ "2018D2" ][ 1 ][ 2 ]  =   2.279;
    fiducialXHigh_[ "2018D2" ][ 1 ][ 2 ] =  24.760;
    fiducialYLow_[ "2018D2" ][ 1 ][ 2 ]  = -10.598;
    fiducialYHigh_[ "2018D2" ][ 1 ][ 2 ] =   3.898;
      
    return (  fiducialXLow_, fiducialXHigh_, fiducialYLow_, fiducialYHigh_ )


# def fiducial_cuts_all():
# 
#     fiducialXLow_, fiducialXHigh_, fiducialYLow_, fiducialYHigh_ = fiducial_cuts()
#     print ( fiducialXLow_, fiducialXHigh_, fiducialYLow_, fiducialYHigh_ )
#     
#     # Per data period, arm=(0,1), station=(0,2)
#     fiducialXLow_all = {}
#     fiducialXHigh_all = {}
#     fiducialYLow_all = {}
#     fiducialYHigh_all = {}
#     for arm_ in (0,1):
#         fiducialXLow_all[ arm_ ] = {}
#         fiducialXLow_all[ arm_ ][ 2 ] = []
#         fiducialXHigh_all[ arm_ ] = {}
#         fiducialXHigh_all[ arm_ ][ 2 ] = []
#         fiducialYLow_all[ arm_ ] = {}
#         fiducialYLow_all[ arm_ ][ 2 ] = []
#         fiducialYHigh_all[ arm_ ] = {}
#         fiducialYHigh_all[ arm_ ][ 2 ] = []
# 
#     data_periods = [ "2017B", "2017C1", "2017E", "2017F1" ]
# 
#     for period_ in data_periods:
#         for arm_ in (0,1):
#             fiducialXLow_all[ arm_ ][ 2 ].append( fiducialXLow_[ period_ ][ arm_][ 2 ] )
#             fiducialXHigh_all[ arm_ ][ 2 ].append( fiducialXHigh_[ period_ ][ arm_][ 2 ] )
#             fiducialYLow_all[ arm_ ][ 2 ].append( fiducialYLow_[ period_ ][ arm_][ 2 ] )
#             fiducialYHigh_all[ arm_ ][ 2 ].append( fiducialYHigh_[ period_ ][ arm_][ 2 ] )
# 
#     for arm_ in (0,1):
#         fiducialXLow_all[ arm_ ][ 2 ] = np.max( fiducialXLow_all[ arm_ ][ 2 ] )
#         fiducialXHigh_all[ arm_ ][ 2 ] = np.min( fiducialXHigh_all[ arm_ ][ 2 ] )
#         fiducialYLow_all[ arm_ ][ 2 ] = np.max( fiducialYLow_all[ arm_ ][ 2 ] )
#         fiducialYHigh_all[ arm_ ][ 2 ] = np.min( fiducialYHigh_all[ arm_ ][ 2 ] )
#
#     print ( fiducialXLow_all, fiducialXHigh_all, fiducialYLow_all, fiducialYHigh_all )
#     
#     return ( fiducialXLow_all, fiducialXHigh_all, fiducialYLow_all, fiducialYHigh_all )


def fiducial_cuts_all( data_sample ):

    data_periods = None
    if data_sample == '2017':
        # data_periods = [ "2017B", "2017C1", "2017E", "2017F1" ]
        data_periods = [ "2017B", "2017C1", "2017C2", "2017D", "2017E", "2017F1", "2017F2", "2017F3" ]
    elif data_sample == '2018':
        data_periods = [ "2018A", "2018B1", "2018B2", "2018C", "2018D1", "2018D2" ]

    fiducialXLow_, fiducialXHigh_, fiducialYLow_, fiducialYHigh_ = fiducial_cuts()
    print ( fiducialXLow_, fiducialXHigh_, fiducialYLow_, fiducialYHigh_ )
    
    # Per data period, arm=(0,1), station=(0,2)
    fiducialXLow_all = {}
    fiducialXHigh_all = {}
    fiducialYLow_all = {}
    fiducialYHigh_all = {}
    for arm_ in (0,1):
        fiducialXLow_all[ arm_ ] = {}
        fiducialXLow_all[ arm_ ][ 2 ] = []
        fiducialXHigh_all[ arm_ ] = {}
        fiducialXHigh_all[ arm_ ][ 2 ] = []
        fiducialYLow_all[ arm_ ] = {}
        fiducialYLow_all[ arm_ ][ 2 ] = []
        fiducialYHigh_all[ arm_ ] = {}
        fiducialYHigh_all[ arm_ ][ 2 ] = []

    for period_ in data_periods:
        for arm_ in (0,1):
            fiducialXLow_all[ arm_ ][ 2 ].append( fiducialXLow_[ period_ ][ arm_][ 2 ] )
            fiducialXHigh_all[ arm_ ][ 2 ].append( fiducialXHigh_[ period_ ][ arm_][ 2 ] )
            fiducialYLow_all[ arm_ ][ 2 ].append( fiducialYLow_[ period_ ][ arm_][ 2 ] )
            fiducialYHigh_all[ arm_ ][ 2 ].append( fiducialYHigh_[ period_ ][ arm_][ 2 ] )

    for arm_ in (0,1):
        fiducialXLow_all[ arm_ ][ 2 ] = np.max( fiducialXLow_all[ arm_ ][ 2 ] )
        fiducialXHigh_all[ arm_ ][ 2 ] = np.min( fiducialXHigh_all[ arm_ ][ 2 ] )
        fiducialYLow_all[ arm_ ][ 2 ] = np.max( fiducialYLow_all[ arm_ ][ 2 ] )
        fiducialYHigh_all[ arm_ ][ 2 ] = np.min( fiducialYHigh_all[ arm_ ][ 2 ] )

    print ( fiducialXLow_all, fiducialXHigh_all, fiducialYLow_all, fiducialYHigh_all )
    
    return ( fiducialXLow_all, fiducialXHigh_all, fiducialYLow_all, fiducialYHigh_all )


# Per data period, arm=(0,1)
# Periods: "2016_preTS2", "2016_postTS2", "2017_preTS2", "2017_postTS2", "2018"
def aperture_parametrisation( period, arm, xangle, xi ):

    #https://github.com/cms-sw/cmssw/tree/916cb3d20213734a0465240720c8c8c392b92eac/Validation/CTPPS/python/simu_config

    if (period == "2016_preTS2"):
        if   (arm == 0): return 3.76296E-05+((xi<0.117122)*0.00712775+(xi>=0.117122)*0.0148651)*(xi-0.117122);
        elif (arm == 1): return 1.85954E-05+((xi<0.14324)*0.00475349+(xi>=0.14324)*0.00629514)*(xi-0.14324);
    elif (period == "2016_postTS2"):
        if   (arm == 0): return 6.10374E-05+((xi<0.113491)*0.00795942+(xi>=0.113491)*0.01935)*(xi-0.113491);
        elif (arm == 1): return (xi-0.110)/130.0;
    elif (period == "2017_preTS2"):
        if   (arm == 0): return -(8.71198E-07*xangle-0.000134726)+((xi<(0.000264704*xangle+0.081951))*-(4.32065E-05*xangle-0.0130746)+(xi>=(0.000264704*xangle+0.081951))*-(0.000183472*xangle-0.0395241))*(xi-(0.000264704*xangle+0.081951));
        elif (arm == 1): return 3.43116E-05+((xi<(0.000626936*xangle+0.061324))*0.00654394+(xi>=(0.000626936*xangle+0.061324))*-(0.000145164*xangle-0.0272919))*(xi-(0.000626936*xangle+0.061324));
    elif (period == "2017_postTS2"):
        if   (arm == 0): return -(8.92079E-07*xangle-0.000150214)+((xi<(0.000278622*xangle+0.0964383))*-(3.9541e-05*xangle-0.0115104)+(xi>=(0.000278622*xangle+0.0964383))*-(0.000108249*xangle-0.0249303))*(xi-(0.000278622*xangle+0.0964383));
        elif (arm == 1): return 4.56961E-05+((xi<(0.00075625*xangle+0.0643361))*-(3.01107e-05*xangle-0.00985126)+(xi>=(0.00075625*xangle+0.0643361))*-(8.95437e-05*xangle-0.0169474))*(xi-(0.00075625*xangle+0.0643361));
    elif (period == "2018"):
        if   (arm == 0): return -(8.44219E-07*xangle-0.000100957)+((xi<(0.000247185*xangle+0.101599))*-(1.40289E-05*xangle-0.00727237)+(xi>=(0.000247185*xangle+0.101599))*-(0.000107811*xangle-0.0261867))*(xi-(0.000247185*xangle+0.101599));
        elif (arm == 1): return -(-4.74758E-07*xangle+3.0881E-05)+((xi<(0.000727859*xangle+0.0722653))*-(2.43968E-05*xangle-0.0085461)+(xi>=(0.000727859*xangle+0.0722653))*-(7.19216E-05*xangle-0.0148267))*(xi-(0.000727859*xangle+0.0722653));
    else:
        return -999.


def check_aperture( period, arm, xangle, xi, theta_x ):
    return ( theta_x < -aperture_parametrisation( period, arm, xangle, xi ) )


def get_data( fileNames, selection=None, version="V1" ):

    if not version in ("V1", "V2"):
        print ( "Unsupported version: {}".format( version ) )
        exit()

    # df_columns_ = ['Run', 'LumiSection', 'EventNum', 'Slice', 'CrossingAngle',
    #                'MultiRP', 'Arm', 'RPId1', 'RPId2',
    #                'TrackX1', 'TrackY1', 'TrackX2', 'TrackY2',
    #                'TrackThX_SingleRP', 'TrackThY_SingleRP', 'Track1ThX_MultiRP', 'Track1ThY_MultiRP', 'Track2ThX_MultiRP', 'Track2ThY_MultiRP',
    #                'TrackPixShift_SingleRP', 'Track1PixShift_MultiRP', 'Track2PixShift_MultiRP',
    #                'Xi', 'T', 'ThX', 'ThY', 'Time',
    #                'nVertices', 'PrimVertexZ',
    #                'Muon0Pt', 'Muon0Eta', 'Muon0Phi', 'Muon0VtxZ',
    #                'Muon1Pt', 'Muon1Eta', 'Muon1Phi', 'Muon1VtxZ',
    #                'InvMass', 'ExtraPfCands', 'Acopl',
    #                'XiMuMuPlus', 'XiMuMuMinus']
    df_columns_types_ = {
        "Run": "int64", "LumiSection": "int64", "EventNum": "int64", "Slice": "int32",
        "MultiRP": "int32", "Arm": "int32", "RPId1": "int32", "RPId2": "int32",
        "TrackPixShift_SingleRP": "int32", "Track1PixShift_MultiRP": "int32", "Track2PixShift_MultiRP": "int32",
        "nVertices": "int32", "ExtraPfCands": "int32", "random": "int32"
        }
    
    df_list = None
    df_protons_multiRP_list = None
    df_protons_singleRP_list = None
    if version == "V1":
        df_list = []
    elif version == "V2":
        df_protons_multiRP_list = []
        df_protons_singleRP_list = []

    df_counts_list = []

    for file_ in fileNames:
        print ( file_ )
        with h5py.File( file_, 'r' ) as f:
            print ( list(f.keys()) )

            dset = None
            dset_protons_multiRP = None
            dset_protons_singleRP = None
            if version == "V1":
                dset = f['protons']
                print ( dset.shape )
                print ( dset[:,:] )
            elif version == "V2":
                dset_protons_multiRP = f['protons_multiRP']
                print ( dset_protons_multiRP.shape )
                print ( dset_protons_multiRP[:,:] )
                dset_protons_singleRP = f['protons_singleRP']
                print ( dset_protons_singleRP.shape )
                print ( dset_protons_singleRP[:,:] )

            dset_columns = f['columns']
            print ( dset_columns.shape )
            columns = list( dset_columns )
            print ( columns )
            columns_str = [ item.decode("utf-8") for item in columns ]
            print ( columns_str )

            dset_selections = f['selections']
            selections_ = [ item.decode("utf-8") for item in dset_selections ]
            print ( selections_ )

            dset_counts = f['event_counts']
            df_counts_list.append( pd.Series( dset_counts, index=selections_ ) )
            print ( df_counts_list[-1] )

            if "Run_mc" in columns_str:
                df_columns_types_.update( { "Run_mc": "int64" } )

            if "Run_rnd" in columns_str: 
                df_columns_types_.update( { "Run_rnd": "int64", "LumiSection_rnd": "int64", "EventNum_rnd": "int64" } )

            if version == "V1":
                chunk_size = 1000000
                entries = dset.shape[0]
                start_ = list( range( 0, entries, chunk_size ) )
                stop_ = start_[1:]
                stop_.append( entries )
                print ( start_ )
                print ( stop_ )
                for idx in range( len( start_ ) ):
                    print ( start_[idx], stop_[idx] )
                    #print ( dset[ start_[idx] : stop_[idx] ] )
                    # df_ = pd.DataFrame( dset[ start_[idx] : stop_[idx] ], columns=columns_str )
                    # df_ = df_[ df_columns_ ].astype( df_columns_types_ )
                    df_ = pd.DataFrame( dset[ start_[idx] : stop_[idx] ], columns=columns_str ).astype( df_columns_types_ )
                    
                    if selection:
                        #print ( len(df_) )
                        df_ = selection( df_ )
                        #print ( len(df_) )
    
                    df_list.append( df_ )
                    print ( df_list[-1].head() )
                    print ( len( df_list[-1] ) )
            elif version == "V2":
                chunk_size = 1000000
                entries_protons_multiRP = dset_protons_multiRP.shape[0]
                start_ = list( range( 0, entries_protons_multiRP, chunk_size ) )
                stop_ = start_[1:]
                stop_.append( entries_protons_multiRP )
                print ( start_ )
                print ( stop_ )
                for idx in range( len( start_ ) ):
                    print ( start_[idx], stop_[idx] )
                    # df_ = pd.DataFrame( dset_protons_multiRP[ start_[idx] : stop_[idx] ], columns=columns_str )
                    # df_ = df_[ df_columns_ ].astype( df_columns_types_ )
                    df_ = pd.DataFrame( dset_protons_multiRP[ start_[idx] : stop_[idx] ], columns=columns_str ).astype( df_columns_types_ )
                    
                    if selection:
                        #print ( len(df_) )
                        df_ = selection( df_ )
                        #print ( len(df_) )
    
                    df_protons_multiRP_list.append( df_ )
                    print ( df_protons_multiRP_list[-1].head() )
                    print ( len( df_protons_multiRP_list[-1] ) )

                entries_protons_singleRP = dset_protons_singleRP.shape[0]
                start_ = list( range( 0, entries_protons_singleRP, chunk_size ) )
                stop_ = start_[1:]
                stop_.append( entries_protons_singleRP )
                print ( start_ )
                print ( stop_ )
                for idx in range( len( start_ ) ):
                    print ( start_[idx], stop_[idx] )
                    # df_ = pd.DataFrame( dset_protons_singleRP[ start_[idx] : stop_[idx] ], columns=columns_str )
                    # df_ = df_[ df_columns_ ].astype( df_columns_types_ )
                    df_ = pd.DataFrame( dset_protons_singleRP[ start_[idx] : stop_[idx] ], columns=columns_str ).astype( df_columns_types_ )
                    
                    if selection:
                        #print ( len(df_) )
                        df_ = selection( df_ )
                        #print ( len(df_) )
    
                    df_protons_singleRP_list.append( df_ )
                    print ( df_protons_singleRP_list[-1].head() )
                    print ( len( df_protons_singleRP_list[-1] ) )

    df_counts = df_counts_list[0]
    for idx in range( 1, len( df_counts_list ) ):
        df_counts = df_counts.add( df_counts_list[idx] )
    print ( df_counts )

    if version == "V1":
        df = pd.concat( df_list )
        print ( df )
        return ( df_counts, df )
    elif version == "V2":
        df_protons_multiRP = pd.concat( df_protons_multiRP_list )
        print (df_protons_multiRP)
        df_protons_singleRP = pd.concat( df_protons_singleRP_list )
        print (df_protons_singleRP)    
        return ( df_counts, df_protons_multiRP, df_protons_singleRP )


def process_data( df, data_sample, lepton_type, proton_selection, min_mass=0., min_pt_1=-1, min_pt_2=-1, apply_fiducial=True, within_aperture=False, random_protons=False, mix_protons=False, runOnMC=False, select2protons=False, nprot_value=3 ):

    if runOnMC:
        print ( "Turning within_aperture OFF for MC." )
        within_aperture = False
        
    msk = ( df["InvMass"] >= min_mass )
    if min_pt_1 > 0: msk = msk & ( df["Muon0Pt"] >= min_pt_1 )
    if min_pt_2 > 0: msk = msk & ( df["Muon1Pt"] >= min_pt_2 )

    fiducialXLow_all = None
    fiducialXHigh_all = None
    fiducialYLow_all = None
    fiducialYHigh_all = None
    if apply_fiducial:
        fiducialXLow_all, fiducialXHigh_all, fiducialYLow_all, fiducialYHigh_all = fiducial_cuts_all( data_sample )
    
    track_angle_cut_ = 0.02
    
    run_str_ = "Run"
    if random_protons or mix_protons:
        run_str_ = "Run_rnd"
    elif runOnMC and not mix_protons:
        run_str_ = "Run_mc"

    xangle_str_ = "CrossingAngle"
    if random_protons or mix_protons:
        xangle_str_ = "CrossingAngle_rnd"

    df_run_ranges_ = None
    df_run_ranges_mixing_ = None
    if data_sample == '2017':
        df_run_ranges_ = df_run_ranges_2017
        df_run_ranges_mixing_ = df_run_ranges_mixing_2017
    elif data_sample == '2018':
        df_run_ranges_ = df_run_ranges_2018
        df_run_ranges_mixing_ = df_run_ranges_mixing_2018
    print ( df_run_ranges_ )
    print ( df_run_ranges_mixing_ )

    if "period" not in df.columns:
        df.loc[ :, "period" ] = np.nan
        for idx_ in range( df_run_ranges_.shape[0] ):
            msk_period_ = ( ( df.loc[ :, run_str_ ] >= df_run_ranges_.iloc[ idx_ ][ "min" ] ) & ( df.loc[ :, run_str_ ] <= df_run_ranges_.iloc[ idx_ ][ "max" ] ) )
            sum_period_ = np.sum( msk_period_ )
            if sum_period_ > 0:
                period_key_ = df_run_ranges_.index[ idx_ ]
                df.loc[ :, "period" ].loc[ msk_period_ ] = period_key_
                print ( "{}: {}".format( period_key_, sum_period_ ) )
        print ( df.loc[ :, "period" ] )

    msk1 = None
    msk2 = None
    if proton_selection == "SingleRP":
        # Single-RP in pixel stations
        msk1_arm = ( df["RPId1"] == 23 )
        msk2_arm = ( df["RPId1"] == 123 )
        df[ "XiMuMu" ] = np.nan
        df[ "XiMuMu" ].where( ~msk1_arm, df[ "XiMuMuPlus" ], inplace=True )
        df[ "XiMuMu" ].where( ~msk2_arm, df[ "XiMuMuMinus" ], inplace=True )
        
        msk_pixshift = ( df[ "TrackPixShift_SingleRP" ] == 0 )

        msk_fid = None
        if apply_fiducial:
            df[ "xlow" ] = np.nan
            df[ "xhigh" ] = np.nan
            df[ "ylow" ] = np.nan
            df[ "yhigh" ] = np.nan
            df[ "xlow" ].where( ~msk1_arm, fiducialXLow_all[ 0 ][ 2 ] , inplace=True )
            df[ "xhigh" ].where( ~msk1_arm, fiducialXHigh_all[ 0 ][ 2 ] , inplace=True )
            df[ "ylow" ].where( ~msk1_arm, fiducialYLow_all[ 0 ][ 2 ] , inplace=True )
            df[ "yhigh" ].where( ~msk1_arm, fiducialYHigh_all[ 0 ][ 2 ] , inplace=True )
            df[ "xlow" ].where( ~msk2_arm, fiducialXLow_all[ 1 ][ 2 ] , inplace=True )
            df[ "xhigh" ].where( ~msk2_arm, fiducialXHigh_all[ 1 ][ 2 ] , inplace=True )
            df[ "ylow" ].where( ~msk2_arm, fiducialYLow_all[ 1 ][ 2 ] , inplace=True )
            df[ "yhigh" ].where( ~msk2_arm, fiducialYHigh_all[ 1 ][ 2 ] , inplace=True )

            msk_fid = ( ( np.abs(df["TrackThX_SingleRP"]) <= track_angle_cut_ ) &
                        ( np.abs(df["TrackThY_SingleRP"]) <= track_angle_cut_ ) &
                        ( df["TrackX1"] >= df[ "xlow" ] ) &
                        ( df["TrackX1"] <= df[ "xhigh" ] ) &
                        ( df["TrackY1"] >= df[ "ylow" ] ) &
                        ( df["TrackY1"] <= df[ "yhigh" ] ) )

        #    msk1 = msk & msk_pixshift & msk_fid & ( df["MultiRP"] == 0 ) & msk1_arm
        #    msk2 = msk & msk_pixshift & msk_fid & ( df["MultiRP"] == 0 ) & msk2_arm
        #else:
        #    msk1 = msk & msk_pixshift & ( df["MultiRP"] == 0 ) & msk1_arm
        #    msk2 = msk & msk_pixshift & ( df["MultiRP"] == 0 ) & msk2_arm
        
        msk1 = msk & msk_pixshift & ( df["MultiRP"] == 0 ) & msk1_arm
        msk2 = msk & msk_pixshift & ( df["MultiRP"] == 0 ) & msk2_arm
        if msk_fid is not None:
            msk1 = msk1 & msk_fid
            msk2 = msk2 & msk_fid
            
    elif proton_selection == "MultiRP":
        # Multi-RP
        msk_multiRP = ( df["MultiRP"] == 1 )
        msk1_arm = ( df["Arm"] == 0 )
        msk2_arm = ( df["Arm"] == 1 )
        df[ "XiMuMu" ] = np.nan
        df[ "XiMuMu" ].where( ~msk1_arm, df[ "XiMuMuPlus" ], inplace=True )
        df[ "XiMuMu" ].where( ~msk2_arm, df[ "XiMuMuMinus" ], inplace=True )
        
        msk_pixshift = ( ( df[ "Track1PixShift_MultiRP" ] == 0 ) & ( df[ "Track2PixShift_MultiRP" ] == 0 ) )

        if within_aperture:
            # df.loc[ :, "period" ] = np.nan
            # for idx_ in range( df_run_ranges.shape[0] ):
            #     msk_period_ = ( ( df[ "Run" ] >= df_run_ranges.iloc[ idx_ ][ "min" ] ) & ( df[ "Run" ] <= df_run_ranges.iloc[ idx_ ][ "max" ] ) )
            #     sum_period_ = np.sum( msk_period_ )
            #     if sum_period_ > 0:
            #         period_key_ = df_run_ranges.index[ idx_ ]
            #         df.loc[ :, "period" ].loc[ msk_period_ ] = period_key_
            #         print ( "{}: {}".format( period_key_, sum_period_ ) )

            df.loc[ :, "within_aperture" ] = np.nan
            df.loc[ :, "within_aperture" ].loc[ msk_multiRP ] = df.loc[ msk_multiRP ].apply(
                    lambda row: check_aperture( aperture_period_map[ row["period"] ], row["Arm"], row["CrossingAngle"], row["Xi"], row["ThX"] ),
                    axis=1
                    )
            #df.loc[ :, "within_aperture" ].loc[ msk_multiRP ] = df.loc[ msk_multiRP ].apply(
            #        lambda row: print( aperture_period_map[ row["period"] ], row["Arm"], row["CrossingAngle"], row["Xi"], row["ThX"] ),
            #        axis=1
            #        )

        msk_fid = None
        if apply_fiducial:
            df[ "xlow" ] = np.nan
            df[ "xhigh" ] = np.nan
            df[ "ylow" ] = np.nan
            df[ "yhigh" ] = np.nan
            df[ "xlow" ].where( ~msk1_arm, fiducialXLow_all[ 0 ][ 2 ] , inplace=True )
            df[ "xhigh" ].where( ~msk1_arm, fiducialXHigh_all[ 0 ][ 2 ] , inplace=True )
            df[ "ylow" ].where( ~msk1_arm, fiducialYLow_all[ 0 ][ 2 ] , inplace=True )
            df[ "yhigh" ].where( ~msk1_arm, fiducialYHigh_all[ 0 ][ 2 ] , inplace=True )
            df[ "xlow" ].where( ~msk2_arm, fiducialXLow_all[ 1 ][ 2 ] , inplace=True )
            df[ "xhigh" ].where( ~msk2_arm, fiducialXHigh_all[ 1 ][ 2 ] , inplace=True )
            df[ "ylow" ].where( ~msk2_arm, fiducialYLow_all[ 1 ][ 2 ] , inplace=True )
            df[ "yhigh" ].where( ~msk2_arm, fiducialYHigh_all[ 1 ][ 2 ] , inplace=True )

            msk_fid = ( ( np.abs(df["Track2ThX_MultiRP"]) <= track_angle_cut_ ) &
                        ( np.abs(df["Track2ThY_MultiRP"]) <= track_angle_cut_ ) &
                        ( df["TrackX2"] >= df[ "xlow" ] ) &
                        ( df["TrackX2"] <= df[ "xhigh" ] ) &
                        ( df["TrackY2"] >= df[ "ylow" ] ) &
                        ( df["TrackY2"] <= df[ "yhigh" ] ) )

        #    msk1 = msk & msk_pixshift & msk_fid & ( df["MultiRP"] == 1 ) & msk1_arm
        #    msk2 = msk & msk_pixshift & msk_fid & ( df["MultiRP"] == 1 ) & msk2_arm
        #else:
        #    msk1 = msk & msk_pixshift & ( df["MultiRP"] == 1 ) & msk1_arm
        #    msk2 = msk & msk_pixshift & ( df["MultiRP"] == 1 ) & msk2_arm

        msk_aperture = None
        if within_aperture:
            msk_aperture = df.loc[ :, "within_aperture" ]
    
        msk1 = msk & msk_pixshift & ( df["MultiRP"] == 1 ) & msk1_arm
        msk2 = msk & msk_pixshift & ( df["MultiRP"] == 1 ) & msk2_arm
        if msk_fid is not None:
            msk1 = msk1 & msk_fid
            msk2 = msk2 & msk_fid
        if msk_aperture is not None:
            msk1 = msk1 & msk_aperture
            msk2 = msk2 & msk_aperture
            
    print ( "Number of rows: {}".format( len(df) ) )
    df = df[ msk1 | msk2 ]
    print ( "Number of rows selected: {}".format( len(df) ) )
    
    columns_eff_ = []

    if runOnMC and not mix_protons and proton_selection == "MultiRP":
        if data_sample == '2017': 
            # efficiencies_2017
            from proton_efficiency import efficiencies_2017, strict_zero_efficiencies, proton_efficiency_uncertainty
            strips_multitrack_efficiency, strips_sensor_efficiency, multiRP_efficiency, file_eff_strips, file_eff_multiRP = efficiencies_2017()
            sz_efficiencies = strict_zero_efficiencies()

            data_periods = [ "2017B", "2017C1", "2017C2", "2017D", "2017E", "2017F1", "2017F2", "2017F3" ]

            lumi_periods_ = None
            if lepton_type == 'muon':
                lumi_periods_ = lumi_periods_2017[ 'muon' ]
            elif lepton_type == 'electron':
                lumi_periods_ = lumi_periods_2017[ 'electron' ]

            proton_eff_unc_per_arm_ = proton_efficiency_uncertainty[ "2017" ]

            df.loc[ :, 'eff_proton_all_weighted' ] = 0.
            df.loc[ :, 'eff_multitrack_weighted' ] = 0.
            df.loc[ :, 'eff_strictzero_weighted' ] = 0.
            for period_ in data_periods:
                f_eff_strips_multitrack_ = lambda row: strips_multitrack_efficiency[ period_ ][ "45" if row["Arm"] == 0 else "56" ].GetBinContent( 1 )
    
                f_eff_strips_sensor_     = lambda row: strips_sensor_efficiency[ period_ ][ "45" if row["Arm"] == 0 else "56" ].GetBinContent(
                                                strips_sensor_efficiency[ period_ ][ "45" if row["Arm"] == 0 else "56" ].FindBin( row["TrackX2"], row["TrackY2"] )
                                                )
    
                f_eff_multiRP_           = lambda row: multiRP_efficiency[ period_ ][ "45" if row["Arm"] == 0 else "56" ].GetBinContent(
                                                multiRP_efficiency[ period_ ][ "45" if row["Arm"] == 0 else "56" ].FindBin( row["TrackX1"], row["TrackY1"] )
                                                )
    
                f_eff_strips_strictzero_ = lambda row: sz_efficiencies[ period_ ][ "45" if row["Arm"] == 0 else "56" ][ int( ( row["CrossingAngle"] // 10 ) * 10 ) ]

                f_eff_proton_all_        = lambda row: f_eff_strips_sensor_(row) * f_eff_multiRP_(row)

                # f_eff_all_               = lambda row: f_eff_strips_sensor_(row) * f_eff_multiRP_(row) * f_eff_strips_multitrack_(row)

                df.loc[ :, 'eff_proton_all_' + period_ ] = df[ ["Arm", "TrackX1", "TrackY1", "TrackX2", "TrackY2"] ].apply( f_eff_proton_all_, axis=1 )
                df.loc[ :, 'eff_proton_all_weighted' ]   = df.loc[ :, 'eff_proton_all_weighted' ] + lumi_periods_[ period_ ] * df.loc[ :, 'eff_proton_all_' + period_ ]
                df.loc[ :, 'eff_multitrack_' + period_ ] = df[ [ "Arm" ] ].apply( f_eff_strips_multitrack_, axis=1 )
                df.loc[ :, 'eff_multitrack_weighted' ]   = df.loc[ :, 'eff_multitrack_weighted' ] + lumi_periods_[ period_ ] * df.loc[ :, 'eff_multitrack_' + period_ ]
                df.loc[ :, 'eff_strictzero_' + period_ ] = df[ [ "Arm", "CrossingAngle" ] ].apply( f_eff_strips_strictzero_, axis=1 )
                df.loc[ :, 'eff_strictzero_weighted' ]   = df.loc[ :, 'eff_strictzero_weighted' ] + lumi_periods_[ period_ ] * df.loc[ :, 'eff_strictzero_' + period_ ]
                columns_eff_.append( 'eff_proton_all_' + period_ )        
                columns_eff_.append( 'eff_multitrack_' + period_ )        
                columns_eff_.append( 'eff_strictzero_' + period_ )        
            columns_eff_.append( 'eff_proton_all_weighted' ) 
            columns_eff_.append( 'eff_multitrack_weighted' ) 
            columns_eff_.append( 'eff_strictzero_weighted' )

            lumi_ = np.sum( list( lumi_periods_.values() ) )
            df.loc[ :, 'eff_proton_all_weighted' ] = df.loc[ :, 'eff_proton_all_weighted' ] / lumi_
            df.loc[ :, 'eff_multitrack_weighted' ] = df.loc[ :, 'eff_multitrack_weighted' ] / lumi_
            df.loc[ :, 'eff_strictzero_weighted' ] = df.loc[ :, 'eff_strictzero_weighted' ] / lumi_

            f_eff_strips_multitrack_ = lambda row: strips_multitrack_efficiency[ row["period"] ][ "45" if row["Arm"] == 0 else "56" ].GetBinContent( 1 )
    
            f_eff_strips_sensor_     = lambda row: strips_sensor_efficiency[ row["period"] ][ "45" if row["Arm"] == 0 else "56" ].GetBinContent(
                                            strips_sensor_efficiency[ row["period"] ][ "45" if row["Arm"] == 0 else "56" ].FindBin( row["TrackX2"], row["TrackY2"] )
                                            )
    
            f_eff_multiRP_           = lambda row: multiRP_efficiency[ row["period"] ][ "45" if row["Arm"] == 0 else "56" ].GetBinContent(
                                            multiRP_efficiency[ row["period"] ][ "45" if row["Arm"] == 0 else "56" ].FindBin( row["TrackX1"], row["TrackY1"] )
                                            )
    
            f_eff_strips_strictzero_ = lambda row: sz_efficiencies[ row["period"] ][ "45" if row["Arm"] == 0 else "56" ][ int( ( row["CrossingAngle"] // 10 ) * 10 ) ]

            f_eff_proton_all_        = lambda row: f_eff_strips_sensor_(row) * f_eff_multiRP_(row)
            df.loc[ :, 'eff_proton_all' ] = df[ [ "period", "Arm", "TrackX1", "TrackY1", "TrackX2", "TrackY2" ] ].apply( f_eff_proton_all_, axis=1 )
            df.loc[ :, 'eff_multitrack' ] = df[ [ "period", "Arm" ] ].apply( f_eff_strips_multitrack_, axis=1 )
            df.loc[ :, 'eff_strictzero' ] = df[ [ "period", "Arm", "CrossingAngle" ] ].apply( f_eff_strips_strictzero_, axis=1 )
            columns_eff_.append( 'eff_proton_all' ) 
            columns_eff_.append( 'eff_multitrack' ) 
            columns_eff_.append( 'eff_strictzero' )

            f_eff_proton_unc_ = lambda row: proton_eff_unc_per_arm_[ "45" if row["Arm"] == 0 else "56" ]
            df.loc[ :, 'eff_proton_unc' ] = df[ [ "Arm" ] ].apply( f_eff_proton_unc_, axis=1 )
            columns_eff_.append( 'eff_proton_unc' ) 
        elif data_sample == '2018': 
            # efficiencies_2018
            from proton_efficiency import efficiencies_2018, proton_efficiency_uncertainty
            sensor_near_efficiency, multiRP_efficiency, file_eff_rad_near, file_eff_multiRP = efficiencies_2018()

            data_periods = [ "2018A", "2018B1", "2018B2", "2018C", "2018D1", "2018D2" ]

            lumi_periods_ = None
            if lepton_type == 'muon':
                lumi_periods_ = lumi_periods_2018[ 'muon' ]
            elif lepton_type == 'electron':
                lumi_periods_ = lumi_periods_2018[ 'electron' ]

            proton_eff_unc_per_arm_ = proton_efficiency_uncertainty[ "2018" ]

            df.loc[ :, 'eff_proton_all_weighted' ] = 0.
            for period_ in data_periods:
                f_eff_sensor_near_       = lambda row: sensor_near_efficiency[ period_ ][ "45" if row["Arm"] == 0 else "56" ].GetBinContent(
                                                sensor_near_efficiency[ period_ ][ "45" if row["Arm"] == 0 else "56" ].FindBin( row["TrackX1"], row["TrackY1"] )
                                                )
    
                f_eff_multiRP_           = lambda row: multiRP_efficiency[ period_ ][ "45" if row["Arm"] == 0 else "56" ].GetBinContent(
                                                multiRP_efficiency[ period_ ][ "45" if row["Arm"] == 0 else "56" ].FindBin( row["TrackX1"], row["TrackY1"] )
                                                )

                f_eff_proton_all_        = lambda row: f_eff_sensor_near_(row) * f_eff_multiRP_(row)

                df.loc[ :, 'eff_proton_all_' + period_ ] = df[ ["Arm", "TrackX1", "TrackY1"] ].apply( f_eff_proton_all_, axis=1 )
                df.loc[ :, 'eff_proton_all_weighted' ]   = df.loc[ :, 'eff_proton_all_weighted' ] + lumi_periods_[ period_ ] * df.loc[ :, 'eff_proton_all_' + period_ ]
                columns_eff_.append( 'eff_proton_all_' + period_ )        
            columns_eff_.append( 'eff_proton_all_weighted' ) 

            lumi_ = np.sum( list( lumi_periods_.values() ) )
            df.loc[ :, 'eff_proton_all_weighted' ] = df.loc[ :, 'eff_proton_all_weighted' ] / lumi_

            f_eff_sensor_near_       = lambda row: sensor_near_efficiency[ row["period"] ][ "45" if row["Arm"] == 0 else "56" ].GetBinContent(
                                            sensor_near_efficiency[ row["period"] ][ "45" if row["Arm"] == 0 else "56" ].FindBin( row["TrackX1"], row["TrackY1"] )
                                            )
    
            f_eff_multiRP_           = lambda row: multiRP_efficiency[ row["period"] ][ "45" if row["Arm"] == 0 else "56" ].GetBinContent(
                                            multiRP_efficiency[ row["period"] ][ "45" if row["Arm"] == 0 else "56" ].FindBin( row["TrackX1"], row["TrackY1"] )
                                            )
    
            f_eff_proton_all_        = lambda row: f_eff_sensor_near_(row) * f_eff_multiRP_(row)
            df.loc[ :, 'eff_proton_all' ] = df[ [ "period", "Arm", "TrackX1", "TrackY1" ] ].apply( f_eff_proton_all_, axis=1 )
            columns_eff_.append( 'eff_proton_all' ) 

            f_eff_proton_unc_ = lambda row: proton_eff_unc_per_arm_[ "45" if row["Arm"] == 0 else "56" ]
            df.loc[ :, 'eff_proton_unc' ] = df[ [ "Arm" ] ].apply( f_eff_proton_unc_, axis=1 )
            columns_eff_.append( 'eff_proton_unc' ) 

    if runOnMC and mix_protons and proton_selection == "MultiRP":
        df.loc[ :, "eff_proton_all" ] = 1.0
        df.loc[ :, "eff_proton_all_weighted" ] = 1.0
        df.loc[ :, "eff_proton_unc" ] = 0.0
        if data_sample == '2017':
            df.loc[ :, "eff_multitrack" ] = 1.0
            df.loc[ :, "eff_strictzero" ] = 1.0
            df.loc[ :, "eff_multitrack_weighted" ] = 1.0
            df.loc[ :, "eff_strictzero_weighted" ] = 1.0

    if not runOnMC and proton_selection == "MultiRP":
        df.loc[ :, "eff_proton_all" ] = 1.0
        df.loc[ :, "eff_proton_all_weighted" ] = 1.0
        df.loc[ :, "eff_proton_unc" ] = 0.0
        if data_sample == '2017':
            df.loc[ :, "eff_multitrack" ] = 1.0
            df.loc[ :, "eff_strictzero" ] = 1.0
            df.loc[ :, "eff_multitrack_weighted" ] = 1.0
            df.loc[ :, "eff_strictzero_weighted" ] = 1.0

    use_hash_index_ = True
    index_vars_ = None
    if not use_hash_index_:
        index_vars_ = ['Run', 'LumiSection', 'EventNum', 'Slice']
    else:
        from pandas.util import hash_array
        arr_hash_id_ = hash_array( df.loc[ :, 'Muon0Pt' ].values  )
        df.loc[ :, "hash_id" ] = arr_hash_id_
        print ( df.loc[ :, "hash_id" ] )
        index_vars_ = ['Run', 'LumiSection', 'EventNum', 'hash_id', 'Slice']
    print ( index_vars_ )
    df_index = df.set_index( index_vars_ )

    columns_drop_ = [
        'MultiRP', 'Arm', 'RPId1', 'RPId2',
        'TrackX1', 'TrackY1', 'TrackX2', 'TrackY2',
        'TrackThX_SingleRP', 'TrackThY_SingleRP', 'Track1ThX_MultiRP', 'Track1ThY_MultiRP', 'Track2ThX_MultiRP', 'Track2ThY_MultiRP',
        'TrackPixShift_SingleRP', 'Track1PixShift_MultiRP', 'Track2PixShift_MultiRP',
        'Xi', 'T', 'ThX', 'ThY', 'Time'
        ]

    if runOnMC:
        columns_drop_.extend( columns_eff_ )
    print ( columns_drop_ )

    calculate_vars_pp_ = True
    df_events_ = None
    df_2protons_ = None
    df_ximax_ = None
    if proton_selection == "MultiRP":
        if calculate_vars_pp_:
            if select2protons:
                df_ximax_, df_events_, df_2protons_ = process_events( data_sample, df_index, select2protons=select2protons, runOnMC=runOnMC, columns_drop=columns_drop_, use_hash_index=use_hash_index_, nprot_value=nprot_value )
            else:
                df_ximax_ = process_events( data_sample, df_index, select2protons=select2protons, runOnMC=runOnMC, columns_drop=columns_drop_, use_hash_index=use_hash_index_, nprot_value=nprot_value )
        else:
            labels_xi_ = [ "_nom", "_p100", "_m100" ]
            if runOnMC:
                columns_drop_.extend( [ "Xi" + label_ for label_ in labels_xi_ ] )

            df_events_ = df_index.drop( columns=columns_drop_ )
            df_events_ = df_events_[ ~df_events_.index.duplicated(keep='first') ]
            print ( "Number of events: {}".format( df_events_.shape[0] ) )

    print ( df_index )

    if proton_selection == "SingleRP":
        return ( df_index )
    elif proton_selection == "MultiRP":
        if select2protons:
            return ( df_index, df_ximax_, df_events_, df_2protons_ )
        else:
            return ( df_index, df_ximax_ )


# def process_events( data_sample, df_protons_multiRP_index, select2protons = False, runOnMC=False, mix_protons=False, columns_drop=None, use_hash_index=False, nprot_value=3 ):
def process_events( data_sample, df_protons_multiRP_index, select2protons = False, runOnMC=False, columns_drop=None, use_hash_index=False, nprot_value=3 ):

    index_vars_ = None
    if not use_hash_index:
        index_vars_ = ['Run', 'LumiSection', 'EventNum', 'Slice']
    else:
        index_vars_ = ['Run', 'LumiSection', 'EventNum', 'hash_id', 'Slice']
    print ( index_vars_ )
   
    df_protons_multiRP_groupby_arm = df_protons_multiRP_index[ [ "Arm" ] ].groupby( index_vars_ )
    df_protons_multiRP_index['nprotons_arm0'] = df_protons_multiRP_groupby_arm[ "Arm" ].transform( lambda s_: ( np.sum( s_ == 0 ) ) )
    df_protons_multiRP_index['nprotons_arm1'] = df_protons_multiRP_groupby_arm[ "Arm" ].transform( lambda s_: ( np.sum( s_ == 1 ) ) )
    print( df_protons_multiRP_index['nprotons_arm0'] )
    print( df_protons_multiRP_index['nprotons_arm1'] )

    msk_nprotons = None
    if data_sample == '2017':
        msk_nprotons = ( df_protons_multiRP_index['nprotons_arm0'] == 1 ) & ( df_protons_multiRP_index['nprotons_arm1'] == 1 )
    elif data_sample == '2018':
        msk_nprotons = ( df_protons_multiRP_index['nprotons_arm0'] <= nprot_value ) & ( df_protons_multiRP_index['nprotons_arm1'] <= nprot_value )
    print ( msk_nprotons )
    df_protons_multiRP_index_nprotons = df_protons_multiRP_index.loc[ msk_nprotons ]

    groupby_vars_ = index_vars_.copy()
    groupby_vars_.append( 'Arm' )

    df_protons_multiRP_groupby_byarm_xi_max = df_protons_multiRP_index[ [ "Arm", "Xi" ] ].groupby( groupby_vars_ )
    msk_xi_max = df_protons_multiRP_groupby_byarm_xi_max[ "Xi" ].transform( lambda s_: ( s_ >= s_.max() ) )
    print ( msk_xi_max )
    df_protons_multiRP_index_xi_max = df_protons_multiRP_index.loc[ msk_xi_max ]

    var_list_ = None
    if data_sample == '2017':
        var_list_ = [ "Arm", "Xi", "eff_proton_all_weighted", "eff_multitrack_weighted", "eff_strictzero_weighted", "eff_proton_all", "eff_multitrack", "eff_strictzero", "eff_proton_unc" ]
    elif data_sample == '2018':
        var_list_ = [ "Arm", "Xi", "eff_proton_all_weighted", "eff_proton_all", "eff_proton_unc" ]

    # labels_xi_ = [ "_nom", "_p10", "_p30", "_p60", "_p100", "_m10", "_m30", "_m60", "_m100" ]
    # labels_xi_ = [ "_nom", "_p100", "_m100" ]
    # if runOnMC:
    #     var_list_.extend( [ "xi" + label_ for label_ in labels_xi_ ] )
    # 
    # if runOnMC:
    #     columns_drop.extend( [ "xi" + label_ for label_ in labels_xi_ ] )

    df_protons_multiRP_events = None
    df_protons_multiRP_index_2protons = None
    if select2protons: 
        df_protons_multiRP_groupby_arm = df_protons_multiRP_index_xi_max[ [ "Arm" ] ].groupby( index_vars_ )
        msk_2protons = df_protons_multiRP_groupby_arm[ "Arm" ].transform( lambda s_: ( np.sum( s_ == 0 ) == 1 ) & ( np.sum( s_ == 1 ) == 1 ) )
        print ( msk_2protons )
        df_protons_multiRP_index_2protons = df_protons_multiRP_index_xi_max.loc[ msk_2protons ]

        df_protons_multiRP_2protons_groupby = df_protons_multiRP_index_2protons[ var_list_ ].groupby( index_vars_ )

        df_protons_multiRP_events = df_protons_multiRP_index_2protons.drop( columns=columns_drop )
        df_protons_multiRP_events = df_protons_multiRP_events[ ~df_protons_multiRP_events.index.duplicated(keep='first') ]
        print ( "Number of events: {}".format( df_protons_multiRP_events.shape[0] ) )

        df_protons_multiRP_events.loc[ :, "MX" ] = df_protons_multiRP_2protons_groupby[ "Xi" ].agg(
            lambda s_: 13000. * np.sqrt( s_.iloc[0] * s_.iloc[1] )
            )
        print ( df_protons_multiRP_events.loc[ :, "MX" ] )
        df_protons_multiRP_events.loc[ :, "YX" ] = df_protons_multiRP_2protons_groupby[ ["Arm", "Xi"] ].apply(
            lambda df__: 0.5 * np.log( df__[ "Xi" ][ df__[ "Arm" ] == 0 ].iloc[0] / df__[ "Xi" ][ df__[ "Arm" ] == 1 ].iloc[0] )
            )
        print ( df_protons_multiRP_events.loc[ :, "YX" ] )
        df_protons_multiRP_events.loc[ :, "MX" + "_nom" ] = df_protons_multiRP_events.loc[ :, "MX" ]
        df_protons_multiRP_events.loc[ :, "YX" + "_nom" ] = df_protons_multiRP_events.loc[ :, "YX" ]

    # if runOnMC:
    #     # for label_ in [ "_jes_up", "_jes_dw" ]:
    #     # for label_ in [ "_jes_up", "_jes_dw", "_jer_up", "_jer_dw" ]:
    #     #     df_protons_multiRP_events.loc[ :, "R_MWW_MX" + label_ ] = ( df_protons_multiRP_events.loc[ :, "MWW" + label_ ] / df_protons_multiRP_events.loc[ :, "MX" + "_nom" ] ) 
    #     #      df_protons_multiRP_events.loc[ :, "Diff_YWW_YX" + label_ ] = ( df_protons_multiRP_events.loc[ :, "YWW" + label_ ] - df_protons_multiRP_events.loc[ :, "YX" + "_nom" ] )
    # 
    #     for label0_ in labels_xi_:
    #         for label1_ in labels_xi_:
    #             vars__ = [ "Arm", "Xi" + label0_ ] if label0_ == label1_  else [ "Arm", "Xi" + label0_, "Xi" + label1_ ]
    #             
    #             print ( "MX" + label0_ + label1_ )
    #             df_protons_multiRP_2protons_groupby_apply_MX_ = df_protons_multiRP_2protons_groupby[ vars__ ].apply(
    #                 lambda df__: 13000. * np.sqrt( df__[ "Xi" + label0_ ][ df__[ "Arm" ] == 0 ].iloc[0] * df__[ "Xi" + label1_ ][ df__[ "Arm" ] == 1 ].iloc[0] )
    #                 )
    #             df_protons_multiRP_events.loc[ :, "MX" + label0_ + label1_ ] = df_protons_multiRP_2protons_groupby_apply_MX_
    #             
    #             print ( "YX" + label0_ + label1_ )
    #             df_protons_multiRP_2protons_groupby_apply_YX_ = df_protons_multiRP_2protons_groupby[ vars__ ].apply(
    #                 lambda df__: 0.5 * np.log( df__[ "Xi" + label0_ ][ df__[ "Arm" ] == 0 ].iloc[0] / df__[ "Xi" + label1_ ][ df__[ "Arm" ] == 1 ].iloc[0] )
    #                 )
    #             df_protons_multiRP_events.loc[ :, "YX" + label0_ + label1_ ] = df_protons_multiRP_2protons_groupby_apply_YX_
    #             
    #             # print ( "R_MWW_MX" + label0_ + label1_ )
    #             # df_protons_multiRP_events.loc[ :, "R_MWW_MX" + label0_ + label1_ ] = ( df_protons_multiRP_events.loc[ :, "MWW" + "_nom" ] / df_protons_multiRP_events.loc[ :, "MX" + label0_ + label1_ ] )
    #             
    #             # print ( "Diff_YWW_YX" + label0_ + label1_ )
    #             # df_protons_multiRP_events.loc[ :, "Diff_YWW_YX" + label0_ + label1_ ] = ( df_protons_multiRP_events.loc[ :, "YWW" + "_nom" ] - df_protons_multiRP_events.loc[ :, "YX" + label0_ + label1_ ] )

        # if runOnMC and not mix_protons:
        if runOnMC:
            df_protons_multiRP_events.loc[ :, "eff_proton_all_weighted" ] = df_protons_multiRP_2protons_groupby[ "eff_proton_all_weighted" ].agg(
                lambda s_: ( s_.iloc[0] * s_.iloc[1] )
                )
            print ( df_protons_multiRP_events.loc[ :, "eff_proton_all_weighted" ] )
        
            if data_sample == '2017':
                df_protons_multiRP_events.loc[ :, "eff_multitrack_weighted" ] = df_protons_multiRP_2protons_groupby[ "eff_multitrack_weighted" ].agg(
                    lambda s_: ( s_.iloc[0] * s_.iloc[1] )
                    )
                print ( df_protons_multiRP_events.loc[ :, "eff_multitrack_weighted" ] )
                df_protons_multiRP_events.loc[ :, "eff_strictzero_weighted" ] = df_protons_multiRP_2protons_groupby[ "eff_strictzero_weighted" ].agg(
                    lambda s_: ( s_.iloc[0] * s_.iloc[1] )
                    )
                print ( df_protons_multiRP_events.loc[ :, "eff_strictzero_weighted" ] )

            df_protons_multiRP_events.loc[ :, "eff_proton_all" ] = df_protons_multiRP_2protons_groupby[ "eff_proton_all" ].agg(
                lambda s_: ( s_.iloc[0] * s_.iloc[1] )
                )
            print ( df_protons_multiRP_events.loc[ :, "eff_proton_all" ] )
        
            if data_sample == '2017':
                df_protons_multiRP_events.loc[ :, "eff_multitrack" ] = df_protons_multiRP_2protons_groupby[ "eff_multitrack" ].agg(
                    lambda s_: ( s_.iloc[0] * s_.iloc[1] )
                    )
                print ( df_protons_multiRP_events.loc[ :, "eff_multitrack" ] )
                df_protons_multiRP_events.loc[ :, "eff_strictzero" ] = df_protons_multiRP_2protons_groupby[ "eff_strictzero" ].agg(
                    lambda s_: ( s_.iloc[0] * s_.iloc[1] )
                    )
                print ( df_protons_multiRP_events.loc[ :, "eff_strictzero" ] )

            df_protons_multiRP_events.loc[ :, "eff_proton_unc" ] = df_protons_multiRP_2protons_groupby[ "eff_proton_unc" ].agg(
                lambda s_: np.sqrt( s_.iloc[0] ** 2 + s_.iloc[1] ** 2 )
                )

            print ( df_protons_multiRP_events.loc[ :, "eff_proton_unc" ] )
            df_protons_multiRP_events.loc[ :, "eff_proton_var_up" ] = ( 1. + df_protons_multiRP_events.loc[ :, "eff_proton_unc" ] )
            df_protons_multiRP_events.loc[ :, "eff_proton_var_dw" ] = ( 1. - df_protons_multiRP_events.loc[ :, "eff_proton_unc" ] )
            print ( df_protons_multiRP_events.loc[ :, "eff_proton_var_up" ] )
            print ( df_protons_multiRP_events.loc[ :, "eff_proton_var_dw" ] )


    if select2protons:
        return ( df_protons_multiRP_index_xi_max, df_protons_multiRP_events, df_protons_multiRP_index_2protons )
    else:
        return df_protons_multiRP_index_xi_max
