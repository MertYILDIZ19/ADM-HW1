###############   Detect Floating Point Number   ################

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
N=int(input())

for _ in range(N):
     print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', input())))


###############   Re.split()   ################

regex_pattern = r"[.,]+"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))


###############   Group(), Groups() & Groupdict()   ################

# Enter your code here. Read input from STDIN. Print output to STDOUT

N = input()
for i in range(len(N)-1):
    if N[i] ==N[i+1] and N[i].isalnum():
        print(N[i])
        break
    elif i<len(N)-2:
        continue
    else:
        print(-1)


###############   Re.findall() & Re.finditer()   ################

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

S = '[qwrtypsdfghjklzxcvbnm]'
a = re.findall('(?<=' + S +')([aeiou]{2,})' + S, input(), re.I)
print('\n'.join(a or ['-1']))



###############   Re.start() & Re.end()   ################

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

Str1 = input()
Str2 = input()

SubStr = re.compile(Str2)
S = SubStr.search(Str1)
if not S: print( "(-1, -1)")

L=[m.start() for m in re.finditer('(?='+Str2+')', Str1)]
for i in L:
    print((i,i+len(Str2)-1))


###############    Regex Substitution    ################

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

S = int(input())
for i in range(S):
      Patt1=re.compile(R'(?<= )(&&)(?= )')
      Patt2=re.compile(R'(?<= )(\|\|)(?= )')
      print(Patt2.sub('or', Patt1.sub('and', input())))


###############   Validating Roman Numerals    ################

regex_pattern = r"M{0,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[VX]|V?I{0,3})$"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))


###############   Validating phone numbers   ################

# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())

for _ in range(N):
    Ph_Number = input()
    if len(Ph_Number)== 10 and Ph_Number.isnumeric() and Ph_Number[0] in "789":
        print("YES")
    else:
        print("NO")


###############    Validating and Parsing Email Addresses  ################

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

N=int(input())
for _ in range(N):
    Name, E_mail = input().split(" ")
    Form_email = E_mail[1:-1]
    pattern = re.compile(r'[a-zA-Z0-9+](\w|-|\.|_)+@[a-zA-Z]+\.[A-Za-z]{1,3}')
    if pattern.match(Form_email)!=None:
        if pattern.match(Form_email).group(0)==Form_email:
            print(Name, E_mail)


###############    Hex Color Code  ################

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
import sys

[print(j) for i in sys.stdin for j in re.findall('[\s:](#[a-f0-9]{6}|#[a-f0-9]{3})', i, re.I)]


###############    HTML Parser - Part 1  ################

# Enter your code here. Read input from STDIN. Print output to STDOUT

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def Handler_Factory(msg):
        msg = msg.ljust(6) + ':'
        def handler(self, tag, attrs=[]):
            print(msg, tag)
            for a in attrs:
                print("-> %s > %s" % a)
        return handler

    locals().update(zip(
        map("handle_{}tag".format, ("start", "end", "startend")),
        map(Handler_Factory, ("Start", "End", "Empty"))
    ))

MyHTMLParser().feed(' '.join(input() for _ in range(int(input()))))


###############    HTML Parser - Part 2  ################

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if "\n" not in data:
            print(">>> Single-line Comment")
            print(data, end="")
        else:
            print(">>> Multi-line Comment")
            print(data)

    def handle_data(self, data):
        if data != '\n':
            print(">>> Data")
            print(data)


html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()

###############    Detect HTML Tags, Attributes and Attribute Values  ################

# Enter your code here. Read input from STDIN. Print output to STDOUT

from html.parser import HTMLParser

class The_HTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for i in attrs:
            print("->", i[0], ">", i[1])

parser = The_HTMLParser()

for i in range(int(input())):
    parser.feed(input())

###############    Validating UID  ################

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

N=int(input())
for _ in range(N):
    S = input()
    print('Valid' if all([re.search(r, S) for r in [r'[A-Za-z0-9]{10}',r'([A-Z].*){2}',r'([0-9].*){3}']]) and not re.search(r'.*(.).*\1', S) else 'Invalid')


###############    Validating Credit Card Numbers  ################

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

N=int(input())

for i in range(N):
    Credit_Card = input()
    if re.match(r'^[456][0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}$',Credit_Card) and not re.search(r'([\d])\1\1\1', Credit_Card.replace("-",'')):
        print("Valid")
    else:
        print("Invalid")


###############    Validating Postal Codes  ################

regex_integer_in_range = r"_________"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"_________"	# Do not delete 'r'.

import re

print(bool(re.match(
    r'^'
    r'(?!.*(.).\1.*(.).\2)'
    r'(?!.*(.)(.)\3\4)'
    r'[1-9]\d{5}'
    r'$', input()
)))

import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)


###############    Matrix Script  ################

#!/bin/python3

import math
import os
import random
import re
import sys


import re
x,y = list(map(int,input().split()))
rows =[input() for i in range(x)]
text = "".join([row[i] for i in range(y) for row in rows])
text = re.sub('([A-Za-z1-9])[^A-Za-z1-9]+([A-Za-z1-9])', r'\1 \2', text)
text = re.sub('  ', ' ', text)
print(text)
