#!/usr/bin/python3

from os import environ

if __name__ == '__main__':
    print(f"Your current virtual env is {environ['VIRTUAL_ENV']}")
