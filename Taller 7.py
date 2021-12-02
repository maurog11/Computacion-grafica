import math
import numpy as np
import pygame
import time

Ventana = pygame
Amarillo = np.array([255,255,0])
Rojo = np.array([255,0,0])
Verde = np.array([0,255,0])
Azul = np.array([0,0,255])
Blanco = np.array([255,255,255])
Negro = np.array([0,0,0])

pygame.init()
Ventana = pygame.display.set_mode((800,600))
Ventana.fill((255,255,255))
pygame.display.set_caption("Primitivas graficas") 

def Punto(Ventana, Color, Pos_ini):
    pygame.draw.line(Ventana, Color, Pos_ini, Pos_ini,1)



def LineaBres(Ventana, Color, Pos_ini, Pos_fin):
    x1=Pos_ini[0]
    y1=Pos_ini[1]
    x2=Pos_fin[0]
    y2=Pos_fin[1]
    dy=y2-y1
    dx= x2-x1
    stepY = -1 if dy < 0 else 1
    dy = math.fabs(dy)
    stepX = -1 if dx < 0 else 1
    dx = math.fabs(dx)

    if dx > dy:
        p = 2 * dy - dx
        incE = 2 * dy
        incNE = 2 * (dy - dx)
        x = x1
        y = y1
        xEnd = x2
        stepX = 1
        Punto(Ventana, Color,[x,y])
        while x != xEnd:
            if x < xEnd:
                x += stepX
            else:
                x -= stepX
            if p < 0:
                p += incE
            else:
                p += incNE
                y += stepY
            Punto(Ventana, Color, [x,y])
    
    else:
        p = 2 * dx - dy
        incE = 2 * dx
        incNE = 2 * (dx - dy)
        x = x1
        y = y1
        yEnd = y2
        stepY = 1
        Punto(Ventana, Color, [x,y])
        while y != yEnd:
            if y < yEnd:
                y += stepY
            else:
                y -= stepY
            if p < 0:
                p += incE
            else:
                p += incNE
                x += stepX
            Punto(Ventana, Color, [x,y])


def Rectangulo_Relleno(Ventana,Colorb,Color,Pos_ini,Pos_fin):
    X0= Pos_ini[0]
    Y0= Pos_ini[1]
    X1= Pos_fin[0]
    Y1= Pos_fin[1]
    LineaBres(Ventana, Colorb, [X0, Y0],[X1,Y0])
    LineaBres(Ventana, Colorb, [X0, Y1],[X1,Y1])
    LineaBres(Ventana, Colorb, [X0, Y0],[X0,Y1])
    LineaBres(Ventana, Colorb, [X1, Y0],[X1,Y1])
    Y0= Y0 +1
    t=Y0-1
    j = (Y1 + Y0-1)/ 2
    h = (X1+X0)/2
    while Y0 < Y1:
        if t < j:
            LineaBres(Ventana, Color, [X0+1, Y0],[h,Y0])
            Y0=Y0+1
            t=t+1
        else:
            LineaBres(Ventana, Color, [h, Y0],[X1,Y0])
            Y0=Y0+1


def Figura_2(Ventana,Colorb,Color,Pos_ini,Pos_fin):
    X0= Pos_ini[0]
    Y0= Pos_ini[1]
    X1= Pos_fin[0]
    Y1= Pos_fin[1]
    LineaBres(Ventana, Colorb, [X0, Y0],[X1,Y0])
    LineaBres(Ventana, Colorb, [X0, Y1],[X1,Y1])
    LineaBres(Ventana, Colorb, [X0, Y0],[X0,Y1])
    LineaBres(Ventana, Colorb, [X1, Y0],[X1,Y1])
    Y0= Y0 +1
    t=50
    j=150
    p=250
    q=250
    while Y0 < 150:
            LineaBres(Ventana, Color, [X0+1, Y0],[200,Y0])
            Y0=Y0+1
    while p < 350:
            LineaBres(Ventana, Color, [X0+1, p],[200,p])
            p=p+1
    while q < 350:
            LineaBres(Ventana, Color, [300, q],[400,q])
            q=q+1
    while t < 150:
            LineaBres(Ventana, Color, [300, t],[400,t])
            t=t+1
    while j < 250:
            LineaBres(Ventana, Color, [200, j],[300,j])
            j=j+1
   

