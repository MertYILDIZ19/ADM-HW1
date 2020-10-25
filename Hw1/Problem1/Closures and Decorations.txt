###############   Standardize Mobile Number Using Decorators   ################

def wrapper(f):
    def fun(l):
        # complete the function
        
        Phone_Numbers = []
        for i in l:
            if len(i) == 12:
                Phone_Numbers.append(("+91 " + i[2:7] + " " + i[7:]))
            elif len(i) == 11:
                Phone_Numbers.append(("+91 " + i[1:6] + " " + i[6:]))
            elif len(i) == 10:
                Phone_Numbers.append(("+91 " + i[:5] + " " + i[5:]))
            else:
                Phone_Numbers.append((i[:3] + " " + i[3:8] + " " + i[8:]))

        f(Phone_Numbers)

    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


###############   Decorators 2 - Name Directory  ################

import operator

def person_lister(f):
    def inner(people):
        # complete the function

        for i in sorted(people, key=lambda x: int(x[2])):
            yield f(i)

    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')