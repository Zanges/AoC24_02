from task1 import INPUT_FILE, load, dummy_data, transform, is_valid


def would_be_valid(data: list[int]) -> bool:
    """
    Check if the data would be valid if an element was removed

    :param data: the data to check

    :return: True if the data would be valid, False otherwise
    """
    if is_valid(data):
        return True
    for i in range(len(data)):
        new_list = data[:i] + data[i + 1:]
        print(new_list)
        if is_valid(new_list):
            return True


def sum_valid(data: list[list[int]]) -> int:
    """
    Count the number of valid data

    :param data: the data to check

    :return: the number of valid data
    """
    valid = 0
    for row in data:
        if would_be_valid(row):
            valid += 1
    return valid


def main():
    data = load(INPUT_FILE)
    # data = dummy_data()
    data = transform(data)
    print(data)
    print(sum_valid(data))


if __name__ == '__main__':
    main()