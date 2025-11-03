# binary search algorithm implementation
# linear search is O(n) while binary search is O(log n) since the list is divided into 2 for evry iteration

# transactions = [{
#     'name': 'Ethan',
#     'device_id': 'ldw47',
#     'amount': '1200'
# },
#     {
#     'name': 'liberty',
#     'device_id': 'Tvw743',
#     'amount': '1407'
# },
#     {
#     'name': 'Bukenya',
#     'device_id': 'dmx300',
#     'amount': '800'
# }]


# def find_transaction(transactions):
#     for index, element in enumerate(transactions):
#         if element['device_id'] == 'ldw47':
#             return index
#     return -1

# def linear_search(numbers_list, number_to_find):
#     for index, element in enumerate(numbers_list):
#         if element == number_to_find:
#             return index
#     return 'infinity'


# if __name__ == '__main__':

#     numbers_list = [2, 4, 5, 6, 7, 10]
#     number_to_find = 79
#     index = linear_search(numbers_list, number_to_find)

#     print(f"found number at index : {index}")


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


if __name__ == '__main__':

    numbers_list = [2, 4, 5, 6, 7, 10]
    number_to_find = 79
    index = binary_search(numbers_list, number_to_find)

    print(f"found number at index : {index}")
