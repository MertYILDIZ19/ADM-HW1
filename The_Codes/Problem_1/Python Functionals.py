###############   Map and Lambda Function   ################

cube = lambda x:x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    Sec_Num = 1
    Fir_Num =0
    The_Series = [0,1]
    for _ in range(n-2):
        Dummy = Sec_Num
        Sec_Num = Fir_Num + Sec_Num
        Fir_Num = Dummy
        The_Series.append(Sec_Num)
    if n==0:
        return []
    elif n==1:
        return[0]
    return The_Series

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))