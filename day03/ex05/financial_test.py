import requests, sys, pytest
from bs4 import BeautifulSoup


def test_parse_ticker():
    res = parse('MSFT', 'Total Revenue')
    assert res[0] == 'Total Revenue'


def test_parse_tuple():
    res = parse('MSFT', 'Total Revenue')
    assert type(res) == tuple


def test_parse_url():
    try:
        parse('MSweFT', 'Total Revenue')
        assert False
    except ConnectionError:
        assert True


def main(ticker, table):
    test_parse_url()
    test_parse_tuple()
    test_parse_ticker()
    res = parse(ticker, table)
    if res:
        print(res)


def parse(ticker, table):
    ticker = ticker
    table = table
    url = f'https://finance.yahoo.com/quote/{ticker}/financials?p={ticker}'
    try:
        response = requests.get(url, headers={
            'User-Agent': 'Custom'})
    except requests.exceptions.ConnectionError as e:
        print('Error: {}'.format(e))
        return None
    soup = BeautifulSoup(response.text, "html.parser")
    finance = soup.find_all('div', class_='fi-row')
    if not finance:
        raise ConnectionError
    tab = {}
    for elem in finance:
        try:
            title = elem.find('div', class_='Va(m)').text
            lst = []
            fin_value = elem.find_all('div', class_='Ta(c)')
            for item in fin_value:
                lst.append(item.text)
            tab[title] = lst
        except Exception as e:
            continue
    try:
        return tuple([table, *tab[table]])
    except KeyError as e:
        print('Error: {}'.format(e))
        return None


if __name__ == '__main__':

    try:
        if len(sys.argv) == 3:
            main(sys.argv[1], sys.argv[2])
        else:
            raise ValueError('Count of arg')
    except ValueError as e:
        print('Exception:', e)