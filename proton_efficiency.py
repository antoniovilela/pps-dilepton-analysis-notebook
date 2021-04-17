
import ROOT

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