def Figura_3(Ventana,Colorb,Color,pos_ini,pos_fin):
    X0= pos_ini[0]
    Y0= pos_ini[1]
    X1= pos_fin[0]
    Y1= pos_fin[1]
    LineaBres(Ventana, Colorb, [X0, Y0],[X1,Y0])
    LineaBres(Ventana, Colorb, [X0, Y1],[X1,Y1])
    LineaBres(Ventana, Colorb, [X0, Y0],[X0,Y1])
    LineaBres(Ventana, Colorb, [X1, Y0],[X1,Y1])
    Y0= Y0 +1
    t=150
    j=150
    p=250
    q=150
    while Y0 < 150:
            LineaBres(Ventana, Color, [200, Y0],[300,Y0])
            Y0=Y0+1
    while p < 350:
            LineaBres(Ventana, Color, [200, p],[300,p])
            p=p+1
    while j < 250:
            LineaBres(Ventana, Color, [200, j],[300,j])
            j=j+1
    while t < 250:
            LineaBres(Ventana, Color, [100, t],[200,t])
            t=t+1 
    while q < 250:
            LineaBres(Ventana, Color, [300, q],[400,q])
            q=q+1   


def Figura_4(Ventana,Colorb,Color,pos_ini,pos_fin):
    X0= pos_ini[0]
    Y0= pos_ini[1]
    X1= pos_fin[0]
    Y1= pos_fin[1]
    LineaBres(Ventana, Blanco, [X0, Y0],[X1,Y0])
    LineaBres(Ventana, Blanco, [X0, Y1],[X1,Y1])
    LineaBres(Ventana, Blanco, [X0, Y0],[X0,Y1])
    LineaBres(Ventana, Blanco, [X1, Y0],[X1,Y1])
    Y0= Y0 +1
    t=150
    j=250
    p=350
    q=450
    while Y0 < 150:
            LineaBres(Ventana,Color, [X0, Y0],[200,Y0])
            Y0=Y0+1
    while t < 250:
            LineaBres(Ventana,Color, [X0, t],[300,t])
            t=t+1
    while j < 350:
            LineaBres(Ventana,Color, [X0, j],[400,j])
            j=j+1
    while p < 450:
            LineaBres(Ventana,Color, [X0, p],[500,p])
            p=p+1
    while q < 550:
            LineaBres(Ventana,Color, [X0, q],[600,q])
            q=q+1
  

def Figura_5(Ventana,Colorb,Color,pos_ini,pos_fin):
    X0= pos_ini[0]
    Y0= pos_ini[1]
    X1= pos_fin[0]
    Y1= pos_fin[1]
    LineaBres(Ventana, Blanco, [X0, Y0],[X1,Y0])
    LineaBres(Ventana, Blanco, [X0, Y1],[X1,Y1])
    LineaBres(Ventana, Blanco, [X0, Y0],[X0,Y1])
    LineaBres(Ventana, Blanco, [X1, Y0],[X1,Y1])
    Y0= Y0 +1
    t=100
    j=200
    p=300
    q=400
    s=500
    while Y0 < 100:
            LineaBres(Ventana,Color, [350, Y0],[450,Y0])
            Y0=Y0+1
    while t < 200:
            LineaBres(Ventana,Color, [300, t],[500,t])
            t=t+1
    while j < 300:
            LineaBres(Ventana,Color, [250, j],[550,j])
            j=j+1
    while p < 400:
            LineaBres(Ventana,Color, [200, p],[600,p])
            p=p+1
    while q < 500:
            LineaBres(Ventana,Color, [150, q],[650,q])
            q=q+1
    while s < 600:
            LineaBres(Ventana,Color, [100, s],[700,s])
            s=s+1


