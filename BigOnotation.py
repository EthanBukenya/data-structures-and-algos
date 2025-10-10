# Big O notation
# This the measurement of how running time and space requirement complexity of an algorithm grows as as imput size increases.

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
