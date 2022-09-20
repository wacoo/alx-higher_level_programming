#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
strr = repr(number)
dig = int(strr[-1])
if dig > 5:
    print("Last digit of", number, 'is', dig, 'and is greater than 5')
elif dig == 0:
    print("Last digit of", number, 'is', dig, 'and is 0')
else:
    print("Last digit of", number, 'is', dig, 'and is less than 6 and not 0')