def TrianguloRectangulo(Ventana,Colorb,x_ini,y_ini,Base,Altura):
    X0= x_ini
    Y0= y_ini
    LineaBres(Ventana, Colorb, [X0, Y0],[X0+Base,Y0])
    LineaBres(Ventana, Colorb, [X0, Y0],[X0,Y0-Altura])
    LineaBres(Ventana, Colorb, [X0+Base, Y0],[X0, Y0-Altura])
    


def Triangulo(Ventana,Colorb,x_ini,y_ini,base,altu):
    X0= x_ini
    Y0= y_ini
    LineaBres(Ventana, Colorb, [X0, Y0],[X0+base,Y0])
    LineaBres(Ventana, Colorb, [X0, Y0],[X0+(base/2),Y0-altu])
    LineaBres(Ventana, Colorb, [X0+base, Y0],[X0+(base/2),Y0-altu])


def Circulo(Ventana,Colorb,xc,yc,x,y):
    Punto(Ventana,Colorb,[xc+x,yc+y])
    Punto(Ventana,Colorb,[xc-x,yc+y])
    Punto(Ventana,Colorb,[xc+x,yc-y])
    Punto(Ventana,Colorb,[xc-x,yc-y])
    Punto(Ventana,Colorb,[xc+y,yc+x])
    Punto(Ventana,Colorb,[xc-y,yc+x])
    Punto(Ventana,Colorb,[xc+y,yc-x])
    Punto(Ventana,Colorb,[xc-y,yc-x])


def CirculoBres(Ventana,Color,xc,yc,r):
    x = 0
    y = r
    d = 3 - 2 * r
    Circulo(Ventana, Color, xc, yc, x, y)
    while(y >= x):
        x = x+1
        if(d > 0):
            y = y-1
            d = d+4*(x-y)+10
        else:
            d = d+4*x+6
        Circulo(Ventana, Color, xc, yc, x, y);

def Trapecio(Ventana,Colorb,x_ini,y_ini,Base_menor,Base_mayor,base,Altura):
    X0= x_ini
    Y0= y_ini
    LineaBres(Ventana, Colorb, [X0, Y0],[Base_mayor,Y0])
    LineaBres(Ventana, Colorb, [X0+(Base_mayor/4), Altura],[Base_menor-(Base_mayor/4),Altura])
    LineaBres(Ventana, Colorb, [X0, Y0],[X0+(Base_mayor/4),Altura])
    LineaBres(Ventana, Colorb, [Base_mayor,Y0],[Base_menor-(Base_mayor/4),Altura])


def Pentagono(Ventana,Colorb,x_ini,y_ini,Lado,Borde):
    X0= x_ini
    Y0= y_ini
    LineaBres(Ventana, Colorb, [X0, Y0],[Lado,Y0])
    LineaBres(Ventana, Colorb, [X0-(Lado*0.1), Lado],[X0,Y0])
    LineaBres(Ventana, Colorb, [Lado+(Lado*0.1), Lado],[Lado,Y0])
    LineaBres(Ventana, Colorb, [Lado+(Lado*0.1), Lado],[230,Borde-100])
    LineaBres(Ventana, Colorb, [X0-(Lado*0.1), Lado],[230,Borde-100])
   


#Figura 1
Rectangulo_Relleno(Ventana,Negro,Azul,[250,50],[600,300])

#Figura 2
#Figura_2(Ventana,Negro,Azul,[100,50],[400,350])

#Figura 3
#Figura_3(Ventana,Negro,Azul,[100,50],[400,350])

#Figura 4
#Figura_4(Ventana,Negro,Azul,[100,50],[600,550])

#Figura 5
#Figura_5(Ventana,Negro,Azul,[100,0],[700,600])

#Figura 6
#TrianguloRectangulo(Ventana,Azul,200,300,100,100)

#Figura 7
#Triangulo(Ventana,Azul,300,400,200,200)

#Figura 8
#Trapecio(Ventana,Azul,100,500,500,500,100,300)

#Figura 9
#Pentagono(Ventana,Azul,100,500,350,350)

#Figura 10
#CirculoBres(Ventana,Azul,400,300,100)



pygame.display.update()

time.sleep(5)