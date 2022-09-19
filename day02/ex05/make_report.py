#!/usr/bin/python3

from analitics import Research
from config import *


def main():
    researcher = Research(FILEPATH)

    try:
        data = researcher.file_reader(has_header=HAS_HEADER)
    except Exception as err:
        print(type(err).__name__, err, sep=': ')
        return

    anal = Research.Analytics(data)
    counts = anal.counts()
    fractions = anal.fractions(counts)
    predict_rand = anal.predict_random(NUM_OF_STEPS)
    report = REPORT_TEMPLATE.format(sum(counts), counts[1], counts[0],
                                    fractions[1], fractions[0],
                                    NUM_OF_STEPS, predict_rand.count([1, 0]),
                                    predict_rand.count([0, 1]))
    anal.save_file(report, 'report', 'txt')


if __name__ == '__main__':
    main()