import numpy as np
a=np.array([-1,1])
b=np.array([1,1])
print(np.dot(a,b))

X = np.array([[1,0,1],[2,2,2]])
out = X[0:2,2]
print(out)

X=np.array([[1,0],[0,1]])
Y=np.array([[2,2],[2,2]])
Z=np.dot(X,Y)
print(Z)

with open("example.txt","r") as file1:
    FileContent=file1.read()
print(FileContent)