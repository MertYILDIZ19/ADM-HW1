###############    List Comprehensions ################

if __name__ == '__main__':
    x,y,z,n = [int(raw_input()) for i in range(4)]
    print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if ((i+j+k) != n)])


###############   Find the Runner-Up Score!   ################

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    z = max(arr)
    while max(arr) == z:
        arr.remove(max(arr))

    print max(arr)


###############   Finding the percentage   ################

if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    query_scores = student_marks[query_name]
    print("{0:.2f}".format(sum(query_scores)/(len(query_scores))))


###############   Lists   ################

if __name__ == '__main__':
    N = int(raw_input())
    l = []
    for _ in range(N):
        s = raw_input().split()
        cmd = s[0]
        args = s[1:]
        if cmd !="print":
            cmd += "("+ ",".join(args) +")"
            eval("l."+cmd)
        else:
            print l



###############   Tuples   ################

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    tup = ()

    for x in integer_list:
        tup+=(x,)
    print(hash(tup))


###############   Nested Lists   ################

if __name__ == '__main__':
    n=int(input())
    arr=[[raw_input(),float(input())] for _ in range(0,n)]
    arr.sort(key=lambda x: (x[1],x[0]))
    names = [i[0] for i in arr]
    marks = [i[1] for i in arr]
    min_val=min(marks)
    while marks[0]==min_val:
        marks.remove(marks[0])
        names.remove(names[0])    
    for x in range(0,len(marks)):
        if marks[x]==min(marks):
            print(names[x])   
