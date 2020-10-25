###############   Calendar Module   ################

# Enter your code here. Read input from STDIN. Print output to STDOUT

import datetime
import calendar
Date = list(map(int, raw_input().split(' ')))
Day = datetime.datetime(Date[2], Date[0], Date[1])
print(calendar.day_name[Day.weekday()].upper())

###############   Time Delta   ################

#!/bin/python3

import math
import os
import random
import re
import sys
import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):

    return str(int(abs((datetime.datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z') - datetime.datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')).total_seconds())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
