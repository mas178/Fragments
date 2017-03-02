"""
Non-unique Elements
https://py.checkio.org/mission/non-unique-elements/
"""


def checkio(data: list) -> list:
    return [x for x in data if data.count(x) > 1]


def checkio2(data: list) -> list:
    result = []
    for x in data:
        if data.count(x) > 1:
            result.append(x)

    return result


if __name__ == "__main__":
    assert isinstance(checkio([1]), list), "The result must be a list"
    assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
    assert checkio([1, 2, 3, 4, 5]) == [], "2nd example"
    assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
    assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"
    assert isinstance(checkio2([1]), list), "The result must be a list"
    assert checkio2([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
    assert checkio2([1, 2, 3, 4, 5]) == [], "2nd example"
    assert checkio2([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
    assert checkio2([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"
