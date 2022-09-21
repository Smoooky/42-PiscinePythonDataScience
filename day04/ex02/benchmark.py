#!/usr/bin/env python3

import timeit
from sys import argv


def get_email_list() -> list:
    emails = ['john@gmail.com', 'james@gmail.com',
              'alice@yahoo.com', 'anna@live.com',
              'philipp@gmail.com'] * 5
    return emails


def loop_approach(emails: list) -> list:
    res = []
    for address in emails:
        if address.split('@')[1] == 'gmail.com':
               res.append(address)
    return res


def list_comprehension_approach(emails: list) -> list:
    res = [i for i in emails if i.split('@')[1] == 'gmail.com']
    return res


def map_approach(emails: list) -> list:
    def to_gmail(address: str) -> str:
        if address.split('@')[1] == 'gmail.com':
            return address

    return list(map(to_gmail, emails))


def filter_approach(emails: list) -> list:
    def is_gmail(address: str) -> bool:
        if address.split('@')[1] == 'gmail.com':
            return True
        return False
    return list(filter(is_gmail, emails))


def main():
    if len(argv) == 3:
        print(timeit.timeit(argv[1] + '_approach(get_email_list())',
                            'from __main__ import get_email_list, loop_approach, '
                            'list_comprehension_approach, map_approach, '
                            'filter_approach', number=int(argv[2])))
    else:
        print('Wrong amount of arguments: waiting for 2, given: ' + str(len(argv) - 1))


if __name__ == '__main__':
    main()
