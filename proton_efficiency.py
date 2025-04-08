
import ROOT

# Efficiency uncertanties
proton_efficiency_uncertainty = {
    '2016': { '45': 0.10,   '56': 0.10   },
    '2017': { '45': 0.0265, '56': 0.0265 },
    '2018': { '45': 0.0206, '56': 0.0221 }
}

# Strict zero efficiencies
def strict_zero_efficiencies():

    data_periods_ = [ "2017B", "2017C1", "2017C2", "2017D", "2017E", "2017F1", "2017F2", "2017F3" ]
    data_periods_.extend( [ "2017C", "2017E1", "2017E2", "2017F" ] )
    sz_efficiencies = {}

    for period_ in data_periods_:
        sz_efficiencies[ period_ ] = {}
        for sector_ in [ "45", "56" ]:
            sz_efficiencies[ period_ ][ "45" ] = {}
            sz_efficiencies[ period_ ][ "56" ] = {}

    xangle_values_ = [ 120, 130, 140, 150 ]
    xangle_extra_values_ = [ 100, 110, 160, 170 ]

    sector_ = "45"
    xangle_ = 120
#     if xangle == 120:
#         if period == "B":  prob = 0.8605
#         if period == "C":  prob = 0.8687
#         if period == "D":  prob = 0.8665
#         if period == "E1": prob = 1.0000*0
#         if period == "E2": prob = 0.6945
#         if period == "F":  prob = 0.6803
    sz_efficiencies[ "2017B" ][ sector_ ][ xangle_ ]  = 0.8605
    sz_efficiencies[ "2017C" ][ sector_ ][ xangle_ ]  = 0.8687
    sz_efficiencies[ "2017D" ][ sector_ ][ xangle_ ]  = 0.8665
    sz_efficiencies[ "2017E1" ][ sector_ ][ xangle_ ] = 0.
    sz_efficiencies[ "2017E2" ][ sector_ ][ xangle_ ] = 0.6945
    sz_efficiencies[ "2017F" ][ sector_ ][ xangle_ ]  = 0.6803
    sz_efficiencies[ "2017C1" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017C" ][ sector_ ][ xangle_ ]
    sz_efficiencies[ "2017C2" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017C" ][ sector_ ][ xangle_ ]
    sz_efficiencies[ "2017E" ][ sector_ ][ xangle_ ]  = sz_efficiencies[ "2017E2" ][ sector_ ][ xangle_ ]
    sz_efficiencies[ "2017F1" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017F" ][ sector_ ][ xangle_ ]
    sz_efficiencies[ "2017F2" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017F" ][ sector_ ][ xangle_ ]
    sz_efficiencies[ "2017F3" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017F" ][ sector_ ][ xangle_ ]
    xangle_ = 130
#     if xangle == 130:
#         if period == "B":  prob = 0.7749
#         if period == "C":  prob = 0.7888
#         if period == "D":  prob = 0.7920
#         if period == "E1": prob = 1.0000*0
#         if period == "E2": prob = 0.4680
#         if period == "F":  prob = 0.4667
    sz_efficiencies[ "2017B" ][ sector_ ][ xangle_ ]  = 0.7749
    sz_efficiencies[ "2017C" ][ sector_ ][ xangle_ ]  = 0.7888
    sz_efficiencies[ "2017D" ][ sector_ ][ xangle_ ]  = 0.7920
    sz_efficiencies[ "2017E1" ][ sector_ ][ xangle_ ] = 0.
    sz_efficiencies[ "2017E2" ][ sector_ ][ xangle_ ] = 0.4680
    sz_efficiencies[ "2017F" ][ sector_ ][ xangle_ ]  = 0.4667
    sz_efficiencies[ "2017C1" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017C" ][ sector_ ][ xangle_ ]
    sz_efficiencies[ "2017C2" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017C" ][ sector_ ][ xangle_ ]
    sz_efficiencies[ "2017E" ][ sector_ ][ xangle_ ]  = sz_efficiencies[ "2017E2" ][ sector_ ][ xangle_ ]
    sz_efficiencies[ "2017F1" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017F" ][ sector_ ][ xangle_ ]
    sz_efficiencies[ "2017F2" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017F" ][ sector_ ][ xangle_ ]
    sz_efficiencies[ "2017F3" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017F" ][ sector_ ][ xangle_ ]
    xangle_ = 140
#     if xangle == 140:
#         if period == "B":  prob = 0.7137
#         if period == "C":  prob = 0.7181
#         if period == "D":  prob = 0.7353
#         if period == "E1": prob = 1.0000*0
#         if period == "E2": prob = 0.3556
#         if period == "F":  prob = 0.3878
    sz_efficiencies[ "2017B" ][ sector_ ][ xangle_ ]  = 0.7137
    sz_efficiencies[ "2017C" ][ sector_ ][ xangle_ ]  = 0.7181
    sz_efficiencies[ "2017D" ][ sector_ ][ xangle_ ]  = 0.7353
    sz_efficiencies[ "2017E1" ][ sector_ ][ xangle_ ] = 0.
    sz_efficiencies[ "2017E2" ][ sector_ ][ xangle_ ] = 0.3556
    sz_efficiencies[ "2017F" ][ sector_ ][ xangle_ ]  = 0.3878
    sz_efficiencies[ "2017C1" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017C" ][ sector_ ][ xangle_ ]
    sz_efficiencies[ "2017C2" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017C" ][ sector_ ][ xangle_ ]
    sz_efficiencies[ "2017E" ][ sector_ ][ xangle_ ]  = sz_efficiencies[ "2017E2" ][ sector_ ][ xangle_ ]
    sz_efficiencies[ "2017F1" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017F" ][ sector_ ][ xangle_ ]
    sz_efficiencies[ "2017F2" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017F" ][ sector_ ][ xangle_ ]
    sz_efficiencies[ "2017F3" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017F" ][ sector_ ][ xangle_ ]
    xangle_ = 150
#     if xangle == 150:
#         if period == "B":  prob = 0.6359
#         if period == "C":  prob = 0.6510
#         if period == "D":  prob = 0.6713
#         if period == "E1": prob = 1.0000*0
#         if period == "E2": prob = 0.3493
#         if period == "F":  prob = 0.3593
    sz_efficiencies[ "2017B" ][ sector_ ][ xangle_ ]  = 0.6359
    sz_efficiencies[ "2017C" ][ sector_ ][ xangle_ ]  = 0.6510
    sz_efficiencies[ "2017D" ][ sector_ ][ xangle_ ]  = 0.6713
    sz_efficiencies[ "2017E1" ][ sector_ ][ xangle_ ] = 1.0000
    sz_efficiencies[ "2017E2" ][ sector_ ][ xangle_ ] = 0.3493
    sz_efficiencies[ "2017F" ][ sector_ ][ xangle_ ]  = 0.3593
    sz_efficiencies[ "2017C1" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017C" ][ sector_ ][ xangle_ ]
    sz_efficiencies[ "2017C2" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017C" ][ sector_ ][ xangle_ ]
    sz_efficiencies[ "2017E" ][ sector_ ][ xangle_ ]  = sz_efficiencies[ "2017E2" ][ sector_ ][ xangle_ ]
    sz_efficiencies[ "2017F1" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017F" ][ sector_ ][ xangle_ ]
    sz_efficiencies[ "2017F2" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017F" ][ sector_ ][ xangle_ ]
    sz_efficiencies[ "2017F3" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017F" ][ sector_ ][ xangle_ ]

    sector_ = "56"
    xangle_ = 120
#     if xangle == 120:
#         if period == "B":  prob = 0.8412*prob
#         if period == "C":  prob = 0.8370*prob
#         if period == "D":  prob = 0.8273*prob
#         if period == "E1": prob = 0.6572*prob
#         if period == "E2": prob = 0.6307*prob
#         if period == "F":  prob = 0.6053*prob
    sz_efficiencies[ "2017B" ][ sector_ ][ xangle_ ]  = 0.8412
    sz_efficiencies[ "2017C" ][ sector_ ][ xangle_ ]  = 0.8370
    sz_efficiencies[ "2017D" ][ sector_ ][ xangle_ ]  = 0.8273
    sz_efficiencies[ "2017E1" ][ sector_ ][ xangle_ ] = 0.6572
    sz_efficiencies[ "2017E2" ][ sector_ ][ xangle_ ] = 0.6307
    sz_efficiencies[ "2017F" ][ sector_ ][ xangle_ ]  = 0.6053
    sz_efficiencies[ "2017C1" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017C" ][ sector_ ][ xangle_ ]
    sz_efficiencies[ "2017C2" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017C" ][ sector_ ][ xangle_ ]
    sz_efficiencies[ "2017E" ][ sector_ ][ xangle_ ]  = sz_efficiencies[ "2017E2" ][ sector_ ][ xangle_ ]
    sz_efficiencies[ "2017F1" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017F" ][ sector_ ][ xangle_ ]
    sz_efficiencies[ "2017F2" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017F" ][ sector_ ][ xangle_ ]
    sz_efficiencies[ "2017F3" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017F" ][ sector_ ][ xangle_ ]
    xangle_ = 130
#     if xangle == 130:
#         if period == "B":  prob = 0.7409*prob
#         if period == "C":  prob = 0.7400*prob
#         if period == "D":  prob = 0.7376*prob
#         if period == "E1": prob = 0.4822*prob
#         if period == "E2": prob = 0.3976*prob
#         if period == "F":  prob = 0.3813*prob
    sz_efficiencies[ "2017B" ][ sector_ ][ xangle_ ]  = 0.7409
    sz_efficiencies[ "2017C" ][ sector_ ][ xangle_ ]  = 0.7400
    sz_efficiencies[ "2017D" ][ sector_ ][ xangle_ ]  = 0.7376
    sz_efficiencies[ "2017E1" ][ sector_ ][ xangle_ ] = 0.4822
    sz_efficiencies[ "2017E2" ][ sector_ ][ xangle_ ] = 0.3976
    sz_efficiencies[ "2017F" ][ sector_ ][ xangle_ ]  = 0.3813
    sz_efficiencies[ "2017C1" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017C" ][ sector_ ][ xangle_ ]
    sz_efficiencies[ "2017C2" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017C" ][ sector_ ][ xangle_ ]
    sz_efficiencies[ "2017E" ][ sector_ ][ xangle_ ]  = sz_efficiencies[ "2017E2" ][ sector_ ][ xangle_ ]
    sz_efficiencies[ "2017F1" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017F" ][ sector_ ][ xangle_ ]
    sz_efficiencies[ "2017F2" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017F" ][ sector_ ][ xangle_ ]
    sz_efficiencies[ "2017F3" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017F" ][ sector_ ][ xangle_ ]
    xangle_ = 140
#     if xangle == 140:
#         if period == "B":  prob = 0.6752*prob
#         if period == "C":  prob = 0.6607*prob
#         if period == "D":  prob = 0.6729*prob
#         if period == "E1": prob = 0.3791*prob
#         if period == "E2": prob = 0.2982*prob
#         if period == "F":  prob = 0.3100*prob
    sz_efficiencies[ "2017B" ][ sector_ ][ xangle_ ]  = 0.6752
    sz_efficiencies[ "2017C" ][ sector_ ][ xangle_ ]  = 0.6607
    sz_efficiencies[ "2017D" ][ sector_ ][ xangle_ ]  = 0.6729
    sz_efficiencies[ "2017E1" ][ sector_ ][ xangle_ ] = 0.3791
    sz_efficiencies[ "2017E2" ][ sector_ ][ xangle_ ] = 0.2982
    sz_efficiencies[ "2017F" ][ sector_ ][ xangle_ ]  = 0.3100
    sz_efficiencies[ "2017C1" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017C" ][ sector_ ][ xangle_ ]
    sz_efficiencies[ "2017C2" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017C" ][ sector_ ][ xangle_ ]
    sz_efficiencies[ "2017E" ][ sector_ ][ xangle_ ]  = sz_efficiencies[ "2017E2" ][ sector_ ][ xangle_ ]
    sz_efficiencies[ "2017F1" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017F" ][ sector_ ][ xangle_ ]
    sz_efficiencies[ "2017F2" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017F" ][ sector_ ][ xangle_ ]
    sz_efficiencies[ "2017F3" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017F" ][ sector_ ][ xangle_ ]
    xangle_ = 150
#     if xangle == 150:
#         if period == "B":  prob = 0.5948*prob
#         if period == "C":  prob = 0.5896*prob
#         if period == "D":  prob = 0.6010*prob
#         if period == "E1": prob = 0.3467*prob
#         if period == "E2": prob = 0.2904*prob
#         if period == "F":  prob = 0.2862*prob
    sz_efficiencies[ "2017B" ][ sector_ ][ xangle_ ]  = 0.5948
    sz_efficiencies[ "2017C" ][ sector_ ][ xangle_ ]  = 0.5896
    sz_efficiencies[ "2017D" ][ sector_ ][ xangle_ ]  = 0.6010
    sz_efficiencies[ "2017E1" ][ sector_ ][ xangle_ ] = 0.3467
    sz_efficiencies[ "2017E2" ][ sector_ ][ xangle_ ] = 0.2904
    sz_efficiencies[ "2017F" ][ sector_ ][ xangle_ ]  = 0.2862
    sz_efficiencies[ "2017C1" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017C" ][ sector_ ][ xangle_ ]
    sz_efficiencies[ "2017C2" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017C" ][ sector_ ][ xangle_ ]
    sz_efficiencies[ "2017E" ][ sector_ ][ xangle_ ]  = sz_efficiencies[ "2017E2" ][ sector_ ][ xangle_ ]
    sz_efficiencies[ "2017F1" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017F" ][ sector_ ][ xangle_ ]
    sz_efficiencies[ "2017F2" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017F" ][ sector_ ][ xangle_ ]
    sz_efficiencies[ "2017F3" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017F" ][ sector_ ][ xangle_ ]

    for xangle_ in xangle_extra_values_:
        for sector_ in [ "45", "56" ]:
            xangle_ref_ = 0.
            if xangle_ < xangle_values_[ 0 ]: xangle_ref_ = xangle_values_[ 0 ]
            elif xangle_ > xangle_values_[ -1 ]: xangle_ref_ = xangle_values_[ -1 ]
            sz_efficiencies[ "2017B" ][ sector_ ][ xangle_ ]  = sz_efficiencies[ "2017B" ][ sector_ ][ xangle_ref_ ]
            sz_efficiencies[ "2017C" ][ sector_ ][ xangle_ ]  = sz_efficiencies[ "2017C" ][ sector_ ][ xangle_ref_ ]
            sz_efficiencies[ "2017D" ][ sector_ ][ xangle_ ]  = sz_efficiencies[ "2017D" ][ sector_ ][ xangle_ref_ ]
            sz_efficiencies[ "2017E1" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017E1" ][ sector_ ][ xangle_ref_ ]
            sz_efficiencies[ "2017E2" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017E2" ][ sector_ ][ xangle_ref_ ]
            sz_efficiencies[ "2017F" ][ sector_ ][ xangle_ ]  = sz_efficiencies[ "2017F" ][ sector_ ][ xangle_ref_ ]
            sz_efficiencies[ "2017C1" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017C" ][ sector_ ][ xangle_ ]
            sz_efficiencies[ "2017C2" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017C" ][ sector_ ][ xangle_ ]
            sz_efficiencies[ "2017E" ][ sector_ ][ xangle_ ]  = sz_efficiencies[ "2017E2" ][ sector_ ][ xangle_ ]
            sz_efficiencies[ "2017F1" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017F" ][ sector_ ][ xangle_ ]
            sz_efficiencies[ "2017F2" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017F" ][ sector_ ][ xangle_ ]
            sz_efficiencies[ "2017F3" ][ sector_ ][ xangle_ ] = sz_efficiencies[ "2017F" ][ sector_ ][ xangle_ ]

    print ( sz_efficiencies )

    return sz_efficiencies

def efficiencies_2017():

    file_eff_strips = ROOT.TFile.Open( "./efficiencies/Strips/StripsTracking/PreliminaryEfficiencies_July132020_1D2DMultiTrack.root", "READ" )
    file_eff_multiRP = ROOT.TFile.Open( "./efficiencies/Pixel/RPixTracking/pixelEfficiencies_multiRP.root", "READ" )
    
    data_periods = [ "2017B", "2017C1", "2017C2", "2017D", "2017E", "2017F1", "2017F2", "2017F3" ]
    years = [ period[:4] for period in data_periods ]
    
    strips_multitrack_efficiency = {}
    strips_sensor_efficiency = {}
    multiRP_efficiency = {}
    
    # Retrieve histograms from files and save them in dictionaries for future usage
    for idx_, period_ in enumerate( data_periods ):
        strips_multitrack_efficiency[ period_ ] = {}
        strips_sensor_efficiency[ period_ ] = {}
        multiRP_efficiency[ period_ ] = {}
        year = years[ idx_ ]
        for sector in ["45","56"]:
            rp_number_strips = "3" if sector == "45" else "103"
    
            strips_multitrack_efficiency[ period_ ][ sector ] = file_eff_strips.Get(
                "Strips/" + year + "/" + period_ + "/h" + sector + "multitrackeff_" + period_ + "_avg_RP" + rp_number_strips
                )
    
            strips_sensor_efficiency[ period_ ][ sector ] = file_eff_strips.Get(
                "Strips/" + year + "/" + period_ + "/h" + sector + "_" + period_ + "_all_2D"
                )
            
            multiRP_efficiency[ period_ ][ sector ] = file_eff_multiRP.Get(
                "Pixel/" + year + "/" + period_ + "/h" + sector + "_220_" + period_ + "_all_2D"
                )
    print ( strips_multitrack_efficiency )
    print ( strips_sensor_efficiency )
    print ( multiRP_efficiency )

    return ( strips_multitrack_efficiency, strips_sensor_efficiency, multiRP_efficiency, file_eff_strips, file_eff_multiRP )

def efficiencies_2018():

    file_eff_radiation = ROOT.TFile.Open( "./efficiencies/Pixel/RPixTracking/pixelEfficiencies_radiation_reMiniAOD.root", "READ" )
    file_eff_multiRP = ROOT.TFile.Open( "./efficiencies/Pixel/RPixTracking/pixelEfficiencies_multiRP_reMiniAOD.root", "READ" )
    
    data_periods = [ "2018A", "2018B1", "2018B2", "2018C", "2018D1", "2018D2" ]
    years = [ period[:4] for period in data_periods ]
    
    sensor_near_efficiency = {}
    multiRP_efficiency = {}
    
    # Retrieve histograms from files and save them in dictionaries for future usage
    for idx_, period_ in enumerate( data_periods ):
        sensor_near_efficiency[ period_ ] = {}
        multiRP_efficiency[ period_ ] = {}
        year_ = years[ idx_ ]
        for sector_ in ["45","56"]:
            station_ = "210"
            sensor_near_efficiency[ period_ ][ sector_ ] = file_eff_radiation.Get(
                "Pixel/" + year_ + "/" + period_ + "/h" + sector_ + "_" + station_ + "_" + period_ + "_all_2D"
                )
            
            station_ = "220"
            multiRP_efficiency[ period_ ][ sector_ ] = file_eff_multiRP.Get(
                "Pixel/" + year_ + "/" + period_ + "/h" + sector_ + "_" + station_ + "_" + period_ + "_all_2D"
                )
    print ( sensor_near_efficiency )
    print ( multiRP_efficiency )

    return ( sensor_near_efficiency, multiRP_efficiency, file_eff_radiation, file_eff_multiRP )
