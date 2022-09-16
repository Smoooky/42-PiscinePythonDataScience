#!/bin/sh

if [ $# -eq 0 ]
then
  echo "Please enter input files from the result of partitioner.sh"
else
{
  list=($*)
  head -n 1 ${list[0]} > concatenates.csv
  for i in ${list[@]}
  do
    tail -n +2 $i >> concatenates.csv
  done
}
fi