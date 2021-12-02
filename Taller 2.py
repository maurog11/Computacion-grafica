import numpy as np
import math

# Punto 1
m=np.array([[0,2,4,6],[0,3,5,7]])
np.savetxt("matriz.mat", m)
print("M=",m)
del m
n=np.loadtxt("matriz.mat")
print(n[1][3])
print(n[0:2,0:2])

# Punto 2
a=np.array([[1,3,5,8],[2,6,5,3],[4,1,9,7],[1,8,0,2]])
b=np.array([[1,9,5,8],[12,5,5,9],[4,2,9,74],[0,6,0,3]])
c=np.array([[1,9],[10,2] ])

print("A=",a)
print("B=",b)
print("C=",c)

# (3*A)
print("3*A=",3*a)

# (A-7)
print("A-7=",a-7)

# (A*B)
print("A*B=",a*b)

# (A^-1)
print("A^-1=",np.linalg.inv(a))

# (B^-1)
print("B^-1=",np.linalg.inv(b))