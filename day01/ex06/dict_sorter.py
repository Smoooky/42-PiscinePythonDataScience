def get_dict() -> dict:
    country_codes = {
        'Russia': '25',
        'France': '132',
        'Germany': '132',
        'Spain': '178',
        'Italy': '162',
        'Portugal': '17',
        'Finland': '3',
        'Hungary': '2',
        'The Netherlands': '28',
        'The USA': '610',
        'The United Kingdom': '95',
        'China': '83',
        'Iran': '76',
        'Turkey': '65',
        'Belgium': '34',
        'Canada': '28',
        'Switzerland': '26',
        'Brazil': '25',
        'Austria': '14',
        'Israel': '12'
    }
    return  country_codes


def sort_dict(country_codes: dict) -> dict:
    return dict(sorted(country_codes.items(), key=lambda item: (-int(item[1]), item[0])))


def main():
    print_dict()


if __name__ == '__main__':
    main()
