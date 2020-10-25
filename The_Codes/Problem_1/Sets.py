###############   Introduction to Sets   ################

from __future__ import division

def average(arr):
    # your code goes here
    sum_arr = sum(set(arr))
    len_arr = len(set(arr))
    avg = sum_arr/len_arr
    return avg;
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    result = average(arr)
    print result

###############    Symmetric Difference   ################

# Enter your code here. Read input from STDIN. Print output to STDOUT

int(raw_input())
N = raw_input().split()
Nintegers = set(list(map(int, N)))
int(raw_input())
M = raw_input().split()
Mintegers = set(list(map(int, M)))
simm_diff = []
for i in list(Nintegers.difference(Mintegers)):
    simm_diff.append(i)
for j in list(Mintegers.difference(Nintegers)):
    simm_diff.append(j)
for k in sorted(simm_diff):
    print k

###############    No Idea!   ################

# Enter your code here. Read input from STDIN. Print output to STDOUT

m_n = raw_input().split()
m = int(m_n[0])
n = int(m_n[1])

el_arr = list()
happiness = 0

el_arr = list(map(int, raw_input().strip().split()))

Set_A = set(map(int, raw_input().strip().split()))
Set_B = set(map(int, raw_input().strip().split()))

for i in el_arr:
    if i in Set_A:
        happiness = happiness+1
    if i in Set_B:
        happiness = happiness-1

print(happiness)

###############    Set .add()   ################

# Enter your code here. Read input from STDIN. Print output to STDOUT

Stamps = set()
for i in range(int(raw_input())):
    Stamps.add(raw_input())
print(len(Stamps))

###############    Set .discard(), .remove() & .pop()   ################

n = input()
s = set(map(int, raw_input().split()))

for i in range(int(raw_input())):
    command = raw_input().split()
    if command[0] == "pop":
        s.pop()

    elif command[0] == "remove":
        s.remove(int(command[1]))

    elif command[0] == "discard":
        s.discard(int(command[1]))

print(sum(s))

###############    Set .union() Operation   ################

# Enter your code here. Read input from STDIN. Print output to STDOUT

n1 = int(raw_input())
arr1 = set(list(map(int, raw_input().split())))

n2 = int(raw_input())
arr2 = set(list(map(int, raw_input().split())))

print(len(arr1.union(arr2)))

###############    Set .intersection() Operation   ################

# Enter your code here. Read input from STDIN. Print output to STDOUT

n1 = int(raw_input())
arr1 = set(list(map(int, raw_input().split())))

n2 = int(raw_input())
arr2 = set(list(map(int, raw_input().split())))

print(len(arr1.intersection(arr2)))

###############    Set .difference() Operation   ################

# Enter your code here. Read input from STDIN. Print output to STDOUT

n1 = int(raw_input())
arr1 = set(list(map(int, raw_input().split())))

n2 = int(raw_input())
arr2 = set(list(map(int, raw_input().split())))

print(len(arr1.difference(arr2)))

###############    Set .symmetric_difference() Operation   ################

# Enter your code here. Read input from STDIN. Print output to STDOUT

n1 = int(raw_input())
arr1 = set(list(map(int, raw_input().split())))

n2 = int(raw_input())
arr2 = set(list(map(int, raw_input().split())))

print(len(arr1.symmetric_difference(arr2)))

###############    Set Mutations   ################

# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    (_, A) = (int(raw_input()),set(map(int, raw_input().split())))
    B = int(raw_input())
    for _ in range(B):
        (Command, NewSet) = (raw_input().split()[0],set(map(int, raw_input().split())))
        getattr(A, Command)(NewSet)

    print (sum(A))

###############    The Captain's Room   ################

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input())
Arr1 = list(map(int, raw_input().split()))
Set_Arr1 = set(Arr1)

print(((sum(Set_Arr1)*n)-(sum(Arr1)))//(n-1))

###############    Check Subset   ################

for i in range(int(raw_input())):

    N1 = int(raw_input())
    Arr1 = set(list(map(int, raw_input().split())))

    N2 = int(raw_input())
    Arr2 = set(list(map(int, raw_input().split())))

    if Arr1.issubset(Arr2):
        print(True)
    else:
        print(False)

###############    Check Strict Superset   ################

# Enter your code here. Read input from STDIN. Print output to STDOUT

Arr1 = set(list(map(int, raw_input().split())))
N1 = int(raw_input())

Count = 0
for i in range(N1):
    Sets = set(list(map(int, raw_input().split())))

    if Sets.issubset(Arr1) and len(Arr1)>len(Sets):
       Count +=1
if Count == N1:
    print(True)
else:
    print(False)



