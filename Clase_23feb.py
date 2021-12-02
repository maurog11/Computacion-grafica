import math
import numpy as np
import matplotlib as matplotlib
import pygame as pg

def ComponenteX (r,ang): #Calcular coordenadas polares 
    return(round(r*math.cos(ang*math.pi/180),2))

def ComponenteY (r,ang):
    return(round(r*math.sin(ang*math.pi/180),2))

def MagnitudVector (x,y):
    return(round(math.sqrt(x**2+y**2),2))

def AnguloVector (x,y):
    return(round(math.atan((y/x))*180/math.pi,2))



def main():
    x=ComponenteX(5,20)
    y=ComponenteY(5,20)
    r=MagnitudVector(x,y)
    ang=AnguloVector(x,y)
    print("Componente x:",x)
    print("Componente y:",y)
    print("Magnitud del vector:",r)
    print("Angulo del vector:",ang)

main()