#!/bin/sh

if [ $# -eq 0 ]
  then
    INPUT_PATH="../ex02/hh_sorted.csv"
  else
    INPUT_PATH=$1
fi

OUTPUT_PATH="hh_positions.csv"

head -n 1 ${INPUT_PATH} > ${OUTPUT_PATH}
tail -n +2 ${INPUT_PATH} | \
awk \
    'BEGIN{
      FS=OFS="\",";

      Regexes[0] = "[Jj]unior";
      Regexes[2] = "[Mm]iddle";
      Regexes[4] = "[Ss]enior";
    }

    {
      result = "";
      for (i = 0; i < length(Regexes); ++i)
      {
        match($3, Regexes[i]);
        if (RLENGTH > 0) {
          first_char = substr($3, RSTART, 1);
          if (length(result) == 0)
            result = toupper(first_char) substr($3, RSTART + 1, RLENGTH - 1);
          else
            result = result "/" toupper(first_char) substr($3, RSTART + 1, RLENGTH - 1);
        }
      }
      if (length(result) == 0) {
        $3 = "\"-";
      }
      else {
        $3 = "\"" result;
      }
      print;
    }' \
    >> ${OUTPUT_PATH}