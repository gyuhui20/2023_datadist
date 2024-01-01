#!/bin/bash

touch data_using_${1}process.txt
echo Q_0, N_end, time >> data_using_${1}process.txt

START=1
END=400

#Q_0에 1부터 400까지 넣는 과정을 실행함
#위의 과정을 1부터 8개까지의 CPU를 사용하는 프로세스를 순서대로 진행하고, 진행 시간을 따로 기록함(.txt파일)
for Q0 in `seq $START $END`; do
  echo get_N_end_numpy.py -Q_0 $Q0
done | xargs -n 3 -P $1 python >> data_using_${1}process_np.txt

