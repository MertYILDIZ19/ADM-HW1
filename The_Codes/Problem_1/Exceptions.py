###############   Exceptions   ################

# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(raw_input())
for i in range(T):
    a, b = raw_input().split(' ')

    try:
        print(int(a)//int(b))
    except Exception as error:
        print "Error Code:", error 


