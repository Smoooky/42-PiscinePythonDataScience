#!/usr/bin/python3

import sys


def get_dicts() -> tuple:
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }

    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }

    return COMPANIES, STOCKS


def is_key(raw: str, dictionary: dict) -> tuple:
    prepared = raw.lower()

    for key in dictionary:
        if prepared == key.lower():
            return True, key
    return False, ''


def process_request(raw_list: list) -> None:
    companies, stocks = get_dicts()

    if len(raw_list) == 0:
        return

    for value in raw_list:
        res = is_key(value, companies)
        if res[0]:
            print(f'{ res[1] } stock price is { stocks[companies[res[1]]] }')
            continue

        res = is_key(value, stocks)
        if res[0]:
            print(f'{ res[1] } is a ticker symbol for ' +
                  f'{ list(companies.keys())[list(companies.values()).index(res[1])] }')
            continue

        print(f'{ value } is an unknown company or an unknown ticker symbol')
    return


def parse_args(arg: str, sep=',') -> list:
    arg = arg.replace(' ', '')

    arg_list = []
    begin_index = 0
    while begin_index < len(arg):
        end_index = arg.find(sep, begin_index)
        if end_index + 1 >= len(arg):  # trailing comma
            return []

        if end_index == -1:  # end of line
            end_index = len(arg)

        # empty value -> return empty list
        if end_index - begin_index < 1:
            return []

        # push and go next
        arg_list.append(arg[begin_index:end_index])
        begin_index = end_index + 1

        # return the result
    return arg_list


def main():
    if len(sys.argv) == 2:
        raw_list = parse_args(sys.argv[1])
        process_request(raw_list)


if __name__ == '__main__':
    main()
