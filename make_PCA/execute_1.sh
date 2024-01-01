#!/bin/bash
python3 GetCombis.py > vars_2.txt

time {
    cat ./vars_2.txt | xargs -n 2 -P $1 python3 main.py >> result_for_${1}.txt
}