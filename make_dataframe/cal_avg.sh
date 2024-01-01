#!/bin/bash
#cal_avg.sh

touch day_avg.csv
start=$(date +%s)
seq 1 365 | xargs -n 1 -P $1 python3 ./cal_day_avg.py >> ./day_avg.csv
end=$(date +%s)
echo "time: $(($end-$start)) sec"

#cal_avg_mp.sh
touch day_avg_mp.csv
start=$(date +%s)
echo 366 | xargs -n 1 -P $1 python3 ./cal_day_avg_mp.py >> ./day_avg_mp.csv
end=$(date +%s)
echo "time with mp: $(($end-$start)) sec"

#cal_avg_ppe.sh
touch day_avg_ppe.csv
start=$(date +%s)
echo 366 | xargs -n 1 -P $1 python3 ./cal_day_avg_ppe.py >> ./day_avg_ppe.csv
end=$(date +%s)
echo "time with ppe: $(($end-$start)) sec"
