import pytest

from sys import argv, exit
from bs4 import BeautifulSoup
from requests import get
from time import sleep


class YahooFinanceScrapper:
    def __init__(self, ticker_symbol: str) -> None:
        self.ticker_symbol = ticker_symbol
        self.base_url = 'http://finance.yahoo.com/quote/{}/financials'
        self.page = None

    def set_ticker(self, ticker_symbol: str) -> None:
        self.ticker_symbol = ticker_symbol

    def request_page(self) -> int:
        self.page = get(self.base_url.format(self.ticker_symbol),
                        headers={'User-Agent': 'Custom'})
        return self.page.status_code

    def get_row(self, row_name: str, update_request=False) -> tuple:
        if self.page is None or update_request:
            self.request_page()
        if self.page.status_code != 200:
            raise RuntimeError(f'Request was failed with status code {self.page.status_code})')

        soup = BeautifulSoup(self.page.text, features='html.parser')
        if soup.find('section', attrs={'id': 'lookup-page'}) is not None:
            raise RuntimeError('Such page does not exist')

        values_row = []
        all_rows = soup.findAll('div', attrs={'data-test': 'fin-row'})
        for row in all_rows:
            if row.find('span', text=row_name, attrs={'class': 'Va(m)'}) is not None:
                all_cols = row.findAll('div', attrs={'data-test': 'fin-col'})
                for col in all_cols:
                    values_row.append(col.text)

        if len(values_row) == 0:
            raise RuntimeError(f'Such field ({row_name}) does not exist')

        return row_name, *values_row


# TESTS


def test_request_success():
    scrapper = YahooFinanceScrapper('aapl')
    assert scrapper.request_page() == 200


def test_request_fail():
    scrapper = YahooFinanceScrapper('asdkjasjdlkasjduh')
    assert scrapper.request_page() != 200


def test_request_type():
    scrapper = YahooFinanceScrapper('aapl')
    assert type(scrapper.request_page()) is int


def test_get_row_success_1():
    scrapper = YahooFinanceScrapper('aapl')
    assert scrapper.get_row('Total Revenue')[0] == 'Total Revenue'


def test_get_row_success_2():
    scrapper = YahooFinanceScrapper('aapl')
    assert scrapper.get_row('Gross Profit')[0] == 'Gross Profit'


def test_get_row_fail_1():
    scrapper = YahooFinanceScrapper('sdfasd')
    with pytest.raises(RuntimeError):
        scrapper.get_row('')


def test_get_row_fail_2():
    scrapper = YahooFinanceScrapper('aapl')
    with pytest.raises(RuntimeError):
        scrapper.get_row('sdfmsldhfjk')


def test_get_row_type():
    scrapper = YahooFinanceScrapper('aapl')
    assert type(scrapper.get_row('Total Revenue')) is tuple


if __name__ == '__main__':
    test_request_success()
    test_request_success()
    test_request_type()

    test_get_row_success_1()
    test_get_row_success_2()
    test_get_row_fail_1()
    test_get_row_fail_2()
    test_get_row_type()