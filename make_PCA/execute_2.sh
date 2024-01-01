#!/bin/bash

start=$(date +%s)
cat vars_2.txt | xargs -n 2 -P 6 python3 main.py
end=$(date +%s)

echo "Elapsed Time: $(($end-$start)) seconds"