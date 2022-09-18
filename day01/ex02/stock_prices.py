#!/usr/bin/python3

import sys


def get_dict_by_name(name: str) -> dict:
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

    if name == 'companies':
        return COMPANIES
    elif name == 'stocks':
        return STOCKS
    else:
        return None


def get_abbreviation(name: str, companies: dict) -> str:
    try:
        return companies[name]
    except KeyError:
        return None


def get_stock_price(abbr: str, stocks: dict) -> float:
    return stocks[abbr]


def main():
    if len(sys.argv) != 2:
        return
    name = sys.argv[1].lower().capitalize()
    abbr = get_abbreviation(name, get_dict_by_name('companies'))
    if abbr is not None:
        print(get_stock_price(abbr, get_dict_by_name('stocks')))
    else:
        print('Unknown company')


if __name__ == '__main__':
    main()
