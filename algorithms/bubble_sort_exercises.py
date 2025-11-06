def bubble_sort(elements):
    size = len(elements)
    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if elements[j] > elements[j+1]:
                temp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = temp
                swapped = True
        if not swapped:
            break


if __name__ == '__main__':
    numbers = [2, 1, 5, 0, 7, 3]
    bubble_sort(numbers)

    print(numbers)
