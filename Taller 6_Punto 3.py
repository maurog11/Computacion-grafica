from Libreria import *

MiVentana = pygame
Rojo = (255,0,0)
Amarillo = (255,255,0)
Azul = (0,0,255)
Verde = (0,255,0)
Blanco = (255,255,255)
Morado = (87,35,100)
Magenta = (207,52,118)
Naranja = (255,128,0)
Cian = (0,160,227)
Negro = (0,0,0,)

pygame.init()
MiVentana = pygame.display.set_mode((800,650))
pygame.display.set_caption("Punto 3") 


Rectangulo(MiVentana,Rojo,[124,49],[676,601]) # Cuadrado
#-------------------------------------------------------
LineaBres(MiVentana,Rojo,[400,50],[400,600]) # Lineas Vertical y Horizontal
LineaBres(MiVentana,Rojo,[124,325],[676,325]) #
#-------------------------------------------------------
LineaBres(MiVentana,Azul,[124,187],[538,601]) # Lineas Diagonales Izq-Der
LineaBres(MiVentana,Azul,[262,49],[676,463])#
#-------------------------------------------------------
LineaBres(MiVentana,Azul,[538,49],[124,463])# Lineas Diagonales Der-Izq
LineaBres(MiVentana,Azul,[676,187],[262,601])#
#-------------------------------------------------------
LineaBres(MiVentana,Azul,[262,49],[124,187])# Lineas Diagonales Pequeñas  Der-Izq
LineaBres(MiVentana,Azul,[676,463],[538,601])#
#-------------------------------------------------------
LineaBres(MiVentana,Azul,[538,49],[676,187])# Lineas Diagonales Pequeñas  Izq-Der
LineaBres(MiVentana,Azul,[124,463],[262,601])#
#------------------------------------------------------
Rectangulo(MiVentana,Rojo,[193,118],[331,256])# Cuadrados internos
Rectangulo(MiVentana,Rojo,[469,118],[607,256])#
Rectangulo(MiVentana,Rojo,[193,394],[331,532])#
Rectangulo(MiVentana,Rojo,[469,394],[607,532])#
#----------------------------------------------------
LineaBres(MiVentana,Azul,[262,118],[193,187])# Rombo 1
LineaBres(MiVentana,Azul,[331,187],[262,256])#
LineaBres(MiVentana,Azul,[262,118],[331,187])#
LineaBres(MiVentana,Azul,[193,187],[262,256])#
#----------------------------------------------------
LineaBres(MiVentana,Azul,[538,118],[469,187])# Rombo 2
LineaBres(MiVentana,Azul,[607,187],[538,256])#
LineaBres(MiVentana,Azul,[538,118],[607,187])#
LineaBres(MiVentana,Azul,[469,187],[538,256])#
#----------------------------------------------------
LineaBres(MiVentana,Azul,[262,394],[193,463])# Rombo 3
LineaBres(MiVentana,Azul,[331,463],[262,532])#
LineaBres(MiVentana,Azul,[193,463],[262,532])#
LineaBres(MiVentana,Azul,[262,394],[331,463])#
#----------------------------------------------------
LineaBres(MiVentana,Azul,[538,394],[469,463])# Rombo 4
LineaBres(MiVentana,Azul,[607,463],[538,532])#
LineaBres(MiVentana,Azul,[469,463],[538,532])#
LineaBres(MiVentana,Azul,[538,394],[607,463])#
#----------------------------------------------------
LineaBres(MiVentana,Azul,[227.5,152.5],[296.5,221.5])# Lineas Rombo 1
LineaBres(MiVentana,Azul,[296.5,152.5],[227.5,221.5])#
#------------------------------------------------------------
LineaBres(MiVentana,Azul,[503.5,152.5],[572.5,221.5])# Lineas Rombo 2
LineaBres(MiVentana,Azul,[572.5,152.5],[503.5,221.5])#
#------------------------------------------------------------
LineaBres(MiVentana,Azul,[227.5,428.5],[296.5,497.5])# Lineas Rombo 3
LineaBres(MiVentana,Azul,[296.5,428.5],[227.5,497.5])#
#------------------------------------------------------------
LineaBres(MiVentana,Azul,[503.5,428.5],[572.5,497.5])# Lineas Rombo 4
LineaBres(MiVentana,Azul,[572.5,428.5],[503.5,497.5])#


pygame.display.update()
time.sleep(10)