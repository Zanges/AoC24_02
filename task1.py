from typing import List

INPUT_FILE = "input.txt"


def load(filename: str) -> list[list[str]]:
    """
    Load the data from the file

    :param filename: the name of the file

    :return:
    """
    with open(filename, "r") as fileobj:
        return [line.strip().split() for line in fileobj]


def dummy_data() -> list[list[str]]:
    """
    7 6 4 2 1
    1 2 7 8 9
    9 7 6 2 1
    1 3 2 4 5
    8 6 4 4 1
    1 3 6 7 9
    """
    return [
        ["7", "6", "4", "2", "1"],
        ["1", "2", "7", "8", "9"],
        ["9", "7", "6", "2", "1"],
        ["1", "3", "2", "4", "5"],
        ["8", "6", "4", "4", "1"],
        ["1", "3", "6", "7", "9"],
    ]


def transform(data: list[list[str]]) -> list[list[int]]:
    """
    Transform the data from string to int
    """
    return [[int(x) for x in row] for row in data]


def is_valid(data: list[int]) -> bool:
    """
    Check if the data is valid

    :param data: the data to check

    :return: True if the data is valid, False otherwise
    """
    valid = True
    for criteria in CRITERIAS:
        valid = valid and criteria(data)
    return valid


def fulfills_criteria1(data: list[int]) -> bool:
    """
    Check if the data fulfills criteria 1
    The levels are either all increasing or all decreasing

    :param data: the data to check

    :return: True if the data fulfills the criteria, False otherwise
    """
    increasing = True
    decreasing = True
    for i in range(1, len(data)):
        if data[i] > data[i - 1]:
            decreasing = False
        elif data[i] < data[i - 1]:
            increasing = False
    return increasing or decreasing


def fulfills_criteria2(data: list[int]) -> bool:
    """
    Check if the data fulfills criteria 2
    Any two adjacent levels differ by at least one and at most three.

    :param data: the data to check

    :return: True if the data fulfills the criteria, False otherwise
    """
    for i in range(1, len(data)):
        if abs(data[i] - data[i - 1]) < 1 or abs(data[i] - data[i - 1]) > 3:
            return False
    return True


CRITERIAS = [
    fulfills_criteria1,
    fulfills_criteria2
]


def count_valid(data: list[list[int]]) -> int:
    """
    Count the number of valid data

    :param data: the data to check

    :return: the number of valid data
    """
    return sum([is_valid(row) for row in data])


def main():
    data = load(INPUT_FILE)
    # data = dummy_data()
    data = transform(data)
    print(count_valid(data))


if __name__ == "__main__":
    main()