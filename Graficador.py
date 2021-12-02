import math
import numpy as np
import pygame
import time
from Libreria_graficador import *

Ventana = pygame
bgcolor = 255,255,255
gris = np.array([155,155,155])
blanco = 255,255,255
verde = np.array([0,255,0])
naranja = np.array([239,127,26])
amarillo = np.array([255,255,0])
rojo = np.array([255,0,0])
verde = np.array([0,255,0])
azul = np.array([0,0,255])
blanco = np.array([255,255,255])
linecolor = 0,0,0

pygame.init()
Ventana = pygame.display.set_mode((700,560))
pygame.display.set_caption("Graficador") 
Ventana.fill(bgcolor)

LineaBres(Ventana,linecolor,[20,20],[680,20])
LineaBres(Ventana,linecolor,[20,540],[680,540])
LineaBres(Ventana,linecolor,[20,20],[20,540])
LineaBres(Ventana,linecolor,[680,20],[680,540])
LineaBres(Ventana,linecolor,[120,20],[120,540])
LineaBres(Ventana,linecolor,[580,20],[580,540])

# Cuadro 1
LineaBres(Ventana,linecolor,[30,30],[110,30])
LineaBres(Ventana,linecolor,[30,30],[30,90])
LineaBres(Ventana,linecolor,[30,90],[110,90])
LineaBres(Ventana,linecolor,[110,30],[110,90])
LineaBres(Ventana,linecolor,[40,40],[100,80])

# Cuadro 2
LineaBres(Ventana,linecolor,[30,100],[110,100])
LineaBres(Ventana,linecolor,[30,100],[30,160])
LineaBres(Ventana,linecolor,[30,160],[110,160])
LineaBres(Ventana,linecolor,[110,100],[110,160])
Rectangulo_Relleno(Ventana,blanco,linecolor,[50,110],[90,150])

# Cuadro 3
LineaBres(Ventana,linecolor,[30,170],[110,170])
LineaBres(Ventana,linecolor,[30,170],[30,230])
LineaBres(Ventana,linecolor,[30,230],[110,230])
LineaBres(Ventana,linecolor,[110,170],[110,230])
Rectangulo_Relleno(Ventana,linecolor,linecolor,[50,180],[90,220])

# Cuadro 4
LineaBres(Ventana,linecolor,[30,240],[110,240])
LineaBres(Ventana,linecolor,[30,240],[30,290])
LineaBres(Ventana,linecolor,[30,290],[110,290])
LineaBres(Ventana,linecolor,[110,240],[110,290])
CirculoBres(Ventana, linecolor,70,265,20)

# Cuadro 5
LineaBres(Ventana,linecolor,[30,300],[110,300])
LineaBres(Ventana,linecolor,[30,300],[30,350])
LineaBres(Ventana,linecolor,[30,350],[110,350])
LineaBres(Ventana,linecolor,[110,300],[110,350])
TrianguloRectangulo(Ventana,linecolor,50,340,40,30)

# Cuadro 6
LineaBres(Ventana,linecolor,[30,360],[110,360])
LineaBres(Ventana,linecolor,[30,360],[30,410])
LineaBres(Ventana,linecolor,[30,410],[110,410])
LineaBres(Ventana,linecolor,[110,360],[110,410])
Triangulo(Ventana,linecolor,50,400,40,30)

# Cuadro 7
LineaBres(Ventana,linecolor,[30,420],[110,420])
LineaBres(Ventana,linecolor,[30,420],[30,470])
LineaBres(Ventana,linecolor,[30,470],[110,470])
LineaBres(Ventana,linecolor,[110,420],[110,470])
Pentagono(Ventana,linecolor,50,460,40,440)

# Cuadro 8
LineaBres(Ventana,linecolor,[30,480],[110,480])
LineaBres(Ventana,linecolor,[30,480],[30,530])
LineaBres(Ventana,linecolor,[30,530],[110,530])
LineaBres(Ventana,linecolor,[110,480],[110,530])
LineaBres(Ventana,linecolor,[50,500],[80,500])
LineaBres(Ventana,linecolor,[50,510],[80,510])
LineaBres(Ventana,linecolor,[50,500],[50,510])
LineaBres(Ventana,linecolor,[80,500],[80,510])
LineaBres(Ventana,linecolor,[60,500],[60,510])
LineaBres(Ventana,linecolor,[70,500],[70,510])
LineaBres(Ventana,linecolor,[80,500],[90,505])
LineaBres(Ventana,linecolor,[80,510],[90,505])


