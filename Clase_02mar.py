import numpy as np 
import math 

VectorA = np.array([2,3,4]) # Permite crear un arreglo de tipo Numpy
print("A =",VectorA)

MatrizA = np.array([[2,5,1],[5,6,3],[8,9,2]])
print("Matriz =",MatrizA)

VectorB = VectorA*2  # Multiplicar un escalar por un vector 
print("B =",VectorB)

TempGradosC = np.array([10.12,13.00,17.30,18.35])
TempGradosF = ((TempGradosC * 9/5) + 32)
print("Temperatura en grados C =",TempGradosC)
print("Temperatura en grados F =",TempGradosF)

MiArray = np.array([5,6,7,8,9,8,21,14,9,34]) # Recorrer un vector elemento por elemento 
for i in range(0,10):
    print("Posicion ",i,"=",MiArray[i])

s = MiArray.sum()
print("Suma de los elementos del vector =",s)

