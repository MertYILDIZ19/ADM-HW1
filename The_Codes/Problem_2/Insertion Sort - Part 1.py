#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    The_target = arr[-1]
    Indx = n-2
    
    while (The_target < arr[Indx]) and (Indx >= 0):
        arr[Indx+1] = arr[Indx]
        print(' '.join(map(str, arr)))
        Indx -= 1
        
    arr[Indx+1] = The_target
    print(' '.join(map(str, arr)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
