#!/bin/bash

touch data_using_${1}process.txt
echo Q_0, N_end, time >> data_using_${1}process.txt

START=1
END=400

for Q0 in `seq $START $END`; do
  echo get_N_end_random.py -Q_0 $Q0
done | xargs -n 3 -P $1 python >> data_using_${1}process_rd.txt
