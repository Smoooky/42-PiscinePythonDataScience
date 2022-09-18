#!/usr/bin/python3

import sys


def read_file(filename: str) -> list:
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines


def write_file(filename: str, lines: list) -> None:
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(lines)


def get_letter_start(email: str, emails_data: list) -> str:
    found = False

    for line in emails_data[1:]:
        line = line.replace('\n', '')
        fields = line.split('\t')
        if fields[2] == f'"{email}"':
            found = True
            break

    if not found:
        raise RuntimeError("Email not found")

    return f'Dear {fields[0][1: -1]}, welcome to our team. ' + \
           'We are sure that it will be a pleasure to work with you. ' + \
           'That’s a precondition for the professionals that our company hires.'


def main():
    if len(sys.argv) == 2:
        res = get_letter_start(sys.argv[1], read_file('employees.tsv'))
        print(res)


if __name__ == '__main__':
    main()
