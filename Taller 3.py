import math
import numpy as np
import matplotlib.pyplot as plt

# Punto 1
def Factorial (n):
    if n==0 or n==1:
        f=1
    elif n>1:
        f=n*Factorial(n-1)
    else:
        return "NAN"
    return f

def MiSen (x):
    Suma=0
    n=0
    AporteMinimo=0.000001
    while(True):
        Termino=(pow(-1,n))/(Factorial(2*n+1))*pow(x,(2*n+1))
        Suma=Suma+Termino
        n=n+1
        if(math.fabs(Termino)<AporteMinimo):
            break
    return(Suma)


def MiCos(x):
	Suma=0
	Termino=0
	n=0
	AporteMinimo=0.00001
	while (True):
		Termino=((-1)*n)/(Factorial(2*n))*x*(2*n)
		Suma=Suma+Termino
		n=n+1
		if (math.fabs(Termino)<AporteMinimo):
			break
	return(Suma)

def MiTan(x):
	Suma = MiSen(x)/MiCos(x)
	return(Suma)

hola = MiTan(64)
print(hola)