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


def is_company(raw: str, companies: dict) -> bool:
    name = raw.lower().capitalize()
    if name in companies:
        print(name + ' stock price is ' + companies[name])
        return True
    return False


def is_ticker(raw: str, stocks: dict) -> bool:
    ticker = raw.upper()
    if ticker in stocks:
        print(ticker + ' is a ticker symbol for ' + str(stocks[ticker]))
        return True
    return False


def split_input(input_string: str) -> list:
    return input_string.replace(' ', '').split(',')


def main():
    if len(sys.argv) != 2:
        return
    companies, stocks = get_dicts()
    raw_list = split_input(sys.argv[1])
    for raw_string in raw_list:
        if raw_string == '' or raw_string == ' ':
            return
    for raw_string in raw_list:
        if is_ticker(raw_string, stocks):
            continue
        elif is_company(raw_string, companies):
            continue
        else:
            print(raw_string + ' is unknown company or an unknown ticker symbol')



if __name__ == '__main__':
    main()