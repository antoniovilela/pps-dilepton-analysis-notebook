#!/usr/bin/env python
# coding: utf-8

import os
import numpy as np
import pandas as pd
import h5py
import joblib
from joblib import dump, load

print ( "numpy: {}".format(np.__version__) )
print ( "joblib: {}".format(joblib.__version__) )

import sklearn
import tensorflow as tf
from tensorflow import keras

print ( "sklearn: {}".format(sklearn.__version__) )
print ( "tensorflow: {}".format(tf.__version__) )

from keras_model import Model, build_model

gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)
if gpus:
    tf.config.experimental.set_visible_devices(gpus[0], 'GPU')
    
print ( gpus )

# get_data, process_data, fiducial_cuts, fiducial_cuts_all, aperture_parametrisation, check_aperture
from processing import *

#proton_selection = "SingleRP"
proton_selection = "MultiRP"

#data_periods = [ "2017B", "2017C1", "2017C2", "2017D", "2017E", "2017F1", "2017F2", "2017F3" ]
data_periods = [ "2017B", "2017C1", "2017E", "2017F1" ]

run_tables = True

run_random_experiments = False

train_model = True
save_model = True
#learning_rate_scan = False
run_grid_search = True

n_iter_search_ = 192
#n_iter_search_ = 3
label_ = "test-multiRP"
base_path_ = "/eos/home-a/antoniov/SWAN_projects/pps-dilepton-analysis"

#n_events_signal = None
#n_events_bkg = None
#n_events_bkg = 100000

prob_cut_ = 0.50

L_B  = 2.360904801;
L_C1 = 5.313012839;
L_E  = 8.958810514;
L_F1 = 1.708478656;
lumi_periods = {}
lumi_periods[ "2017B" ]  = L_B
lumi_periods[ "2017C1" ] = L_C1
lumi_periods[ "2017E" ]  = L_E
lumi_periods[ "2017F1" ] = L_F1
print ( lumi_periods )
lumi_total = np.sum( list( lumi_periods.values() ) )
print ( "Total luminosity = {}".format( lumi_total ) )

label_signal = "Elastic"
fileNames_signal = [
    'output/output-MC2017-Elastic-Non3+3-PreSel.h5',
    #'output/output-MC2017-SingleDissociation-Non3+3-PreSel.h5'
]
fileNames_signal = [ "{}/{}".format( base_path_, item_ ) for item_ in fileNames_signal ]
print ( fileNames_signal )

resample_factor = 20
label_bkg = "data_random_resample_20"
fileNames_bkg = [
    'output/output-UL2017B-PreSel-Rnd-Res20.h5',
    'output/output-UL2017C1-PreSel-Rnd-Res20.h5',
    'output/output-UL2017E-PreSel-Rnd-Res20_0.h5',
    'output/output-UL2017E-PreSel-Rnd-Res20_1.h5',
    'output/output-UL2017F1-PreSel-Rnd-Res20.h5'
]
fileNames_bkg = [ "{}/{}".format( base_path_, item_ ) for item_ in fileNames_bkg ]
print ( fileNames_bkg )

# Signal

import time
print( time.strftime("%Y/%m/%d %H:%M:%S", time.localtime() ) )
time_s_ = time.time()

df_counts_signal, df_signal = 2 * [None]

fileName_ = "{}/reduced-data-store-{}.h5".format( base_path_, label_signal )
if run_tables:
    with pd.HDFStore( fileName_, complevel=5 ) as store_:

        df_counts_signal_, df_signal_ = get_data( fileNames_signal )
        df_signal_ = process_data( df_signal_, proton_selection, min_mass = 110. )
        
        store_[ "counts" ] = df_counts_signal_
        store_[ "df" ] = df_signal_

with pd.HDFStore( fileName_, 'r' ) as store_:
    df_counts_signal = store_[ "counts" ]
    df_signal = store_[ "df" ]

# Random experiments

if run_random_experiments:
    from random_experiment import *
    
    np.random.seed( 42 )

    # per period, arm
    systematics = {}
    #systematics[ "Xi" ] = ( systematics_Xi_X, systematics_Xi_Y )
    #fileName_ = "{}/{}".format( base_path_, "reco_characteristics/reco_characteristics_version1.root" )
    fileName_ = "{}/{}".format( base_path_, "reco_characteristics/reco_characteristics_version1.h5" )
    systematics[ "Xi" ] = get_systematics_vs_xi_h5( data_periods, fileName=fileName_ )
    print ( systematics[ "Xi" ] )
    
    random_experiment( df_signal, data_periods=data_periods, lumi_weights=lumi_periods, variables=[ "Xi" ], variations=systematics )
    
df_signal[:20]

time_e_ = time.time()
print ( "Total time elapsed: {:.0f}".format( time_e_ - time_s_ ) )

# Background

import time
print( time.strftime("%Y/%m/%d %H:%M:%S", time.localtime() ) )
time_s_ = time.time()

df_counts_bkg, df_bkg = 2 * [None]

