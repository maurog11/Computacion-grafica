import numpy as np
import math
import matplotlib.pyplot as plt

def MiFactorial (n):
    if n==0 or n==1:
        f=1
    elif n>1:
        f=n*MiFactorial(n-1)
    else:
        return "NAN"
    return f



def MiSeno (x):
    Suma=0
    n=0
    AporteMinimo=0.000001
    while(True):
        Termino=(pow(-1,n))/(MiFactorial(2*n+1))*pow(x,(2*n+1))
        # print("Termino ",n+1,"=",Termino)
        Suma=Suma+Termino
        n=n+1
        if(math.fabs(Termino)<AporteMinimo):
            break
    return(Suma)


def GraficaSeno (PuntoIni,PuntoFinal,CantPuntos):
    x = np.linspace(PuntoIni,PuntoFinal,CantPuntos)
    i=0
    while i<CantPuntos:
        y=MiSeno(x[i])
        plt.plot(x[i],y,"-")
        i=i+1
    plt.title("Grafica funcion seno")
    plt.xlabel("Eje x")
    plt.ylabel("Eje y")
    plt.grid(True)
    plt.show()
   

# Llamado
GraficaSeno(0,2*math.pi,100)

