import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import io

def Brillo(imagen,ajuste):      
    return ajuste+imagen

def CanalBrillo(imagen,ajuste,canal):
    imagen[:,:,canal]=ajuste+imagen[:,:,canal]
    return imagen

def Contraste(imagen,k,opcion):
    if opcion==1:
        return np.uint8(k*np.log(1+np.double(imagen[:,:,:])))
    elif opcion==2:
        return np.uint8(k*np.exp(np.double(imagen[:,:,:])-1))

def Binarizar(imagen,umbral):
    filas,columnas=imagen.shape[0:2]
    r=np.copy(imagen[:,:,0])
    g=np.copy(imagen[:,:,1])
    b=np.copy(imagen[:,:,2])
    def binari(canal):
        for i in range(1,filas):
            for j in range(1,columnas):
                if umbral<canal[i,j]:
                    canal[i,j]=0
                else:
                    canal[i,j]=255
        return canal 
    r=binari(r)
    g=binari(g)
    b=binari(b)
    return r*g*b

def InvertirImagen(imagen):
    return 1-imagen

def AverageGris(imageGris):
    R=imageGris[:,:,0]
    G=imageGris[:,:,1]
    B=imageGris[:,:,2]
    return (R+G+B)/3

def Cian(imagen):
  imagen[:,:,0]=1
  return imagen

def Amarillo(imagen):
    imagen[:,:,2]=1
    return imagen

def Magenta(imagen):
    imagen[:,:,1]=1
    return imagen

def Verde(imagen):
    imagen[:,:,0]=1
    imagen[:,:,2]=1
    return imagen

def Rojo(imagen):
    imagen[:,:,1]=1
    imagen[:,:,2]=1
    return imagen

def Azul(imagen):
    imagen[:,:,0]=1
    imagen[:,:,1]=1
    return imagen

def Negro(imagen):
    imagen[:,:,0]=0
    imagen[:,:,1]=0
    imagen[:,:,2]=0
    return imagen