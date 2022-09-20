#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
strr = repr(number)
dig = int(strr[-1])
if number < 0:
    dig = dig * -1
print(f"Last digit of {number} is {dig} and is ", end='')
if dig > 5:
    print("greater than 5")
elif dig == 0:
    print("and is 0")
else:
    print("less than 6 and not 0")