fileName_ = "{}/reduced-data-store-{}.h5".format( base_path_, label_bkg )
if run_tables:
    with pd.HDFStore( fileName_, complevel=5 ) as store_:

        df_counts_bkg_list_ = []
        df_bkg_list_ = []
        for file_ in fileNames_bkg:
            df_counts_bkg_, df_bkg_ = get_data( [ file_ ] )
            df_bkg_ = process_data( df_bkg_, proton_selection, min_mass = 110., within_aperture=True )
            df_counts_bkg_list_.append( df_counts_bkg_ )
            df_bkg_list_.append( df_bkg_ )

        df_counts_bkg_ = df_counts_bkg_list_[0]
        for idx_ in range( 1, len( df_counts_bkg_list_ ) ):
            df_counts_bkg_ = df_counts_bkg_.add( df_counts_bkg_list_[idx_] )

        df_bkg_ = pd.concat( df_bkg_list_ )
        
        store_[ "counts" ] = df_counts_bkg_
        store_[ "df" ] = df_bkg_

with pd.HDFStore( fileName_, 'r' ) as store_:
    df_counts_bkg = store_[ "counts" ]
    df_bkg = store_[ "df" ]

time_e_ = time.time()
print ( "Total time elapsed: {:.0f}".format( time_e_ - time_s_ ) )

# Set aside test sample

from sklearn.model_selection import train_test_split

y_sig_ = np.ones( df_signal.shape[0] )
y_bkg_ = np.zeros( df_bkg.shape[0] )

df_signal_train, df_signal_test, y_sig_train, y_sig_test = train_test_split( df_signal, y_sig_, test_size=0.40, shuffle=True, random_state=12345 )
df_bkg_train, df_bkg_test, y_bkg_train, y_bkg_test = train_test_split( df_bkg, y_bkg_, test_size=0.40, shuffle=True, random_state=12345 )

print ( df_signal_train, df_signal_test, y_sig_train, y_sig_test )
print ( df_bkg_train, df_bkg_test, y_bkg_train, y_bkg_test )

print ( [ arr_.shape[0] for arr_ in ( df_signal_train, df_signal_test, y_sig_train, y_sig_test ) ] )
print ( [ arr_.shape[0] for arr_ in ( df_bkg_train, df_bkg_test, y_bkg_train, y_bkg_test ) ] )

# Select variables

X_sig_train = None
X_sig_test = None
if run_random_experiments:
    X_sig_train = df_signal_train[ ['Xi_smeared', 'Muon0Pt', 'Muon1Pt', 'InvMass', 'ExtraPfCands', 'Acopl', 'XiMuMu'] ].rename( columns={ "Xi_smeared": "Xi" } )
    X_sig_test = df_signal_test[ ['Xi_smeared', 'Muon0Pt', 'Muon1Pt', 'InvMass', 'ExtraPfCands', 'Acopl', 'XiMuMu'] ].rename( columns={ "Xi_smeared": "Xi" } )
else:
    X_sig_train = df_signal_train[ ['Xi', 'Muon0Pt', 'Muon1Pt', 'InvMass', 'ExtraPfCands', 'Acopl', 'XiMuMu'] ]
    X_sig_test = df_signal_test[ ['Xi', 'Muon0Pt', 'Muon1Pt', 'InvMass', 'ExtraPfCands', 'Acopl', 'XiMuMu'] ]

X_bkg_train = df_bkg_train[ ['Xi', 'Muon0Pt', 'Muon1Pt', 'InvMass', 'ExtraPfCands', 'Acopl', 'XiMuMu'] ]
X_bkg_test = df_bkg_test[ ['Xi', 'Muon0Pt', 'Muon1Pt', 'InvMass', 'ExtraPfCands', 'Acopl', 'XiMuMu'] ]

print ( X_sig_train[:20] )
print ( X_sig_test[:20] )

X_bkg = df_bkg[ ['Xi', 'Muon0Pt', 'Muon1Pt', 'InvMass', 'ExtraPfCands', 'Acopl', 'XiMuMu'] ]

print ( X_bkg_train[:20] )
print ( X_bkg_test[:20] )

X_ = pd.concat( [X_sig_train, X_bkg_train] ) 
y_ = np.concatenate( [y_sig_train, y_bkg_train] )

X_train, X_valid, y_train, y_valid = train_test_split( X_, y_, test_size=0.20, shuffle=True, random_state=42 )

X_test = pd.concat( [X_sig_test, X_bkg_test] ) 
y_test = np.concatenate( [y_sig_test, y_bkg_test] )

# Scale inputs

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform( X_train )
X_valid_scaled = scaler.transform( X_valid )
X_test_scaled = scaler.transform( X_test )
print ( scaler )

if train_model and save_model:
    import time
    id_ = time.strftime("%Y_%m_%d-%H_%M_%S")
    fileName_ = "standard_scaler_{}_{}.joblib".format( label_, id_ )
    print ( "Saving scaler to {}".format( fileName_ ) )
    dump( scaler, fileName_ )

