# # Arrays are data structures where elements are stored in a contiguous memory allocation
# # stock prices for 5 days
# # the Big O complexity for looking up an elent by index is O(1)
# '''
# stock_prices = [230, 502, 300, 250, 120, 111]

# day_one = stock_prices[0]
# day_three = stock_prices[2]
# print(f"stock prices on day three is : {day_three}")

# # on what day was price 120
# # Big o time complexity for searching the day is O(n)
# # for traversal to display all elements in the list is O(n)
# for i in range(len(stock_prices)):
#     if stock_prices[i] == 120:
#         print(f"on day : {i + 1}")


# # insert price at a give index O(n)
# stock_prices.insert(2, 777)
# print(stock_prices)
# '''

# # Exercise: Array DataStructure
# # Let us say your expense for every month are listed below,
# # January - 2200
# # February - 2350
# # March - 2600
# # April - 2130
# # May - 2190
# # Create a list to store these monthly expenses and using that find out,

# # 1. In Feb, how many dollars you spent extra compared to January?

# # solution:
# monthly_expenses = [2200, 2350, 2600, 2130, 2190]
# Jan = monthly_expenses[0]
# Feb = monthly_expenses[1]
# Mar = monthly_expenses[2]
# Apr = monthly_expenses[3]
# May = monthly_expenses[4]


# extra_spent = Feb - Jan
# print(f"Extra dollars spent in feb compared to Jan is $ {extra_spent} ")


# # 2. Find out your total expense in first quarter (first three months) of the year.

# first_quater_total = Jan + Feb + Mar
# print(f"first quater total expense is $ {first_quater_total}")


# # 3. Find out if you spent exactly 2000 dollars in any month
# for i in monthly_expenses:
#     if i == 2000:
#         print(f"the month with 2000 dollars spent is {i}")
# else:
#     print("there's no month with that expense")

# # prefered soln: print("Did I spent 2000$ in any month? ", 2000 in monthly_expenses) # False

# # 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# monthly_expenses.append(1980)
# print(monthly_expenses)

# # 5. You returned an item that you bought in a month of April and
# # got a refund of 200$. Make a correction to your monthly expense list
# # based on this

# monthly_expenses[3] -= 200
# print(f"The monthly expense list with $200 correction is {monthly_expenses}")
# print(Apr - 200)

# 2: You have a list of your favourite marvel super heros.
# heros=['spider man','thor','hulk','iron man','captain america']
# Using this find out,
''' 
1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
Solution

'''

# 3: Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
stocks = []

stocks.append(10)
stocks.append(11)
stocks.append(12)
stocks.append(13)
stocks.append(14)

stocks.insert(1, 111)
print(stocks)
