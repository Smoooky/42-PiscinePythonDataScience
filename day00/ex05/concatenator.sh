#!/bin/sh

if [ $# -eq 0 ]
then
  echo "Please enter input files from the result of partitioner.sh"
else
{
  i=$#
  head -n 1 $${i} > "concatenates.csv"
#  while [ i != 0 ]; do
#     tail -n +2 $${i} >> "concatenates.csv"
#     i=${i}+1
#  done
}
fi