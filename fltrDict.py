import sys

fltrListDict = {
    'ASAP General Store #101': {"CIM-TEK 10mic 70015": 2,
                                "/CIM-TEK 30mic 70016": 0,
                                "/CIM-TEK 30mic 70020": 12,
                                "/CIM-TEK 30mic 70092": 2,
                                "/CIM-TEK 10mic 70097": 10
                                },
    'ASAP General Store #102': {"CIM-TEK 10mic Gas 70015": 0,
                                "/CIM-TEK 30mic Dsl 70016": 1,
                                "/CIM-TEK 30mic Dsl 70020": 0,
                                "/CIM-TEK 30mic Dsl 70092": 3,
                                "/CIM-TEK 10mic Gas 70097": 12
                                },
    'ASAP General Store #103': {"CIM-TEK 10mic Gas 70015": 0,
                                "/CIM-TEK 30mic Dsl 70016": 0,
                                "/CIM-TEK 30mic Dsl 70020": 0,
                                "/CIM-TEK 30mic Dsl 70092": 4,
                                "/CIM-TEK 10mic Gas 70097": 12
                                },
    'ASAP General Store #104': {"CIM-TEK 10mic Gas 70015": 1,
                                "/CIM-TEK 30mic Dsl 70016": 1,
                                "/CIM-TEK 30mic Dsl 70020": 6,
                                "/CIM-TEK 30mic Dsl 70092": 3,
                                "/CIM-TEK 10mic Gas 70097": 11
                                },
    'ASAP General Store #300': {"CIM-TEK 10mic Gas 70015": 0,
                                "/CIM-TEK 30mic Dsl 70016": 0,
                                "/CIM-TEK 30mic Dsl 70020": 6,
                                "/CIM-TEK 30mic Dsl 70092": 1,
                                "/CIM-TEK 10mic Gas 70097": 6
                                },
    'ASAP General Store #301': {"CIM-TEK 10mic Gas 70015": 0,
                                "/CIM-TEK 30mic Dsl 70016": 0,
                                "/CIM-TEK 30mic Dsl 70020": 5,
                                "/CIM-TEK 30mic Dsl 70092": 0,
                                "/CIM-TEK 10mic Gas 70097": 4
                                },
    'ASAP General Store #302': {"CIM-TEK 10mic Gas 70015": 7,
                                "/CIM-TEK 30mic Dsl 70016": 0,
                                "/CIM-TEK 30mic Dsl 70020": 12,
                                "/CIM-TEK 30mic Dsl 70092": 0,
                                "/CIM-TEK 10mic Gas 70097": 0
                                },
    'ASAP General Store #304': {"CIM-TEK 10mic Gas 70015": 3,
                                "/CIM-TEK 30mic Dsl 70016": 0,
                                "/CIM-TEK 30mic Dsl 70020": 8,
                                "/CIM-TEK 30mic Dsl 70092": 0,
                                "/CIM-TEK 10mic Gas 70097": 2
                                },
    'ASAP General Store #307': {"CIM-TEK 10mic Gas 70015": 0,
                                "/CIM-TEK 30mic Dsl 70016": 0,
                                "/CIM-TEK 30mic Dsl 70020": 0,
                                "/CIM-TEK 30mic Dsl 70092": 2,
                                "/CIM-TEK 10mic Gas 70097": 24
                                },
    'ASAP General Store #308': {"CIM-TEK 10mic Gas 70015": 0,
                                "/CIM-TEK 30mic Dsl 70016": 0,
                                "/CIM-TEK 30mic Dsl 70020": 6,
                                "/CIM-TEK 30mic Dsl 70092": 4,
                                "/CIM-TEK 10mic Gas 70097": 12
                                },
    'ASAP General Store #310': {"CIM-TEK 10mic Gas 70015": 8,
                                "/CIM-TEK 30mic Dsl 70016": 4,
                                "/CIM-TEK 30mic Dsl 70020": 0,
                                "/CIM-TEK 30mic Dsl 70092": 0,
                                "/CIM-TEK 10mic Gas 70097": 0
                                },
    'ASAP General Store #311': {"CIM-TEK 10mic Gas 70015": 1,
                                "/CIM-TEK 30mic Dsl 70016": 0,
                                "/CIM-TEK 30mic Dsl 70020": 0,
                                "/CIM-TEK 30mic Dsl 70092": 8,
                                "/CIM-TEK 10mic Gas 70097": 23
                                },
    'ASAP General Store #313': {"CIM-TEK 10mic Gas 70015": 12,
                                "/CIM-TEK 30mic Dsl 70016": 0,
                                "/CIM-TEK 30mic Dsl 70020": 10,
                                "/CIM-TEK 30mic Dsl 70092": 4,
                                "/CIM-TEK 10mic Gas 70097": 0
                                },
    'ASAP General Store #314': {"CIM-TEK 10mic Gas 70015": 0,
                                "/CIM-TEK 30mic Dsl 70016": 0,
                                "/CIM-TEK 30mic Dsl 70020": 8,
                                "/CIM-TEK 30mic Dsl 70092": 4,
                                "/CIM-TEK 10mic Gas 70097": 12
                                },
    'ASAP General Store #322': {"CIM-TEK 10mic Gas 70015": 0,
                                "/CIM-TEK 30mic Dsl 70016": 0,
                                "/CIM-TEK 30mic Dsl 70020": 6,
                                "/CIM-TEK 30mic Dsl 70092": 4,
                                "/CIM-TEK 10mic Gas 70097": 12
                                },
    'ASAP General Store #330': {"CIM-TEK 10mic Gas 70015": 0,
                                "/CIM-TEK 30mic Dsl 70016": 0,
                                "/CIM-TEK 30mic Dsl 70020": 8,
                                "/CIM-TEK 30mic Dsl 70092": 4,
                                "/CIM-TEK 10mic Gas 70097": 13
                                },
    'ASAP General Store #332': {"CIM-TEK 10mic Gas 70015": 15,
                                "/CIM-TEK 30mic Dsl 70016": 5,
                                "/CIM-TEK 30mic Dsl 70020": 14,
                                "/CIM-TEK 30mic Dsl 70092": 0,
                                "/CIM-TEK 10mic Gas 70097": 0
                                },
    'Hydro Fuel Island': {"CIM-TEK 10mic Gas 70015": 0,
                          "/CIM-TEK 30mic Dsl 70016": 0,
                          "/CIM-TEK 30mic Dsl 70020": 4,
                          "/CIM-TEK 30mic Dsl 70092": 0,
                          "/CIM-TEK 10mic Gas 70097": 4
                          },
}


def scrubDict(dictionary: dict()) -> str:
    # Removes unnessesary characters from a dict casted to str.
    scrubbedDict = str(dictionary).replace(
        "{", "").replace(
        "}", "").replace(
        "'", "").replace(
        ",", "").replace(
        "/", "\n"
    )
    return scrubbedDict


def formatFilterDict(location: int) -> str:
    # Takes a location number and returns formtted k, v, pairs.
    locationFilters = str(fltrListDict[location])
    title = str(f'{location}\nFilter List:\n\n')
    return f'{title}{locationFilters}'


if __name__ == '__main__':

    formatFilterDict('ASAP General Store #101')
    print(fltrListDict['ASAP General Store #101']['CIM-TEK 10mic Gas 70015'])
