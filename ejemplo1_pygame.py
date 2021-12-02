import pygame
import math
import numpy as np 
import time

Amarillo=(255,255,0)
Azul=(0,0,255)
Rojo=(255,0,0)
Verde=(0,255,0)
Cian=(0,255,255)
pygame.init()
MiVentana=pygame.display.set_mode((800,600))
pygame.draw.line(MiVentana,Amarillo,(400,50),(400,550),1) # Horizontal
pygame.draw.line(MiVentana,Amarillo,(50,300),(750,300),1) # Vertical

# Vector A
VectorA=(9.40,3.42)
PosIni=(400,300)
PosFin=(PosIni[0]+VectorA[0]*10,PosIni[1]-VectorA[1]*10)
pygame.draw.line(MiVentana,Azul,PosIni,PosFin,1)
# Vector B
VectorB=(9.71,7.05)
PosIni=PosFin
PosFin=(PosIni[0]+VectorB[0]*10,PosIni[1]-VectorB[1]*10)
pygame.draw.line(MiVentana,Rojo,PosIni,PosFin,1)
# Vector C
VectorC=(6.93,4)
PosIni=PosFin
PosFin=(PosIni[0]-VectorC[0]*10,PosIni[1]-VectorC[1]*10)
pygame.draw.line(MiVentana,Verde,PosIni,PosFin,1)
# Vector D
VectorD=(40.14,2)
PosIni=PosFin
PosFin=(PosIni[0]-VectorD[0]*10,PosIni[1]-VectorD[1]*10)
pygame.draw.line(MiVentana,Cian,PosIni,PosFin,1)
# Vector E 

pygame.display.update()
time.sleep(10)