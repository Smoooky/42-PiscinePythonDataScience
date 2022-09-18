#!/usr/bin/python3

import sys


def read_file(filename: str) -> list:
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines


def write_file(filename: str, lines: list) -> None:
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(lines)


def extract_name(email: str) -> tuple:
    dot_pos = email.find('.')
    at_sign_pos = email.find('@')
    name = email[:dot_pos].capitalize()
    surname = email[dot_pos + 1:at_sign_pos].capitalize()
    return name, surname


def to_tsv(emails: list) -> list:
    tsv_data = ['"Name"\t"Surname"\t"E-mail"\n']
    for email in emails:
        email = email.replace('\n', '')
        extracted = extract_name(email)
        tsv_data.append(f'"{extracted[0]}"\t"{extracted[1]}"\t"{email}"\n')
    return tsv_data


def main():
    if len(sys.argv) == 2:
        data = to_tsv(read_file(sys.argv[1]))
        write_file('employees.tsv', data)


if __name__ == '__main__':
    main()

