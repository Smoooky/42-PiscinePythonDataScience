#!/usr/bin/env python3

import timeit


def get_email_list() -> list:
    emails = ['john@gmail.com', 'james@gmail.com',
              'alice@yahoo.com', 'anna@live.com',
              'philipp@gmail.com'] * 5
    return emails


def map_approach(emails: list) -> list:
    def is_gmail(address: str) -> str:
        if address.split('@')[1] == 'gmail.com':
            return address

    return list(map(is_gmail, emails))


def usual_approach(emails: list) -> list:
    res = []
    for address in emails:
        if address.split('@')[1] == 'gmail.com':
            res.append(address)
    return res


def efficient_approach(emails: list) -> list:
    res = [i for i in emails if i.split('@')[1] == 'gmail.com']
    return res


def main():
    time_res = {
        'map': timeit.timeit('map_approach(get_email_list())',
                             'from __main__ import map_approach, get_email_list',
                             number=900000),
        'loop': timeit.timeit('usual_approach(get_email_list())',
                              'from __main__ import usual_approach, get_email_list',
                              number=900000),
        'list comprehension': timeit.timeit('efficient_approach(get_email_list())',
                                            'from __main__ import efficient_approach, get_email_list',
                                            number=900000)
    }

    fastest = min(time_res.items(), key=lambda t: t[1])
    print(f'it is better to use a {fastest[0]}')

    output = ''
    for val in sorted(time_res.values()):
        output += f'{val} vs '
    print(output[:-4])


if __name__ == '__main__':
    main()
