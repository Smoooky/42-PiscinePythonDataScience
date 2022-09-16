#!/bin/sh

if [ $# -eq 0 ]
  then
    CSV_PATH="../ex03/hh_positions.csv"
  else
    CSV_PATH=$1
fi

echo '"name","count"' > hh_uniq_positions.csv

cat $CSV_PATH \
  | awk 'BEGIN{FS=OFS=",";} NR>1 {print $3;}' \
  | sort \
  | uniq -c \
  | awk 'BEGIN{OFS=","} {print $2, $1;}' \
  >> hh_uniq_positions.csv