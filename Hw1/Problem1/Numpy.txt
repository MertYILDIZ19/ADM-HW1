###############    Arrays   ################

import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    return(numpy.array(arr[::-1], float))

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

###############    Shape and Reshape   ################

import numpy as np

arr = input().split(' ')

arr = np.array(arr).astype(int)
print(np.reshape(arr, (3,3)))

###############    Transpose and Flatten   ################

import numpy as np

Size = list(map(int, input().split(' ')))

Matrix = np.array([list(map(int, input().split(' '))) for i in range(Size[0])])

print(np.transpose(Matrix))
print(Matrix.flatten())

###############    Concatenate   ################

import numpy as np

Size = list(map(int, input().split(' ')))

First_Matrix = np.array([list(map(int, input().split(' '))) for i in range(Size[0])])
Second_Matrix = np.array([list(map(int, input().split(' '))) for i in range(Size[1])])

print (np.concatenate((First_Matrix, Second_Matrix)))

###############    Zeros and Ones   ################

import numpy as np

N = tuple(map(int,input().strip().split()))
Zero = np.zeros(N, dtype=np.int)
One = np.ones(N, dtype=np.int)
print (Zero)
print (One)

###############    Eye and Identity   ################

import numpy as np

Size = list(map(int, input().split(' ')))
print(str(np.eye(Size[0], Size[1])).replace('1',' 1').replace('0',' 0'))

###############    Array Mathematics   ################

import numpy 
N, M = list(map(int, input().split()))

Array_1 = numpy.array([input().split() for _ in range(N)], int)
Array_2 = numpy.array([input().split() for _ in range(N)], int)

print(*[eval('Array_1'+i+'Array_2') for i in ['+','-','*','//','%','**']], sep='\n')

###############    Floor, Ceil and Rint   ################

import numpy 
numpy.set_printoptions(sign=' ')

The_Array = numpy.array(list(map(float, input().split(' '))))
print (numpy.floor(The_Array))
print (numpy.ceil(The_Array))
print (numpy.rint(The_Array))

###############    Sum and Prod   ################

import numpy 
N,M = map(int,input().split())
The_Array = numpy.array([input().split() for i in range(N)], int)
print(numpy.prod((numpy.sum(The_Array,axis=0))))

###############    Min and Max   ################

import numpy as np
Size = list(map(int, input().split(' ')))

Matrix = np.array([list(map(int, input().split(' '))) for i in range(Size[0])])
print(np.max((np.min(Matrix, axis = 1))))

###############    Mean, Var, and Std   ################

import numpy 
numpy.set_printoptions(legacy='1.13')

Size = list(map(int, input().split(' ')))

Matrix = numpy.array([list(map(int, input().split(' '))) for i in range(Size[0])])
print(numpy.mean(Matrix, axis = 1))
print(numpy.var(Matrix, axis = 0))
print(numpy.std(Matrix))

###############    Dot and Cross  ################

import numpy as np
N=int(input())
First_Arr,Second_Arr=[(np.array([list(map(int,input().split())) for _ in range(N)])) for _ in range(2)]
print (np.dot(First_Arr,Second_Arr))

###############    Inner and Outer  ################

import numpy 
numpy.set_printoptions(legacy='1.13')

First_Mtx = numpy.array(list(map(int, input().split(' '))))
Second_Mtx = numpy.array(list(map(int, input().split(' '))))

print(numpy.inner(First_Mtx, Second_Mtx))
print(numpy.outer(First_Mtx, Second_Mtx))

###############    Polynomials  ################

import numpy

N = list(map(float,input().split()));
M = input();
print(numpy.polyval(N,int(M)));

###############    Linear Algebra  ################

import numpy 
numpy.set_printoptions(legacy='1.13')
Size = int(input())
Matrix = numpy.array([list(map(float, input().split(' '))) for i in range(Size)])

print(numpy.linalg.det(Matrix))
