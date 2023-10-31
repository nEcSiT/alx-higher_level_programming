#!/usr/bin/python3
import random
number = random.randint(-10, 10)

# Cheecking the codition if the number is positive
if number > 0:
    print('{} is positive'.format(number))

# Cheecking the codition if the number is 0
elif number == 0:
     print('{} is zero'.format(number))

# Cheecking the codition if the number is negative
elif number < 0:
     print('{} is negative'.format(number))

# Printing a newline
print()
