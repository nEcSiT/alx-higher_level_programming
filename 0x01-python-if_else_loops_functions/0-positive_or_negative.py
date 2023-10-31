#!/usr/bin/python3
import random
number = random.randint(-10, 10)

# Cheecking the codition if the number is positive
    if number > 0:
         print(f'{number} is positive')

# Cheecking the codition if the number is 0
    elif number == 0:
         print(f'{number} is zero')

# Cheecking the codition if the number is negative
    else:
         print(f'{number} is negative')

# Printing a newline
print()
