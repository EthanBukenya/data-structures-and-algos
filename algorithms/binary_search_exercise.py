# def binary_search(numbers_list, number_to_find):
#     left_index = 0
#     right_index = len(numbers_list) - 1
#     mid_index = 0

#     while left_index <= right_index:
#         mid_index = (left_index + right_index) // 2
#         mid_number = numbers_list[mid_index]

#         if mid_number == number_to_find:
#             return mid_index

#         if mid_number < number_to_find:
#             left_index = mid_index + 1
#         else:
#             right_index = mid_index - 1

#     return -1


# def binary_search_recurssive(numbers_list, number_to_find, left_index, right_index):
#     if right_index < left_index:
#         return -1

#     mid_index = (left_index + right_index) // 2
#     mid_number = numbers_list[mid_index]

#     if mid_number == number_to_find:
#         return mid_index

#     if mid_number < number_to_find:
#         left_index = mid_number + 1
#     else:
#         right_index = mid_number - 1

#     return binary_search_recurssive(numbers_list, number_to_find, left_index, right_index)


# def find_all_occurances(numbers, number_to_find):
#     index = binary_search(numbers, number_to_find)
#     indices = [index]

#     i = index-1
#     while i >= 0:
#         if numbers[i] == number_to_find:
#             indices.append(i)
#         else:
#             break
#         i = i - 1

#         i = index + 1
#     while i <= len(numbers):
#         if numbers[i] == number_to_find:
#             indices.append(i)
#         else:
#             break
#         i = i + 1

#     return sorted(indices)


# if __name__ == '__main__':
#     # numbers_list = [1, 3, 5, 7, 9, 10]
#     # number_to_find = 7
#     # index = binary_search(numbers_list, number_to_find)

#     # print(f"the mid number index is {index} ")

#     numbers_list = [1, 3, 5, 7, 9, 10]
#     number_to_find = 7
#     index = binary_search_recurssive(
#         numbers_list, number_to_find, 0, len(numbers_list))

#     print(f"the mid number index is {index} ")

#     numbers = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
#     number_to_find = 15
#     indices = find_all_occurances(numbers, number_to_find)
#     print(f"Indices of occurances of {number_to_find} are {indices}")


def binary_search(number_list, number_to_find):
    left_index = 0
    right_index = len(number_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (right_index + left_index) // 2
        mid_number = number_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1


def binary_search_recursive(number_list, number_to_find, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    mid_number = number_list[mid_index]

    if mid_number == number_to_find:
        return mid_index

    if mid_number <= number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_search_recursive(number_list, number_to_find, left_index, right_index)


if __name__ == '__main__':
    numbers_list = [1, 4, 5, 7, 8]
    number_to_find = 7

    # print(binary_search(numbers_list, number_to_find))
    print(binary_search_recursive(numbers_list,
          number_to_find, 0, len(numbers_list)))
