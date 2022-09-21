#!/usr/bin/env python3

import timeit


def get_email_list() -> list:
    emails = ['john@gmail.com', 'james@gmail.com',
              'alice@yahoo.com', 'anna@live.com',
              'philipp@gmail.com'] * 5
    return emails


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
    usual_approach_time = timeit.timeit('usual_approach(get_email_list())',
                                        'from __main__ import usual_approach, get_email_list',
                                        number=900000)
    efficient_approach_time = timeit.timeit('efficient_approach(get_email_list())',
                                            'from __main__ import efficient_approach, get_email_list',
                                            number=900000)

    if efficient_approach_time <= usual_approach_time:
        print('it is better to use a list comprehension')
    else:
        print('it is better to use a loop')

    print(f'{min(usual_approach_time, efficient_approach_time)} vs ' +
          f'{max(usual_approach_time, efficient_approach_time)}')


if __name__ == '__main__':
    main()