# Cuadro 1 color amarillo
Rectangulo_Relleno(Ventana,amarillo,linecolor,[590,30],[670,90])

# Cuadro 2 color azul
Rectangulo_Relleno(Ventana,azul,linecolor,[590,100],[670,160])


# Cuadro 3 color rojo
Rectangulo_Relleno(Ventana,rojo,linecolor,[590,170],[670,230])

# Cuadro 4 color verde
Rectangulo_Relleno(Ventana,verde,linecolor,[590,240],[670,290])

# Cuadro 5 color naranja
Rectangulo_Relleno(Ventana,naranja,linecolor,[590,300],[670,350])

# Cuadro 6 color blanco
Rectangulo_Relleno(Ventana,blanco,linecolor,[590,360],[670,410])

# Cuadro 7 color gris
Rectangulo_Relleno(Ventana,gris,linecolor,[590,420],[670,470])

# Cuadro 8 color negro
Rectangulo_Relleno(Ventana,linecolor,linecolor,[590,480],[670,530])

def SeleccionarColor(x,y, figura, color):
    if (x>=590 and y >= 30 and x <= 670 and y <= 90):
        color = amarillo
    
    if (x>=590 and y >= 100 and x <= 670 and y <= 160):
        color = azul

    if (x>=590 and y >= 170 and x <= 670 and y <= 230):
        color = rojo

    if (x>=590 and y >= 240 and x <= 670 and y <= 290):
        color = verde

    if (x>=590 and y >= 300 and x <= 670 and y <= 350):
        color = naranja

    if (x>=590 and y >= 360 and x <= 670 and y <= 410):
        color = blanco

    if (x>=590 and y >= 420 and x <= 670 and y <= 470):
        color = gris

    if (x>=590 and y >= 480 and x <= 670 and y <= 530):
        color = linecolor
    return (color)


def SeleccionarFigura(x,y,figura, color):
    if (x>=30 and y >= 30 and x <= 110 and y <= 90):
        figura ="Linea"
    if(x>=30 and y >= 100 and x <= 110 and y <= 160):
        figura ="Cuadro"
    if(x>=30 and y >= 170 and x <= 110 and y <= 230):
        figura ="Cuadro2"
    if(x>=30 and y >= 240 and x <= 110 and y <= 290):
        figura ="Circulo"
    if(x>=30 and y >= 300 and x <= 110 and y <= 350):
        figura ="Rectangulo"
    if(x>=30 and y >= 360 and x <= 110 and y <= 410):
        figura ="Triangulo"
    if(x>=30 and y >= 420 and x <= 110 and y <= 470):
        figura ="Pentagono"
    if(x>=30 and y >= 480 and x <= 110 and y <= 530):
        figura ="Lapiz"

    return (figura)



