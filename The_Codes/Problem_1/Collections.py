###############    collections.Counter()   ################

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter
Length_List = int(input())
Shoes_List = list(map(int, raw_input().split()))

Number_of_Sizes = Counter(Shoes_List)

Earning = 0
for i in (range(int(raw_input()))):
    Size ,Price  = list(map(int, raw_input().split()))

    if Number_of_Sizes[Size]:
        Earning += Price
        Number_of_Sizes[Size] -= 1

print(Earning)

###############    DefaultDict Tutorial   ################

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter
n, m = list(map(int, raw_input().split()))

List1 = [raw_input() for i in range(n) ]
List2 = [raw_input() for i in range(m) ]

for j in List2:
    if j in List1:
        print(" ".join(map(str ,[i+1 for i, x in enumerate(List1) if x == j])))
    else:
        print(-1)

###############    Collections.namedtuple()   ################

# Enter your code here. Read input from STDIN. Print output to STDOUT

n= int(input())
stu= list(input().split())
mark = stu.index("MARKS")
total = 0

for i in range(n):
    total +=int(list(input().split())[mark])
print(total/n)


###############    Collections.OrderedDict()   ################

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict

N = int(raw_input())
Ordered_List = OrderedDict()
for i in range(N):
    L_item = raw_input().split(' ')
    Price = int(L_item[-1])
    Item_name = " ".join(L_item[:-1])
    if Ordered_List.get(Item_name):
        Ordered_List[Item_name] += Price
    else:
        Ordered_List[Item_name] = Price

for i,v in Ordered_List.items():
    print i,v

###############    Word Order  ################

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

N = int(raw_input())
Words = [raw_input().strip() for _ in range(N)]
Counts = Counter(Words)

print len(Counts)

for Word in Words:
    Derp = Counts.pop(Word, None)
    if Derp == None:
        continue
    else:
        print Derp,

###############    Collections.deque()    ################

# Enter your code here. Read input from STDIN. Print output to STDOUT

n= int(input())
from collections import deque
d =deque()
for i in range(n):
    row = list(input().split())
    if row[0]=="append":
        d.append(int(row[1]))
    elif row[0]=="appendleft":
        d.appendleft(int(row[1]))
    elif row[0]=="pop":
        d.pop()
    elif row[0]=="popleft":
        d.popleft()

print(*[item for item in d])

###############    Company Logo  ################

# Enter your code here. Read input from STDIN. Print output to STDOUT

s = sorted(raw_input())
d = [(s.count(c), c) for c in set(s)]
for v, k in sorted(d, key=lambda x: (-x[0], x[1]))[:3]:
    print("{} {}".format(k, v))


###############    Piling Up!  ################

# Enter your code here. Read input from STDIN. Print output to STDOUT

T=int(raw_input())
for i in range(T):
    input()
    The_list = [int(i) for i in raw_input().split()]
    Min_list = The_list.index(min(The_list))
    Left = The_list[:Min_list]
    Right = The_list[Min_list+1:]
    if Left == sorted(Left, reverse=True) and Right == sorted(Right):
        print("Yes")
    else:
        print("No")

