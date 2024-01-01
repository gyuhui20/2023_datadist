#!/bin/bash
MINPROC=1
MAXPROC=6

touch time_by_process.txt

for PROC in `seq $MINPROC $MAXPROC`; do
  echo number of process: $PROC | tee -a time_by_process.txt
  (./cal_avg.sh $PROC) 2>&1 | tee -a time_by_process.txt
done

