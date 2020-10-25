print("Hello, World!")


###############    Python If-Else   ################

#!/bin/python

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
print ("Not Weird" if not n%2 and (n in range(2,6) or n>20) else "Weird")


###############    Arithmetic Operators  ################

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())

print('{0} \n{1} \n{2}'.format((a+b),(a-b),(a*b)))


###############    Python: Division  ################

from __future__ import division

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())

    print('{0} \n{1}'.format((a//b),(a/b)))


###############    Loops  ################

if __name__ == '__main__':
    n = int(raw_input())
    counter = 0;
    while  counter < n :
        print (counter**2)
        counter = counter + 1

###############    Write a function  ################

def is_leap(year):
    leap = False
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False
    
    return leap


###############    Print Function  ################

from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())
    for i in range(1, n+1):
        print(i, end="")
