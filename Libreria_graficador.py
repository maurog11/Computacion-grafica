import math
import numpy as np
#import matplotlib.pyplot as plt
import pygame
import time
windows=pygame

def punto(windows, color, p_ini):
    pygame.draw.line(windows,color, p_ini, p_ini,1)

def punto2(windows, color, p_ini):
    pygame.draw.line(windows,color, p_ini, p_ini,4)


def LineaDDA (windows, color,p_ini,p_fin):
    x1=p_ini[0]
    y1=p_ini[1]
    x2=p_fin[0]
    y2=p_fin[1]
    dy=y2-y1
    dx= x2-x1
    if abs(dx) > abs(dy):
        steps = dx
    else:
        steps = dy
    xIncrement= float(dx) / float(steps)
    yIncrement= float(dy) / float(steps)
    punto(windows,color,[x1,y1])
    for i in range(steps):
        x1+=xIncrement
        y1+=yIncrement
        punto(windows,color,[int(round(x1)), int(round(y1))])


def LineaBres(windows, color, p_ini, p_fin):
    x1=p_ini[0]
    y1=p_ini[1]
    x2=p_fin[0]
    y2=p_fin[1]
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
        punto(windows, color,[x,y])
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
            punto(windows, color, [x,y])
    
    else:
        p = 2 * dx - dy
        incE = 2 * dx
        incNE = 2 * (dx - dy)
        x = x1
        y = y1
        yEnd = y2
        stepY = 1
        punto(windows, color, [x,y])
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
            punto(windows, color, [x,y])


def LineaBres2(windows, color, p_ini, p_fin):
    x1=p_ini[0]
    y1=p_ini[1]
    x2=p_fin[0]
    y2=p_fin[1]
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
        punto2(windows, color,[x,y])
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
            punto2(windows, color, [x,y])
    
    else:
        p = 2 * dx - dy
        incE = 2 * dx
        incNE = 2 * (dx - dy)
        x = x1
        y = y1
        yEnd = y2
        stepY = 1
        punto2(windows, color, [x,y])
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
            punto2(windows, color, [x,y])
    

def Rectangulo_Borde(windows, color, pos_ini, pos_fin):
    X0= pos_ini[0]
    Y0= pos_ini[1]
    X1= pos_fin[0]
    Y1= pos_fin[1]
    LineaBres2(windows, color, [X0, Y0],[X1,Y0])
    LineaBres2(windows, color, [X0, Y1],[X1,Y1])
    LineaBres2(windows, color, [X0, Y0],[X0,Y1])
    LineaBres2(windows, color, [X1, Y0],[X1,Y1])


def Rectangulo_Relleno(windows,colorb,colorr,pos_ini,pos_fin):
    X0= pos_ini[0]
    Y0= pos_ini[1]
    X1= pos_fin[0]
    Y1= pos_fin[1]
    LineaBres(windows, colorr, [X0, Y0],[X1,Y0])
    LineaBres(windows, colorr, [X0, Y1],[X1,Y1])
    LineaBres(windows, colorr, [X0, Y0],[X0,Y1])
    LineaBres(windows, colorr, [X1, Y0],[X1,Y1])
    Y0= Y0 +1
    while Y0 <Y1:
        LineaBres(windows, colorb, [X0+1, Y0],[X1-1,Y0])
        Y0=Y0+1


def Circulo(windows,colorb,xc,yc,x,y):
    punto(windows,colorb,[xc+x,yc+y])
    punto(windows,colorb,[xc-x,yc+y])
    punto(windows,colorb,[xc+x,yc-y])
    punto(windows,colorb,[xc-x,yc-y])
    punto(windows,colorb,[xc+y,yc+x])
    punto(windows,colorb,[xc-y,yc+x])
    punto(windows,colorb,[xc+y,yc-x])
    punto(windows,colorb,[xc-y,yc-x])


def CirculoBres(windows, color, xc,yc,r):
    x = 0
    y = r
    d = 3 - 2 * r
    Circulo(windows, color, xc,yc,x,y)
    while (y >= x):
        x = x + 1
        if (d > 0):
            y = y - 1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6
        Circulo(windows, color, xc,yc,x,y)
    


def TrianguloRectangulo(windows,colorb,x_ini,y_ini,base,altu):
    X0= x_ini
    Y0= y_ini
    LineaBres(windows, colorb, [X0, Y0],[X0+base,Y0])
    LineaBres(windows, colorb, [X0, Y0],[X0,Y0-altu])
    LineaBres(windows, colorb, [X0+base, Y0],[X0,Y0-altu])



def Triangulo(windows,colorb,x_ini,y_ini,base,altu):
    X0= x_ini
    Y0= y_ini
    LineaBres(windows, colorb, [X0, Y0],[X0+base,Y0])
    LineaBres(windows, colorb, [X0, Y0],[X0+(base/2),Y0-altu])
    LineaBres(windows, colorb, [X0+base, Y0],[X0+(base/2),Y0-altu])


def Pentagono(windows,colorb,x_ini,y_ini,base,altu):
    X0= x_ini
    Y0= y_ini
    LineaBres(windows, colorb, [X0, Y0],[X0+base,Y0])
    LineaBres(windows, colorb, [X0, Y0],[X0-(X0*0.1),altu])
    LineaBres(windows, colorb, [X0+base, Y0],[base+X0+(X0*0.1),altu])

    LineaBres(windows, colorb, [X0-(X0*0.1),altu],[X0+(base/2),altu-10])
    LineaBres(windows, colorb, [base+X0+(X0*0.1),altu],[X0+(base/2),altu-10])


    

pygame.init()
windows=pygame.display.set_mode((800,600))
windows.fill((255,255,255))
amarillo=np.array([255,255,0])
rojo=np.array([255,0,0])
verde=np.array([0,255,0])
azul=np.array([0,0,255])
blanco=np.array([255,255,255])
