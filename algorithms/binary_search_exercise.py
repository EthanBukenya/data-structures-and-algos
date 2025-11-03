def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1


def binary_search_recurssive(numbers_list, number_to_find, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    mid_number = numbers_list[mid_index]

    if mid_number == number_to_find:
        return mid_index

    if mid_number < number_to_find:
        left_index = mid_number + 1
    else:
        right_index = mid_number + 1

    return binary_search_recurssive(numbers_list, number_to_find, left_index, right_index)


if __name__ == '__main__':
    # numbers_list = [1, 3, 5, 7, 9, 10]
    # number_to_find = 7
    # index = binary_search(numbers_list, number_to_find)

    # print(f"the mid number index is {index} ")

    numbers_list = [1, 3, 5, 7, 9, 10]
    number_to_find = 7
    index = binary_search_recurssive(
        numbers_list, number_to_find, 0, len(numbers_list))

    print(f"the mid number index is {index} ")
