#!/usr/bin/python3

from sys import argv
from random import randint
from os import access, R_OK


class Research:
    def __init__(self, path_to_file: str) -> None:
        self.path_to_file = path_to_file

    @staticmethod
    def is_header_correct(csv_header: str) -> bool:
        if csv_header != 'head,tail\n':
            return False
        return True

    @staticmethod
    def is_line_correct(line: str) -> bool:
        correct_vals = [['0', '1'],
                        ['1', '0']]

        line = line.replace('\n', '')
        if not line:
            return False

        vals = line.split(',')
        if len(vals) != 2:
            return False

        return vals in correct_vals

    def file_reader(self, has_header=True) -> list:
        if not access(self.path_to_file, R_OK):
            raise OSError("Can't read the file")

        res = []
        with open(self.path_to_file, 'r', encoding='utf-8') as file:
            if has_header:
                header = file.readline()
                if not self.is_header_correct(header):
                    raise ValueError('Incorrect header format')

            line = file.readline()
            if not line:
                raise ValueError('No lines after header')
            if not self.is_line_correct(line):
                raise ValueError('Incorrect line format')
            res.append([int(x) for x in line.split(',')])

            for line in file:
                if not self.is_line_correct(line):
                    raise ValueError('Incorrect line format')
                res.append([int(x) for x in line.split(',')])
            return res

    class Calculations:
        def __init__(self, data: list) -> None:
            self.data = data

        def counts(self) -> tuple:
            heads = 0
            tails = 0
            for val in self.data:
                tails += val[0]
                heads += val[1]

            return heads, tails

        @staticmethod
        def fractions(head_and_tails: tuple) -> tuple:
            total = sum(head_and_tails)
            return tuple(val / total * 100 for val in head_and_tails)

    class Analytics(Calculations):
        @staticmethod
        def predict_random(num_of_predictions: int) -> list:
            res = []
            while num_of_predictions:
                rand = randint(0, 1)
                res.append([rand, int(not rand)])
                num_of_predictions -= 1
            return res

        def predict_last(self) -> list:
            return self.data[-1]


def main():
    if len(argv) == 2:
        researcher = Research(argv[1])
        try:
            data = researcher.file_reader()
        except Exception as err:
            print(type(err).__name__, err, sep=': ')
            return

        anal = researcher.Analytics(data)
        counts = anal.counts()
        fractions = anal.fractions(counts)
        predict_rand = anal.predict_random(3)
        predict_last = anal.predict_last()

        print(data)
        print(counts[0], counts[1])
        print(fractions[0], fractions[1])
        print(predict_rand, predict_last, sep='\n')


if __name__ == "__main__":
    main()
