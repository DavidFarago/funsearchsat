#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: gather.sh <i>"
    exit 1
fi

i=$1
if [ ! -e R$i ]; then
    mkdir -p R$i
fi

for f in $(ls *.cnf); do 
    cadical -P$i -d 0 -o R$i/$f $f > R$i/$f.out
done
