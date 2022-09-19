#!/usr/bin/python3

from os import access, R_OK
from sys import argv


class Research:
    def __init__(self, path_to_file: str) -> None:
        self.path_to_file = path_to_file

    @staticmethod
    def is_header_correct(csv_header: str) -> bool:
        col_names = csv_header.replace('\n', '').split(',')
        if len(col_names) != 2:
            return False
        return all(col_names)

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

    def file_reader(self):
        if not access(self.path_to_file, R_OK):
            raise OSError("Can't read the file")

        res = ''
        with open(self.path_to_file, 'r', encoding='utf-8') as file:
            header = file.readline()
            if not self.is_header_correct(header):
                raise ValueError('Incorrect header format')

            res += header
            line = file.readline()
            if not self.is_line_correct(line):
                raise ValueError('No lines after header')
            res += line

            for line in file:
                if not self.is_line_correct(line):
                    raise ValueError('Incorrect line format')
                res += line
            return res


def main():
    if len(argv) == 2:
        researcher = Research(argv[1])
        try:
            print(researcher.file_reader())
        except Exception as err:
            print(type(err).__name__, err, sep=': ')


if __name__ == "__main__":
    main()
