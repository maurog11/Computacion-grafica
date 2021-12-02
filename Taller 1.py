import numpy as np 
import math 
from statistics import mode

# Punto 1 
VectorA = np.array ([2,3,5,1,4,7,9,8,6,10])
print("A =",VectorA)

# Punto 2
VectorB = np.arange(10)
print("B =",VectorB)

# Punto 3 
VectorC = np.concatenate([VectorA,VectorB])
print("C =",VectorC)

# Punto 4 
Min_C = np.amin(VectorC)
print("Valor minimo del vector C =",Min_C)

# Punto 5
Max_C = np.amax(VectorC)
print("Valor maximo del vector C =",Max_C)

# Punto 6
print("Longitud del vector C =",VectorC.size)

# Punto 7 
suma = VectorC.sum()
print("Suma de elementos del vector C =",suma)

# Punto 8 
prom = (VectorC.sum()/20)
print("Promedio de elementos del vector C =",prom)

# Punto 9 
prom2 = VectorC.mean()
print("Promedio de elementos del vector C =",prom2)

# Punto 10
media = VectorC.mean()
print("Media de elementos del vector C =",media)

# Punto 11 
suma = VectorC.sum()
print("Suma de elementos del vector C =",suma)

# Punto 12 
VectorD=[]
for i in range (0,np.size(VectorC)):
    if (VectorC[i]>=5):
        VectorD.append(VectorC[i])
print("Mayores que 5 =",VectorD)

# Punto 13
VectorE=[]
for i in range (0,np.size(VectorC)):
    if ((VectorC[i] >= 5) and (VectorC[i]<= 15)):
        VectorE.append(VectorC[i])
print("Mayores que 5 y menores que 15 del Vector C =",VectorE)

# Punto 14
for i in range (0,np.size(VectorC)):
    if ((VectorC[i]==5) or (VectorC[i]==15) ):
        VectorC[i]=7
print("Vector C sin 15 ni 5 =",VectorC)

# Punto 15
print("Moda del vector C =", mode(VectorC))

# Punto 16
VectorC.sort()
print("Ordenamiento del vector C =", VectorC)

# Punto 17
print("Multiplicar por 2 =",VectorC*2)

# Punto 18
VectorC[6]=60
VectorC[7]=70
VectorC[8]=80
print("Cambio de los elementos =",VectorC)

# Punto 19
VectorC[14]=140
VectorC[15]=150
VectorC[16]=160
print("Segundo cambio de elementos en Vector C =",VectorC)





