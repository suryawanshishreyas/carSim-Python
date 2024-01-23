import time 
import sys
import numpy as np 

import matplotlib.pyplot as plt


def Plotvec2(a,b):
    ax = plt.axes()# to generate the full window axes
    ax.arrow(0, 0, *a, head_width=0.05, color ='r', head_length=0.1)#Add an arrow to the  a Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color ='b', head_length=0.1)#Add an arrow to the  b Axes with arrow head width 0.05, color blue and arrow head length 0.1
    plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)#set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)#set the xlim to left(-2), right(2)

a = np.array([-1,1])
b = np.array([1,1])
result = np.dot(a,b)
Plotvec2(a,b)
#Uncomment below code to check output
plt.plot(a,b)
plt.show()

#-----------------Two Dimensional Array Operation ---------------------#

x = [[11,12,13],[21,22,23],[31,32,33]]
X = np.array(x)
print(X.size)
print(X.shape)
print(X.ndim)
print(X[1,2])
print(X[0][0:2])

#Array Addition

X = np.array([[1,2],[1,2]])
Y = np.array([[0,2],[2,1]])

Z = X + Y
print(Z)

#Array Multiplication
Z = X*Y
print(Z)

#Matrix Multiplication ==> [!IMP]
A = np.array([[1,2,3],[2,3,1],[3,2,1]])
B = np.array([[1,0],[0,1],[-1,-1]])

C = np.dot(A,B)
print(C)
print(np.sin(Z))

#Transpose of matrix

t = np.array([[1,1,1],[2,2,2],[3,3,3]])
print(t.T)