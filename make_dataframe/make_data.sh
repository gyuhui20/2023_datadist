#!/bin/bash
mkdir csv_total

python3 make_date.py > make_date.txt

for PROC in `seq 1 365`; do
    python3 ./make_data4day.py $PROC > ./csv_total/$PROC.csv
done

