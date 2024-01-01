#!/bin/bash

MINPROC=1
MAXPROC=6

touch time_by_process.txt
touch TimeResult.txt

for PROC in `seq $MINPROC $MAXPROC`; do
  echo --------------------------------------------------- | tee -a time_by_process.txt
  echo number of process: $PROC | tee -a time_by_process.txt
  (./execute_1.sh $PROC) 2>&1 | tee -a time_by_process.txt
done

python3 SpeedUp.py > TimeResult.txt