def main():
    figura ="Lapiz"
    color = blanco
    cont = 0

    while True:
        for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT:
                exit()
            if eventos.type == pygame.MOUSEBUTTONDOWN:
                x, y = eventos.pos
                if (x >= 20 and y >= 20 and x <= 690 and y <= 570):
                    color = SeleccionarColor(x,y,figura,color)
                    figura = SeleccionarFigura(x,y, figura,color)
                    print ("x --> ", x, "y --> ", y," ", figura," ", color)
                if ( x >= 120 and y >= 20 and x <= 580 and y <= 540):
                    if (figura =="Linea"):
                        if ( cont < 2):
                            if ( cont == 0):
                                p1 = list(eventos.pos)
                                x1 = p1[0]
                                y1 = p1[1]
                                print ("Dibuja linea punto", cont+1, "x --> ", x1, "y -->", y1)
                                print(cont)
                            if (cont == 1):
                                p2 = list(eventos.pos)
                                x2 = p2[0]
                                y2 = p2[1]
                                print ("Dibuja linea punto ", cont+1, "x --> ", x2, "y --> ", y2)
                                LineaBres2(Ventana,color, [x1,y1], [x2,y2])
                            cont += 1
                            if ( cont == 2):
                                cont = 0
                    if (figura =="Cuadro"):
                        if ( cont < 2):
                            if ( cont == 0):
                                p1 = list(eventos.pos)
                                x1 = p1[0]
                                y1 = p1[1]
                                print ("Dibuja linea punto", cont+1, "x --> ", x1, "y -->", y1)
                                print(cont)
                            if (cont == 1):
                                p2 = list(eventos.pos)
                                x2 = p2[0]
                                y2 = p2[1]
                                print ("Dibuja linea punto ", cont+1, "x --> ", x2, "y --> ", y2)
                                Rectangulo_Borde(Ventana,color, [x1,y1], [x2,y2])
                            cont += 1
                            if ( cont == 2):
                                cont = 0
                    if (figura =="Cuadro 2"):
                        if ( cont < 2):
                            if ( cont == 0):
                                p1 = list(eventos.pos)
                                x1 = p1[0]
                                y1 = p1[1]
                                print ("dibuja linea punto", cont+1, "x --> ", x1, "y -->", y1)
                                print(cont)
                            if (cont == 1):
                                p2 = list(eventos.pos)
                                x2 = p2[0]
                                y2 = p2[1]
                                print ("dibuja linea punto ", cont+1, "x --> ", x2, "y --> ", y2)
                                Rectangulo_Relleno(Ventana,color,color, [x1,y1], [x2,y2])
                            cont += 1
                            if ( cont == 2):
                                cont = 0
                    if (figura =="Circulo"):
                        if ( cont < 2):
                            if ( cont == 0):
                                p1 = list(eventos.pos)
                                x1 = p1[0]
                                y1 = p1[1]
                                print ("dibuja linea punto", cont+1, "x --> ", x1, "y -->", y1)
                                print(cont)
                            if (cont == 1):
                                p2 = list(eventos.pos)
                                x2 = p2[0]
                                y2 = p2[1]
                                print ("dibuja linea punto ", cont+1, "x --> ", x2, "y --> ", y2)
                                CirculoBres(Ventana, color,x1,y1,10)
                            cont += 1
                            if ( cont == 2):
                                cont = 0
                    if (figura =="Rectangulo"):
                        if ( cont < 2):
                            if ( cont == 0):
                                p1 = list(eventos.pos)
                                x1 = p1[0]
                                y1 = p1[1]
                                print ("dibuja linea punto", cont+1, "x --> ", x1, "y -->", y1)
                                print(cont)
                            if (cont == 1):
                                p2 = list(eventos.pos)
                                x2 = p2[0]
                                y2 = p2[1]
                                print ("dibuja linea punto ", cont+1, "x --> ", x2, "y --> ", y2)
                                TrianguloRectangulo(Ventana,color,x1,y1,x2,y2)
                            cont += 1
                            if ( cont == 2):
                                cont = 0  
                    if (figura =="Triangulo"):
                        if ( cont < 2):
                            if ( cont == 0):
                                p1 = list(eventos.pos)
                                x1 = p1[0]
                                y1 = p1[1]
                                print ("dibuja linea punto", cont+1, "x --> ", x1, "y -->", y1)
                                print(cont)
                            if (cont == 1):
                                p2 = list(eventos.pos)
                                x2 = p2[0]
                                y2 = p2[1]
                                print ("dibuja linea punto ", cont+1, "x --> ", x2, "y --> ", y2)
                                Triangulo(Ventana,color,x1,y1,x2,y2)
                            cont += 1
                            if ( cont == 2):
                                cont = 0    
                    if (figura =="Pentagono"):
                        if ( cont < 2):
                            if ( cont == 0):
                                p1 = list(eventos.pos)
                                x1 = p1[0]
                                y1 = p1[1]
                                print ("dibuja linea punto", cont+1, "x --> ", x1, "y -->", y1)
                                print(cont)
                            if (cont == 1):
                                p2 = list(eventos.pos)
                                x2 = p2[0]
                                y2 = p2[1]
                                print ("dibuja linea punto ", cont+1, "x --> ", x2, "y --> ", y2)
                                Pentagono(Ventana,color,300,500,200,440)
                            cont += 1
                            if ( cont == 2):
                                cont = 0                     
            if eventos.type == pygame.MOUSEMOTION:
                if(figura =="Lapiz"):
                    if pygame.mouse.get_pressed() == (1,0,0):
                        p1 = list(eventos.pos)
                        x1 = p1[0]
                        y1 = p1[1]
                        LineaBres2(Ventana,color, [x1,y1], [x1,y1])
    
        pygame.display.update()



pygame.display.flip()

pygame.display.update()

time.sleep(5)
main()