#!/usr/bin/env python
# coding: utf-8

import os
import numpy as np
import pandas as pd
import h5py
#import matplotlib.pyplot as plt
#from matplotlib.colors import LogNorm
from joblib import dump, load

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier

# get_data, process_data, fiducial_cuts, fiducial_cuts_all, aperture_parametrisation, check_aperture
from processing import *

#proton_selection = "SingleRP"
proton_selection = "MultiRP"

train_model = True
run_grid_search = True
save_model = True
n_iter_search_ = 30
label_ = "test-Non3+3-Elatic+SingleDissociation-multiRP"
base_path_ = "/eos/home-a/antoniov/SWAN_projects/pps-dilepton-analysis"

fileNames_signal = [
    'output/output-MC2017-Elastic-Non3+3-PreSel.h5',
    'output/output-MC2017-SingleDissociation-Non3+3-PreSel.h5'
]
fileNames_signal = [ os.path.join( base_path_, file_) for file_ in fileNames_signal ]
print ( fileNames_signal )

resample_factor = 20
fileNames_bkg = [
    'output/output-UL2017B-PreSel-Rnd-Res20.h5',
    'output/output-UL2017C1-PreSel-Rnd-Res20.h5',
    'output/output-UL2017E-PreSel-Rnd-Res20.h5',
    'output/output-UL2017F1-PreSel-Rnd-Res20.h5'
]
fileNames_bkg = [ os.path.join( base_path_, file_) for file_ in fileNames_bkg ]
print ( fileNames_bkg )

# Signal
df_counts_signal, df_signal = get_data( fileNames_signal )
df_signal = process_data( df_signal, proton_selection )
df_signal[:20]

# Background
df_counts_bkg, df_bkg = get_data( fileNames_bkg )
df_bkg = process_data( df_bkg, proton_selection )
df_bkg[:20]

# Select variables
X_sig = df_signal[ ['Xi', 'Muon0Pt', 'Muon1Pt', 'InvMass', 'ExtraPfCands', 'Acopl', 'XiMuMu'] ]
print ( X_sig[:20] )

X_bkg = df_bkg[ ['Xi', 'Muon0Pt', 'Muon1Pt', 'InvMass', 'ExtraPfCands', 'Acopl', 'XiMuMu'] ]
print ( X_bkg[:20] )

y_sig = np.ones( len(X_sig) )
y_bkg = np.zeros( len(X_bkg) )

X = pd.concat( [X_sig, X_bkg] ) 
y = np.concatenate( [y_sig, y_bkg] )

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, shuffle=True, random_state=42 )

# Hyperparameter scan

grid_search = None

if train_model and run_grid_search:
    from sklearn.model_selection import RandomizedSearchCV
    #from sklearn.model_selection import GridSearchCV
    #from scipy.stats import uniform

    param_distribs = {
        "base_estimator__max_depth": np.arange(2,11),
        "base_estimator__min_samples_split": np.arange(2,11),
        "n_estimators": 100 * np.arange(2,6),
        "learning_rate": 0.1 * np.arange(4,16)
        }
    #param_grid = [
    #    { "max_depth": np.arange(2,10),
    #      "n_estimators": 100 * np.arange(1,6),
    #      "learning_rate": 0.1 * np.arange(5,11) }
    #    ]

    grid_search = RandomizedSearchCV(
        AdaBoostClassifier(
            DecisionTreeClassifier(),
            algorithm="SAMME.R"
            ),
        param_distribs,
        n_iter=n_iter_search_, cv=4, verbose=20, n_jobs=-1, random_state=42
        )
    grid_search.fit( X_train, y_train )

    print ( grid_search.best_params_ )
    print ( grid_search.best_score_ )
    print ( grid_search.cv_results_ )

model_final = None
if train_model:
    if run_grid_search: 
        #print ( grid_search.best_estimator_)
        model_final = grid_search.best_estimator_
    else:
        model_final = AdaBoostClassifier(
            DecisionTreeClassifier( max_depth=4 ),
            n_estimators = 200,
            algorithm="SAMME.R",
            learning_rate = 0.5
            )
        model_final.fit( X_train, y_train )
else:
    model_final = load( "ada_clf.joblib" )
    
print ( model_final )

# Evaluate on test data

y_test_proba = model_final.predict_proba( X_test )[:,1]
print ( y_test_proba )

prob_cut = 0.50

y_test_pred = ( y_test_proba >= prob_cut ).astype( "int32" )
print ( y_test_pred )

from sklearn.metrics import accuracy_score
print ( accuracy_score( y_test, y_test_pred ) )
print ( accuracy_score( y_test[ y_test == 1 ], y_test_pred[ y_test == 1 ] ) )
print ( accuracy_score( y_test[ y_test == 0 ], y_test_pred[ y_test == 0 ] ) )

test_errors = []
for test_predict_proba in model_final.staged_predict_proba( X_test ):
    test_errors.append( 1. - accuracy_score( ( test_predict_proba[:,1] >= prob_cut ), y_test ) )

n_trees = len( model_final )

estimator_errors = model_final.estimator_errors_[:n_trees]

print ( test_errors )
print ( estimator_errors )

# Save model

if train_model and save_model:
    import time
    id_ = time.strftime("%Y_%m_%d-%H_%M_%S")
    fileName_ = "adaboost_clf_{}_{}.joblib".format( label_, id_ )
    print ( "Saving model to {}".format( fileName_ ) )
    dump( model_final, fileName_ )

