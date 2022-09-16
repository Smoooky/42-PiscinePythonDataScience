#!/bin/sh

if [ $# -eq 0 ]
  then
    INPUT_PATH="../ex01/hh.csv"
  else
    INPUT_PATH=$1
fi
  (head -n 1 ${INPUT_PATH}; tail -n 20 ${INPUT_PATH} | sort -t ',' -k 2 -k 1n ) > hh_sorted.csv
