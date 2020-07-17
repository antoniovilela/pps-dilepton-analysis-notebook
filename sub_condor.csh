#!/bin/tcsh

source /afs/cern.ch/work/a/antoniov/env/uproot4/bin/activate.csh

set file=$1
set label=$2
set option=$3
set EXEC=/eos/home-a/antoniov/SWAN_projects/pps-dilepton-analysis
set OUTPUT=/eos/home-a/antoniov/SWAN_projects/pps-dilepton-analysis/output
echo "file: "$file
echo "label: "$label
echo "option: "$option
echo $EXEC
echo $OUTPUT
env

echo $PWD

echo 'Running...'
echo python $EXEC/create_table.py --files=$file --label=$label $option
python $EXEC/create_table.py --files=$file --label=$label $option

cp *.h5 $OUTPUT

