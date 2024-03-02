#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: gather.sh <i>"
    exit 1
fi

i=$1
if [ ! -e R$i ]; then
    echo "Directory R$i does not exist"
    exit 1
fi

for f in $(ls *.cnf); do
    hash=$(echo $f | cut -d'-' -f1)
    isize=$(stat -c%s "$f")
    osize=$(stat -c%s "R$i/$f")
    #c total process time since initialization:        17.95    seconds
    time=$(grep "c total process time since initialization" "R$i/$f.out" | tr -s ' ' | cut -d' ' -f7)
    #s UNSATISFIABLE
    result=$(grep ^s "R$i/$f.out" | cut -d' ' -f2)
    if [ -z "$result" ]; then
        result="UNKNOWN"
    fi
    echo "$hash,$result,$isize,$osize,$time"
done