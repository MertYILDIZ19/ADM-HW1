###############   Zipped!   ################

# Enter your code here. Read input from STDIN. Print output to STDOUT

Inputs = list(map(int, input().split(" ")))

The_list = [list(map(float, input().split(" "))) for i in range(Inputs[1])]

for i in zip(*The_list):
    print(sum(i) / len(i))


###############    Input()  ################

# Enter your code here. Read input from STDIN. Print output to STDOUT

x, Px = map(int, raw_input().split(" "))

if eval(raw_input())==Px:
    print(True)
else: 
    print(False)


###############    ginortS ################

# Enter your code here. Read input from STDIN. Print output to STDOUT

lower=[]
upper=[]
even=[]
odd=[]
for i in input():
    if i.islower():
        lower.append(i)
    elif i.isupper():
        upper.append(i)
    elif int(i)%2!=0:
        odd.append(int(i))
    elif int(i)%2==0:
        even.append(int(i))

lower = "".join(sorted(lower))
upper = "".join(sorted(upper))
odd = "".join(map(str,sorted(odd)))
even = "".join(map(str,sorted(even)))

print(lower+upper+odd+even)