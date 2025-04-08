#!/bin/tcsh

### Replace the following lines according to your setup.
### The pps-dilepton-analysis dir contains the create_table.py script and select_events.py module as in the repository:
### git clone https://github.com/antoniovilela/pps-dilepton-analysis-notebook.git pps-dilepton-analysis
set EXEC=/eos/home-a/antoniov/SWAN_projects/pps-dilepton-analysis
set OUTPUT=/eos/home-a/antoniov/SWAN_projects/pps-dilepton-analysis/output
###

set files=$1
set label=$2
set data_sample=$3
set option1="$4"
set option2="$5"
set option3="$6"
set option4="$7"
set option5="$8"
set option6="$9"
set option7="$10"
set option8="$11"
set option9="$12"
set option10="$13"
set option11="$14"
set option12="$15"
echo "files: "$files
echo "label: "$label
echo "data sample: "$data_sample
echo "option: "$option1
echo "option: "$option2
echo "option: "$option3
echo "option: "$option4
echo "option: "$option5
echo "option: "$option6
echo "option: "$option7
echo "option: "$option8
echo "option: "$option9
echo "option: "$option10
echo "option: "$option11
echo "option: "$option12

echo $EXEC
echo $OUTPUT

set currentdir=`pwd`
cd $EXEC
echo $EXEC
source set_lcg.csh
cd $currentdir
echo $currentdir
ls

if ( ! $?PYTHONPATH ) then
    if ( ! $?PYTHON3PATH ) then
        setenv PYTHONPATH ${EXEC}
        echo "PYTHONPATH set to $PYTHONPATH"
    else
        setenv PYTHON3PATH ${PYTHON3PATH}:${EXEC}
        echo "PYTHON3PATH set to $PYTHON3PATH"
    endif 
else
    setenv PYTHONPATH ${PYTHONPATH}:${EXEC}
    echo "PYTHONPATH set to $PYTHONPATH"
endif
env

echo 'Running...'
set cmd_line_options = "--files=$files --label=$label --data_sample=$data_sample $option1 $option2 $option3 $option4 $option5 $option6 $option7 $option8 $option9 $option10 $option11 $option12"
echo python3 $EXEC/create_table.py $cmd_line_options
python3 $EXEC/create_table.py $cmd_line_options
cp *.h5 $OUTPUT
