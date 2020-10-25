###############   sWAP cASE   ################

def swap_case(s):
    result = ""
    for letter in s:
        if letter == letter.upper():
            result += letter.lower()
        else:
            result += letter.upper()
    return result

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result


###############   String Split and Join   ################

def split_and_join(line):
    x=line.split(" ") 
    x='-'.join(x)    
    return x
   
if __name__ == '__main__':
    line = raw_input()
    result = split_and_join(line)
    print result


###############   What's Your Name?   ################

def print_full_name(a, b):
    if(len(a) and len(b) < 11): print("Hello %s %s! You just delved into python." %(a,b))
    
if __name__ == '__main__':
    first_name = raw_input()
    last_name = raw_input()
    print_full_name(first_name, last_name)


###############   Mutations   ################

def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]

if __name__ == '__main__':
    s = raw_input()
    i, c = raw_input().split()
    s_new = mutate_string(s, int(i), c)
    print s_new


###############   String Validators   ################

if __name__ == '__main__':
    s = raw_input()
    t = type(s)
    for method in [t.isalnum, t.isalpha, t.isdigit, t.islower, t.isupper]:
        print any(method(c) for c in s)


###############   Text Allignmnet   ################

# Enter your code here. Read input from STDIN. Print output to STDOUT

thickness = int(input()) #This must be an odd number
c = 'H'

for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


###############   Text Wrap   ################

import textwrap

def wrap(string, max_width):
    for i in range(0,len(string)+1,max_width):
        result=string[i:i+max_width]
        if len(result)==max_width:
            print(result)
        else:
            return(result)
    return

if __name__ == '__main__':
    string, max_width = raw_input(), int(raw_input())
    result = wrap(string, max_width)
    print result


###############   Find A String   ################

def count_substring(string, sub_string):
    counter,sum = 0,0
    for _ in range(0, len(string)):
        if matcher(string[counter:(len(sub_string)+counter)], sub_string):
            sum = sum + 1
        counter=counter + 1
    return sum

def matcher(sliced_str, sub_string):
    return sliced_str == sub_string

if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count


###############   Designer Door Mat   ################

# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int,raw_input().split())
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))


###############   String Formatting   ################

def print_formatted(n):
    # your code goes here
    w = len("{0:b}".format(n))
    for i in range(1,n+1):
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=w))

if __name__ == '__main__':
    n = int(raw_input())
    print_formatted(n)


###############   Alphabet Rangoli   ################

def print_rangoli(size):
    # your code goes here
    mid = size-1
    import string
    line = ['-'] * (2 * size - 1)
    for i in range(mid, 0, -1):
        for j in range(size - i):
            left = line[mid - j]
            right = line[mid + j]
            line[mid - j] = line[mid + j] = string.ascii_lowercase[j + i]
        print( '-'.join(line))


    for i in range(0, mid):
        line = ['-'] * (2 * size - 1)
        for j in range(size - i-1,-1,-1):
            left = line[mid - j]
            right = line[mid + j]
            line[mid - j] = line[mid + j] = string.ascii_lowercase[j + i]
        print( '-'.join(line))
    line = ['-'] * (2 * size - 1)
    line[mid] = line[mid] = string.ascii_lowercase[mid]
    print('-'.join(line))

if __name__ == '__main__':
    n = int(raw_input())
    print_rangoli(n)


###############   Capitalize!   ################

#!/bin/python

import math
import os
import random
import re
import sys
import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    the_list = []
    passport_name =list(s.split(" "))
    for i in passport_name:
        the_list.append(i.capitalize())
    return (' '.join(the_list))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = raw_input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()


###############   The Minion Game   ################

def minion_game(string):
    # your code goes here
    vowel =['A','E','I','O','U']
    S=0
    K=0
    for i in range(len(string)):
        if string[i] in vowel:
            K+= len(string)-i
        else:
            S+=len(string)-i
    if S>K:
        print("Stuart"+" "+ "%d" % S)
    elif K>S:
        print("Kevin"+" "+'%d' % K)
    else:
        print("Draw")


if __name__ == '__main__':
    s = raw_input()
    minion_game(s)


###############   Merge the Tools!   ################

def merge_the_tools(string, k):
    # your code goes here
    from collections import OrderedDict
    strnew=[string[i:i + k] for i in range(0, len(string), k)]
    for i in strnew:
        print("".join(OrderedDict.fromkeys(i)))

if __name__ == '__main__':
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)
    