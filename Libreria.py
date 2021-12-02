import pygame
import math
import numpy as np 
import time

Ventana = pygame

# Dibujar un punto
def punto(Ventana,Color,PosXY):
    pygame.draw.line(Ventana,Color,PosXY,PosXY,1)

def punto2(Ventana, Color, p_ini):
    pygame.draw.line(Ventana,Color, p_ini, p_ini,4)

# Linea DDA
def lineaDDA(Ventana,Color,PosIni,PosFin):
    x1=PosIni[0]
    y1=PosIni[1]
    x2=PosFin[0]
    y2=PosFin[1]
    dy=y2-y1
    dx=x2-x1
    
    if abs(dx)>abs(dy):
        steps = dx
    else:
        steps = dy
    IncrementoX = float(dx)/float(steps)
    IncrementoY = float(dy)/float(steps)
    punto(Ventana,Color,[x1,y1])
    for i in range(steps):
        x1 += IncrementoX
        y1 += IncrementoY
        punto(Ventana,Color,[int(round(x1)),int(round(y1))])

# Linea Bresenham
def LineaBres(Ventana,Color,PosIni,PosFin):
    x1 = PosIni[0]
    y1 = PosIni[1]
    x2 = PosFin[0]
    y2 = PosFin[1]
    dy = y2 - y1
    dx = x2 - x1
    stepY = -1 if dy < 0 else 1
    dy = math.fabs(dy)
    stepX = -1 if dx < 0 else 1
    dx = math.fabs(dx)

    if dx > dy:
        p = 2*dy-dx
        incE = 2*dy
        incNE = 2*(dy-dx)
        x = x1
        y = y1
        xEnd = x2
        stepX = 1
        punto(Ventana,Color,[x,y])
        
        while x != xEnd:
            x += stepX
            if p < 0:
                p += incE
            else:
                p += incNE
                y += stepY
                punto(Ventana,Color,[x,y])
    else: 
        p = 2*dx-dy
        incE = 2*dx
        incNE = 2*(dx-dy)
        x = x1
        y = y1
        yEnd = y2
        stepY = 1
        punto(Ventana,Color,[x,y])
        while y != yEnd:
            y += stepY
            if p < 0:
                p += incE
            else:
                p += incNE
                x += stepX
            punto(Ventana,Color,[x,y])

def Rectangulo(Ventana,Color,PosIni,PosFin):
    x0 = PosIni[0]
    y0 = PosIni[1]
    x1 = PosFin[0]
    y1 = PosFin[1]
    lineaDDA(Ventana,Color,[x0,y0],[x1,y0])
    lineaDDA(Ventana,Color,[x0,y1],[x1,y1])
    lineaDDA(Ventana,Color,[x0,y0],[x0,y1])
    lineaDDA(Ventana,Color,[x1,y0],[x1,y1])

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


def Circulo(Ventana,Color,xc,yc,x,y):
    punto(Ventana, Color, [xc+x,yc+y])
    punto(Ventana, Color, [xc-x,yc+y])
    punto(Ventana, Color, [xc+x,yc-y])
    punto(Ventana, Color, [xc-x,yc-y])
    punto(Ventana, Color, [xc+y,yc+x])
    punto(Ventana, Color, [xc-y,yc+x])
    punto(Ventana, Color, [xc+y,yc-x])
    punto(Ventana, Color, [xc-y,yc-x])

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

def Triangulo(windows,colorb,x_ini,y_ini,base,altu):
    X0= x_ini
    Y0= y_ini
    LineaBres(windows, colorb, [X0, Y0],[X0+base,Y0])
    LineaBres(windows, colorb, [X0, Y0],[X0+(base/2),Y0-altu])
    LineaBres(windows, colorb, [X0+base, Y0],[X0+(base/2),Y0-altu])

def TrianguloRectangulo(Ventana,Color,PosIni,Base,Altura,Dir):
    if Dir==0:
        x0 = PosIni[0]
        y0 = PosIni[1]
        x1 = x0
        y1 = x0 - Altura
        x2 = x0 + Base
        y2 = y0
        LineaBres(Ventana, Color,[x1,y1],[x0,y0])
        LineaBres(Ventana, Color,[x0,y0],[x2,y2])
        LineaBres(Ventana, Color,[x1,y1],[x2,y2])
    else: 
        if Dir==1:
            x0 = PosIni[0]
            y0 = PosIni[1]
            x1 = x0
            y1 = x0 - Altura
            x2 = x0 - Base
            y2 = y0
            LineaBres(Ventana, Color,[x1,y1],[x0,y0])
            LineaBres(Ventana, Color,[x2,y2],[x0,y0])
            LineaBres(Ventana, Color,[x2,y2],[x1,y1])
    
def TrianguloEquilatero(Ventana,Color,PosIni,Lado):
    x0 = PosIni[0]
    y0 = PosIni[1]
    x1 = x0 + Lado
    y1 = y0
    x2 = x0 + (Lado/2)
    y2 = y0 - round(((3**0.5) * Lado)/2)
    LineaBres(Ventana, Color,[x0,y0],[x1,y1])
    LineaBres(Ventana, Color,[x2,y2],[x0,y0])
    LineaBres(Ventana, Color,[x2,y2],[x1,y1])

def Pentagono(Ventana,Colorb,x_ini,y_ini,Lado,Borde):
    X0= x_ini
    Y0= y_ini
    LineaBres(Ventana, Colorb, [X0, Y0],[Lado,Y0])
    LineaBres(Ventana, Colorb, [X0-(Lado*0.1), Lado],[X0,Y0])
    LineaBres(Ventana, Colorb, [Lado+(Lado*0.1), Lado],[Lado,Y0])
    LineaBres(Ventana, Colorb, [Lado+(Lado*0.1), Lado],[230,Borde-100])
    LineaBres(Ventana, Colorb, [X0-(Lado*0.1), Lado],[230,Borde-100])


def LineaBres2(Ventana, Color, Pos_ini, Pos_fin):
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
        punto2(Ventana, Color,[x,y])
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
            punto2(Ventana, Color, [x,y])
    
    else:
        p = 2 * dx - dy
        incE = 2 * dx
        incNE = 2 * (dx - dy)
        x = x1
        y = y1
        yEnd = y2
        stepY = 1
        punto2(Ventana, Color, [x,y])
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
            punto2(Ventana, Color, [x,y])
    

def Rectangulo_Borde(Ventana, Color, Pos_ini, Pos_fin):
    X0= Pos_ini[0]
    Y0= Pos_ini[1]
    X1= Pos_fin[0]
    Y1= Pos_fin[1]
    LineaBres2(Ventana, Color, [X0, Y0],[X1,Y0])
    LineaBres2(Ventana, Color, [X0, Y1],[X1,Y1])
    LineaBres2(Ventana, Color, [X0, Y0],[X0,Y1])
    LineaBres2(Ventana, Color, [X1, Y0],[X1,Y1])

pygame.init()
Ventana = pygame.display.set_mode((800,600))
Ventana.fill((255,255,255))
amarillo = np.array([255,255,0])
rojo = np.array([255,0,0])
verde = np.array([0,255,0])
azul = np.array([0,0,255])
blanco = np.array([255,255,255])

pygame.display.update()

time.sleep(5)