
import numpy as np
import pandas as pd
import h5py

run_ranges_periods = {}
run_ranges_periods[ "2017B" ]  = (297020,299329)
run_ranges_periods[ "2017C1" ] = (299337,300785)
run_ranges_periods[ "2017C2" ] = (300806,302029)
run_ranges_periods[ "2017D" ]  = (302030,303434)
run_ranges_periods[ "2017E" ]  = (303435,304826)
run_ranges_periods[ "2017F1" ] = (304911,305114)
run_ranges_periods[ "2017F2" ] = (305178,305902)
run_ranges_periods[ "2017F3" ] = (305965,306462)
df_run_ranges = pd.DataFrame( run_ranges_periods, index=("min","max") ).transpose()

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


def fiducial_cuts_all():

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

    data_periods = [ "2017B", "2017C1", "2017E", "2017F1" ]

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

    df_columns_ = ['Run', 'LumiSection', 'EventNum', 'Slice', 'CrossingAngle',
                   'MultiRP', 'Arm', 'RPId1', 'RPId2',
                   'TrackX1', 'TrackY1', 'TrackX2', 'TrackY2',
                   'TrackThX_SingleRP', 'TrackThY_SingleRP', 'Track1ThX_MultiRP', 'Track1ThY_MultiRP', 'Track2ThX_MultiRP', 'Track2ThY_MultiRP',
                   'TrackPixShift_SingleRP', 'Track1PixShift_MultiRP', 'Track2PixShift_MultiRP',
                   'Xi', 'T', 'ThX', 'ThY', 'Time',
                   'nVertices', 'PrimVertexZ',
                   'Muon0Pt', 'Muon0Eta', 'Muon0Phi', 'Muon0VtxZ',
                   'Muon1Pt', 'Muon1Eta', 'Muon1Phi', 'Muon1VtxZ',
                   'InvMass', 'ExtraPfCands', 'Acopl',
                   'XiMuMuPlus', 'XiMuMuMinus']
    df_columns_types_ = {
        "Run": "int64", "LumiSection": "int64", "EventNum": "int64", "Slice": "int32",
        "MultiRP": "int32", "Arm": "int32", "RPId1": "int32", "RPId2": "int32",
        "TrackPixShift_SingleRP": "int32", "Track1PixShift_MultiRP": "int32", "Track2PixShift_MultiRP": "int32",
        "nVertices": "int32", "ExtraPfCands": "int32"
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
                    df_ = pd.DataFrame( dset[ start_[idx] : stop_[idx] ], columns=columns_str )
                    df_ = df_[ df_columns_ ].astype( df_columns_types_ )
                    
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
                    df_ = pd.DataFrame( dset_protons_multiRP[ start_[idx] : stop_[idx] ], columns=columns_str )
                    df_ = df_[ df_columns_ ].astype( df_columns_types_ )
                    
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
                    df_ = pd.DataFrame( dset_protons_singleRP[ start_[idx] : stop_[idx] ], columns=columns_str )
                    df_ = df_[ df_columns_ ].astype( df_columns_types_ )
                    
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


def process_data( df, proton_selection, min_mass=0., min_pt_1=-1, min_pt_2=-1, apply_fiducial=True, within_aperture=False, random_protons=False, runOnMC=False ):

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
        fiducialXLow_all, fiducialXHigh_all, fiducialYLow_all, fiducialYHigh_all = fiducial_cuts_all()
    
    track_angle_cut_ = 0.02
    
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
            df.loc[ :, "period" ] = np.nan
            for idx_ in range( df_run_ranges.shape[0] ):
                msk_period_ = ( ( df[ "Run" ] >= df_run_ranges.iloc[ idx_ ][ "min" ] ) & ( df[ "Run" ] <= df_run_ranges.iloc[ idx_ ][ "max" ] ) )
                sum_period_ = np.sum( msk_period_ )
                if sum_period_ > 0:
                    period_key_ = df_run_ranges.index[ idx_ ]
                    df.loc[ :, "period" ].loc[ msk_period_ ] = period_key_
                    print ( "{}: {}".format( period_key_, sum_period_ ) )

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
    
    return ( df )  
