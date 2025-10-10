# Big O notation
# This the measurement of how running time and space requirement complexity of an algorithm grows as as imput size increases.
# we usually assume the worst case senario to be solved, ie searching for a number at the end of the last indexes in list

# data structures
# These are containers storing data in a specific memory layout

# Arrays ara data structures were elements are stored in a contiguous memory location.
# A dictionary is a Hash Table/Map that stores data using a key and value format and it's complexity is order of 1 ie O(1) since searching through is a constant.
# it uses a key on which You apply a hash function to access a specific memory address that is connected to a given element.

# Algorithm
# This is a set of programmed instructions to accomplish a task

# Big O examples
''' def foo(arr) size(arr) -> 100 : 0.23 milliseconds
                           -> 1000: 2.30 milliseconds  
                          Note: time ideally depends on how fast or slow your computer is!

    so big O notation is a mathematical notation for measuring time independent of the computer hardware
        time = a*n + b

        1: keep the fastest growing term
        time = a*n

        2: drop the constants
        time = n

        = O(n) , Therefore the Big O time Complexity is Order of n
        
 '''


# real life example for an order of n program
# a program returning the squared numbers in a list
# Time grows linearlly as input size increases
# returns: [4, 9, 16, 25]
''' 
def squared_numbers(numbers):
    square_numbers = []
    for number in numbers:
        square_numbers.append(number*number)
    return square_numbers


numbers = [2, 3, 4, 5]
print(squared_numbers(numbers))

'''
# Order of 1 or O(1) time complexity example
# time = a * n + b
'''
def find_first_pe(prices, eps, index):
    pe= prices[index]/eps[index]
    return pe
'''

# Order of n^2 time complexity
# time = a * n^2 + b
''' 
numbers = [1, 4, 7, 3, 5, 3, 6, 7, 8, 9, 10]

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] == numbers[j]:
            print("the duplicates are ", numbers[i])
            break
'''
# finding position of a number 77 in a list
# the simple primitive approach O(n)
# because it uses n number of iterations yet binary search takes 3 iterations thus O(log n)
# incase if in interview: O(n) seems slow, can you optimize O(log n)
numbers = [1, 3, 7, 2, 5, 77, 9, 0, 10]
numbers.sort()
print(numbers)

for i in range(len(numbers)):
    if numbers[i] == 77:
        print(i)

# binary search calculations
# first divides the sorted list into half
''' 
iteration k = n/2^k
          1 = n/2^k
          k = n/2
     log2 n = log2 2^k   
     log2 n = k * log2 2
          k = log n  -> O(log n)

'''
