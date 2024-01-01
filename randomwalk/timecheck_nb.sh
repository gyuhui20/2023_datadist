#!/bin/bash

MINPROC=1
MAXPROC=8

touch time_by_using_process_number.txt

for PROC in `seq $MINPROC $MAXPROC`; do
  echo --------------------------------------------------- | tee -a time_by_using_process_number.txt
  echo number of process: $PROC | tee -a time_by_using_process_number.txt
  (time ./run_numba.sh $PROC) 2>&1 | tee -a time_by_using_process_number.txt
  echo --------------------------------------------------- | tee -a time_by_using_process_number.txt
done