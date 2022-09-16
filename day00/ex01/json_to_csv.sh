#!/bin/sh

if [ $# -eq 0 ]
  then
    INPUT_PATH="../ex00/hh.json"
  else
    INPUT_PATH=$1
fi

OUTPUT_PATH=hh.csv

FILTER_FILE=filter.jq

jq -rf ${FILTER_FILE} ${INPUT_PATH}> ${OUTPUT_PATH}