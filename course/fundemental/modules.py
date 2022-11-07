# Modules
# F-Strings
# Literal String Interpolation (commonly as f-strings)
# Reason for the name: (because of the leading f character preceding the string literal)
# Source: https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/

import calendar
import random
import math


# Calendar
#--------------------------------------
calendar = calendar.month(1209,9)
print (calendar)


# Random
#--------------------------------------
#random.int
random_num = random.randint(1,1000)
print (f"Random Number is {random_num}")

movies = ['Matrix', 'Fight Club', 'John Wick', 'Cloud Atlas', 'Before Sunset']

print (f"Current Movie List...\n{movies}\n\n")

# random.choice
print (f"Random Movie is....{random.choice(movies)}\n\n")


# Math
#--------------------------------------

# math.sqrt
print (f"Square root of {random_num} is {math.sqrt(random_num)}\n\n")

# math.pow
# Return the value of 9 raised to the power of 3
any_num = 3
print (f"{random_num} raised to the power of {any_num} ... { math.pow(random_num, any_num) }")