print ( X_train_scaled[:20] )

# Define training callbacks

def get_run_logdir(log_dir):
    import time
    run_id = time.strftime("run_%Y_%m_%d-%H_%M_%S")
    return os.path.join(log_dir, run_id)

def callbacks(patience=10, log_dir=""):
    callbacks_ = []
    # Early stopping
    if patience > 0:
        early_stopping_cb_ = keras.callbacks.EarlyStopping( patience=patience, restore_best_weights=True )
        callbacks_.append( early_stopping_cb_ )
        
    # TensorBoard
    if log_dir:
        run_logdir = get_run_logdir(log_dir)
        print ( "Log dir: {}".format(run_logdir) )
        tensorboard_cb_ = keras.callbacks.TensorBoard( run_logdir )
        callbacks_.append( tensorboard_cb_ )
    
    return callbacks_

# ### Hyperparameter scan

learning_rate = 5e-4
epochs_grid_search = 20

grid_search = None
if train_model and run_grid_search:
    import time
    print( time.strftime("%Y/%m/%d %H:%M:%S", time.localtime() ) )
    time_s_ = time.time()

    from sklearn.model_selection import RandomizedSearchCV
    #from sklearn.model_selection import GridSearchCV

    build_fn_ = Model( input_shape=X_train_scaled.shape[1:], learning_rate=learning_rate )
    keras_clf = keras.wrappers.scikit_learn.KerasClassifier( build_fn_ )

#     #param_grid = [
#     #    { "n_hidden": [2],
#     #      "n_neurons": [50,100] }
#     #    ]
#     param_grid = [
#         { "n_hidden": np.arange(1,3),
#           "n_neurons": [20,50] }
#         ]

    param_distribs = {
        "n_hidden": np.arange(2,6),
        "n_neurons": 2 ** np.arange(4,8),
        "dropout":  0.1 * np.arange(2,6),
        "batch_size": 2 ** np.arange(5,8)
        }

    #grid_search = GridSearchCV( keras_clf, param_grid, cv=3, scoring='f1', refit=False )
    
    grid_search = RandomizedSearchCV(
        keras_clf,
        param_distribs,
        n_iter=n_iter_search_, cv=3, verbose=20, n_jobs=-1, scoring='f1', refit=False, random_state=42
        )

    callbacks_ = callbacks(patience=5)
    print ( callbacks_ )
    grid_search.fit( X_train_scaled, y_train, epochs=epochs_grid_search, validation_data=(X_valid_scaled, y_valid), callbacks=callbacks_ )
    
    print ( grid_search.best_params_ )
    print ( grid_search.best_score_ )
    print ( grid_search.cv_results_ )
    
    time_e_ = time.time()
    print ( "Total time elapsed: {:.0f}".format( time_e_ - time_s_ ) )

# Build model

model_final = None

if train_model:
    params = {'n_hidden': 1, 'n_neurons': 50, 'dropout': 0.20}
    batch_size = 32
    if run_grid_search: 
        params = grid_search.best_params_.copy()
        batch_size = params[ 'batch_size' ]
        params.pop( 'batch_size' )
    print ( params, "batch_size: {}".format( batch_size ) )
    
    model_final = build_model(input_shape=X_train_scaled.shape[1:], learning_rate=learning_rate, **params)
    model_final.summary()
    #log_dir="keras_logs"
    #callbacks_ = callbacks(patience=5, log_dir=log_dir)
    callbacks_ = callbacks( patience=5 )
    print ( callbacks_ )
    model_final.fit( X_train_scaled, y_train, epochs=100, batch_size=batch_size, validation_data=(X_valid_scaled, y_valid), callbacks=callbacks_ )
else:
    model_final = keras.models.load_model( "model/keras_model.h5" )
    
model_final.summary()

# Evaluate on training data (without dropout)

model_final.evaluate( X_train_scaled, y_train )

# Re-evaluate on validation data 

model_final.evaluate( X_valid_scaled, y_valid )

# Evaluate on test data

model_final.evaluate( X_test_scaled, y_test )

y_test_proba = model_final.predict( X_test_scaled )
print ( y_test_proba )

print ( "Prob. cut: {}".format( prob_cut_ ) )

y_test_pred = ( y_test_proba >= prob_cut_ ).astype( "int32" )
print ( y_test_pred )

from sklearn.metrics import accuracy_score
print ( accuracy_score( y_test, y_test_pred ) )
print ( accuracy_score( y_test[ y_test == 1 ], y_test_pred[ y_test == 1 ] ) )
print ( accuracy_score( y_test[ y_test == 0 ], y_test_pred[ y_test == 0 ] ) )

# Save model

if train_model and save_model:
    import time
    id_ = time.strftime("%Y_%m_%d-%H_%M_%S")
    fileName_ = "keras_model_{}_{}.h5".format( label_, id_ )
    print ( "Saving model to {}".format( fileName_ ) )
    model_final.save( fileName_ )

