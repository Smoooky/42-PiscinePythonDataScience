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


def print_name_and_price(abbr: str) -> None:
    companies, stocks = get_dicts()

    abbr = abbr.upper()
    try:
        company_name = list(companies.keys())[list(companies.values()).index(abbr)]
        price = stocks[abbr]
        print(company_name + ' ' + str(price))
    except ValueError:
        print('Unknown ticker')


def main():
    if len(sys.argv) != 2:
        return
    print_name_and_price(sys.argv[1])


if __name__ == '__main__':
    main()
