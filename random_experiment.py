import numpy as np
import pandas as pd
import h5py
#import ROOT

from processing import aperture_period_map

def get_reco_characteristics( file, period, arm=None, rp=None ):
    
    print ( file )
    print ( period )
    print ( arm )
    print ( rp )
    
    algo_str_ = None
    str_ = None
    if arm is None and rp is not None:
        algo_str_ = "single rp"
        str_ = "{}/{}-{}/xi/".format( period, algo_str_, rp)
    elif arm is not None and rp is None:
        algo_str_ = "multi rp"
        str_ = "{}/{}-{}/xi/".format( period, algo_str_, arm)
    print ( str_ )
    
    g_bias_vs_xi_ = file.Get( str_ + "g_bias_vs_xi" )
    g_resolution_vs_xi_ = file.Get( str_ + "g_resolution_vs_xi" )
    g_systematics_vs_xi_ = file.Get( str_ + "g_systematics_vs_xi" )

    bias_X = np.array( list( g_bias_vs_xi_.GetX() ) )
    bias_Y = np.array( list( g_bias_vs_xi_.GetY() ) )
    resolution_X = np.array( list( g_resolution_vs_xi_.GetX() ) )
    resolution_Y = np.array( list( g_resolution_vs_xi_.GetY() ) )
    systematics_X = np.array( list( g_systematics_vs_xi_.GetX() ) )
    systematics_Y = np.array( list( g_systematics_vs_xi_.GetY() ) )
    
    return ( (bias_X, bias_Y), (resolution_X, resolution_Y), (systematics_X, systematics_Y) )

#def get_systematics_vs_xi_ROOT( data_periods, fileName="reco_characteristics/reco_characteristics_version1.root" ):
#    
#    file_systematics_Xi = ROOT.TFile( fileName, "READ" )
#    
#    aperture_systematics_Xi_period_map = aperture_period_map
#    
#    systematics_Xi_X = {}
#    systematics_Xi_Y = {}
#    for idx_, period_ in enumerate( data_periods ):
#        systematics_Xi_X[ period_ ] = {}
#        systematics_Xi_Y[ period_ ] = {}
#        for arm_ in (0,1):
#            (bias_X_, bias_Y_), (resolution_X_, resolution_Y_), (systematics_Xi_X_, systematics_Xi_Y_) = get_reco_characteristics( file_systematics_Xi, period=aperture_systematics_Xi_period_map[ period_ ], arm=arm_ )
#            systematics_Xi_X[ period_ ][ arm_ ] = systematics_Xi_X_
#            systematics_Xi_Y[ period_ ][ arm_ ] = systematics_Xi_Y_
#            idx_low_edge_ = ( systematics_Xi_Y[ period_ ][ arm_ ] > 0. ).argmax()
#            idx_low_edge_inv_ = ( systematics_Xi_Y[ period_ ][ arm_ ][::-1] > 0. ).argmax()
#            print ( idx_low_edge_, systematics_Xi_Y[ period_ ][ arm_ ][ idx_low_edge_ ] )
#            print ( idx_low_edge_inv_, systematics_Xi_Y[ period_ ][ arm_ ][::-1][ idx_low_edge_inv_ ] )
#            systematics_Xi_Y[ period_ ][ arm_ ][:idx_low_edge_] = systematics_Xi_Y[ period_ ][ arm_ ][ idx_low_edge_ ]
#            systematics_Xi_Y[ period_ ][ arm_ ][::-1][:idx_low_edge_inv_] = systematics_Xi_Y[ period_ ][ arm_ ][::-1][ idx_low_edge_inv_ ]
#        
#    return ( systematics_Xi_X, systematics_Xi_Y )

def get_systematics_vs_xi_h5( data_periods, fileName="reco_characteristics/reco_characteristics_version1.h5" ):
    
    key_ = 'Xi'
    systematics_X_ = {}
    systematics_Y_ = {}
    with h5py.File( fileName, 'r' ) as f:
        print ( key_ )
        for period_ in f[ key_ ]:
            print ( period_ )
            systematics_X_[ period_ ] = {}
            systematics_Y_[ period_ ] = {}
            for arm_ in f[ key_ ][ period_ ]:
                print ( arm_ )
                print ( list( f[ key_ ][ period_ ][ arm_ ] ) )
                
                print ( f[ key_ ][ period_ ][ arm_ ][ 'X' ] )
                systematics_X_[ period_ ][ int( arm_ ) ] = np.array( f[ key_ ][ period_ ][ arm_ ][ 'X' ] )
                
                print ( f[ key_ ][ period_ ][ arm_ ][ 'Y' ] )
                systematics_Y_[ period_ ][ int( arm_ ) ] = np.array( f[ key_ ][ period_ ][ arm_ ][ 'Y' ] )
                
    return ( systematics_X_, systematics_Y_ )    
    
def random_experiment( df, data_periods, lumi_weights, variables, variations, resample=None ):
    
    lumi_weights_ = pd.Series( lumi_weights )
    lumi_weights_ = lumi_weights_.loc[ data_periods ]
    probs_lumi_ = lumi_weights_ / lumi_weights_.sum()
    print ( probs_lumi_ )
    
    for var_ in variables:
        print ( var_ )
        variation_X_, variation_Y_ = variations[ var_ ] # per period, arm
        
        df_arr_var_ = df.loc[ :, var_ ]
        df_arr_Arm_ = df.loc[ :, "Arm" ]
        
        # Sample periods
        sample_idx_arr_ = np.random.choice( np.arange( probs_lumi_.index.size ), df.shape[0], p=probs_lumi_ )
        period_arr_ = np.apply_along_axis( lambda idx_: probs_lumi_.index[ idx_ ], 0, sample_idx_arr_ )
        print ( period_arr_, period_arr_.size )
        
        # Fetch systematics
        df__ = pd.DataFrame( np.c_[ period_arr_, df_arr_Arm_, df_arr_var_ ], columns=("period","Arm",var_) )
        print ( df__ )
        sigma_var_ = df__.apply(
            lambda row:
                ( ( variation_Y_[ row[ "period" ] ][ row[ "Arm" ] ][ np.invert( variation_X_[ row[ "period" ] ][ row[ "Arm" ] ] <= row[ var_ ] ).argmax() - 1 ] +
                    variation_Y_[ row[ "period" ] ][ row[ "Arm" ] ][ ( variation_X_[ row[ "period" ] ][ row[ "Arm" ] ] >= row[ var_ ] ).argmax() ] ) / 2. ),
            axis=1 ).values 
        print ( sigma_var_, sigma_var_.size )
        
        # Apply systematics
        # Gaussian shift
        smeared_var_arr_ = df_arr_var_.values + ( 0. + np.random.randn( df_arr_var_.size ) * sigma_var_ )
        print ( smeared_var_arr_, smeared_var_arr_.size )
        
        df.loc[ :, "period_rnd" ] = period_arr_
        df.loc[ :, ( "sigma_" + var_ ) ] = sigma_var_
        df.loc[ :, ( var_ + "_smeared" ) ] = smeared_var_arr_
        