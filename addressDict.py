import sys

storeAddressDict = {
    'ASAP General Store #101': {'Address': '1401 N Airport Road',
                                '/City': 'Weatherford',
                                '/State': 'Oklahoma',
                                '/Phone': '580-772-5618'
                                },
    'ASAP General Store #102': {'Address': '1401 N Airport Road',
                                '/City': 'Weatherford',
                                '/State': 'Oklahoma',
                                '/Phone': '580-772-5618'
                                },
    'ASAP General Store #103': {'Address': '1401 N Airport Road',
                                '/City': 'Weatherford',
                                '/State': 'Oklahoma',
                                '/Phone': '580-772-5618'
                                },
    'ASAP General Store #104': {'Address': '1401 N Airport Road',
                                '/City': 'Weatherford',
                                '/State': 'Oklahoma',
                                '/Phone': '580-772-5618'
                                },
    'ASAP General Store #300': {'Address': '1401 N Airport Road',
                                '/City': 'Weatherford',
                                '/State': 'Oklahoma',
                                '/Phone': '580-772-5618'
                                },
    'ASAP General Store #301': {'Address': '1401 N Airport Road',
                                '/City': 'Weatherford',
                                '/State': 'Oklahoma',
                                '/Phone': '580-772-5618'
                                },
    'ASAP General Store #302': {'Address': '1401 N Airport Road',
                                '/City': 'Weatherford',
                                '/State': 'Oklahoma',
                                '/Phone': '580-772-5618'
                                },
    'ASAP General Store #304': {'Address': '1401 N Airport Road',
                                '/City': 'Weatherford',
                                '/State': 'Oklahoma',
                                '/Phone': '580-772-5618'
                                },
    'ASAP General Store #307': {'Address': '1401 N Airport Road',
                                '/City': 'Weatherford',
                                '/State': 'Oklahoma',
                                '/Phone': '580-772-5618'
                                },
    'ASAP General Store #308': {'Address': '1401 N Airport Road',
                                '/City': 'Weatherford',
                                '/State': 'Oklahoma',
                                '/Phone': '580-772-5618'
                                },
    'ASAP General Store #310': {'Address': '1401 N Airport Road',
                                '/City': 'Weatherford',
                                '/State': 'Oklahoma',
                                '/Phone': '580-772-5618'
                                },
    'ASAP General Store #311': {'Address': '1401 N Airport Road',
                                '/City': 'Weatherford',
                                '/State': 'Oklahoma',
                                '/Phone': '580-772-5618'
                                },
    'ASAP General Store #313': {'Address': '1401 N Airport Road',
                                '/City': 'Weatherford',
                                '/State': 'Oklahoma',
                                '/Phone': '580-772-5618'
                                },
    'ASAP General Store #314': {'Address': '1401 N Airport Road',
                                '/City': 'Weatherford',
                                '/State': 'Oklahoma',
                                '/Phone': '580-772-5618'
                                },
    'ASAP General Store #322': {'Address': '1401 N Airport Road',
                                '/City': 'Weatherford',
                                '/State': 'Oklahoma',
                                '/Phone': '580-772-5618'
                                },
    'ASAP General Store #330': {'Address': '1401 N Airport Road',
                                '/City': 'Weatherford',
                                '/State': 'Oklahoma',
                                '/Phone': '580-772-5618'
                                },
    'ASAP General Store #332': {'Address': '1401 N Airport Road',
                                '/City': 'Weatherford',
                                '/State': 'Oklahoma',
                                '/Phone': '580-772-5618'
                                },
    'Hydro Fuel Island': {'Address': '1401 N Airport Road',
                          '/City': 'Weatherford',
                          '/State': 'Oklahoma',
                          '/Phone': '580-772-5618'
                          },
}


def formatAddressDict(location: str) -> str:
    # Takes a location number and returns formtted k, v, pairs.
    locationAddress = str(storeAddressDict[location])
    title = str(f'{location}:\n\n')
    return f'{title}{locationAddress}'
