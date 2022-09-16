#!/usr/bin/sh

if [ $# -eq 0 ]
  then
    VACANCY='data scientist'
  else
    VACANCY=$1
fi
  curl -A "sstyr" -G "https://api.hh.ru/vacancies"\
  --data-urlencode "text=${VACANCY}"\
  --data-urlencode 'per_page=20'\
  | jq > hh.json