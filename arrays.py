# Arrays are data structures where elements are stored in a contiguous memory allocation
# stock prices for 5 days
# the Big O complexity for looking up an elent by index is O(1)
stock_prices = [230, 502, 300, 250, 120, 111]

day_one = stock_prices[0]
day_three = stock_prices[2]
print(f"stock prices on day three is : {day_three}")

# on what day was price 120
# Big o time complexity for searching the day is O(n)
# for traversal to display all elements in the list is O(n)
for i in range(len(stock_prices)):
    if stock_prices[i] == 120:
        print(f"on day : {i + 1}")


# insert price at a give index O(n)
stock_prices.insert(2, 777)
print(stock_prices)
