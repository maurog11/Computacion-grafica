import numpy as np
import matplotlib.pyplot as plt
from skimage import io

plt.rcParams['image.cmap']='gray'

# Punto 1
plt.figure("Capa colores")

def colores(recorrido,CantRojo,CantVerde,CantAzul,pos):
    imagenRGB=io.imread(recorrido)/255
    imagenNueva=np.copy(imagenRGB)
    imagenNueva[:,:,0]=CantRojo
    imagenNueva[:,:,1]=CantVerde
    imagenNueva[:,:,2]=CantAzul
    plt.subplot(3,3,pos)
    plt.imshow(imagenNueva)
    return imagenNueva


colores("blanco.jpg", 0 , 1, 1, 1)
colores("blanco.jpg", 1, 1, 1, 2)
colores("blanco.jpg", 1, 0, 0, 3)
colores("blanco.jpg", 1, 0, 1, 4)
colores("blanco.jpg", 0.5, 0.5, 0.5, 5)
colores("blanco.jpg", 0, 1, 0, 6)
colores("blanco.jpg", 1, 1, 0, 7)
colores("blanco.jpg", 0, 0, 0, 8)
colores("blanco.jpg", 0, 0, 1, 9)

# Punto 2
ImgNegra=np.zeros((20,30))
Imgdegrada=ImgNegra
multiplicativo=0.1 #d
recorrido=0 
ContadorTono=1
while(recorrido<30):
    Imgdegrada[12:,recorrido]=multiplicativo
    recorrido+=1
    ContadorTono+=1
    if ContadorTono==5:
        multiplicativo+=0.1
        ContadorTono=1

plt.figure()
plt.imshow(Imgdegrada)


# Punto 3 
imagen=io.imread("pereira.jpg")/255.0
imagenNegativo=np.copy(imagen)

def invierte(imagen):
    return 1-imagen

plt.figure("Negativo")
plt.subplot(2,2,1)
plt.imshow(imagen)
plt.subplot(2,2,2)
plt.imshow(invierte(imagenNegativo))
plt.show()


# Punto 4 
ImagenRGB = io.imread("pereira.jpg")/255

print("Tamaño de la imagen",ImagenRGB.shape)

ImagenOriginal = np.copy(ImagenRGB)
plt.title("Original")
plt.imshow(ImagenOriginal)
plt.show()

ImagenRed = np.copy(ImagenRGB)
ImagenRed[:,:,1]=0
ImagenRed[:,:,2]=0
plt.title("Capa Roja")
plt.imshow(ImagenRed)
plt.show()

# Punto 5
ImagenGreen = np.copy(ImagenRGB)
ImagenGreen[:,:,0]=0
ImagenGreen[:,:,2]=0
plt.title("Capa Verde")
plt.imshow(ImagenGreen)
plt.show()

# Punto 6
ImagenBlue = np.copy(ImagenRGB)
ImagenBlue[:,:,0]=0
ImagenBlue[:,:,1]=0
plt.title("Capa Azul")
plt.imshow(ImagenBlue)
plt.show()

# Punto 7
ImagenMagenta = np.copy(ImagenRGB)
ImagenMagenta[:,:,0]=1
ImagenMagenta[:,:,2]=1
plt.title("Capa Magenta")
plt.imshow(ImagenMagenta)
plt.show()

# Punto 8
ImagenCyan = np.copy(ImagenRGB)
ImagenCyan[:,:,1]=1
ImagenCyan[:,:,2]=1
plt.title("Capa Cyan")
plt.imshow(ImagenCyan)
plt.show()

# Punto 9
ImagenYellow= np.copy(ImagenRGB)
ImagenYellow[:,:,2]=0
plt.title("Capa Amarilla")
plt.imshow(ImagenYellow)
plt.show()

# Punto 10
plt.figure("Figura RGB")

ImagenOriginal = np.copy(ImagenRGB)
plt.subplot(2,2,1)
plt.title("Original")
plt.imshow(ImagenOriginal)

ImagenRed = np.copy(ImagenRGB)
ImagenRed[:,:,1]=0
ImagenRed[:,:,2]=0
plt.subplot(2,2,2)
plt.title("Capa Roja")
plt.imshow(ImagenRed)

ImagenGreen = np.copy(ImagenRGB)
ImagenGreen[:,:,0]=0
ImagenGreen[:,:,2]=0
plt.subplot(2,2,3)
plt.title("Capa Verde")
plt.imshow(ImagenGreen)

ImagenBlue = np.copy(ImagenRGB)
ImagenBlue[:,:,0]=0
ImagenBlue[:,:,1]=0
plt.subplot(2,2,4)
plt.title("Capa Azul")
plt.imshow(ImagenBlue)
plt.show()


# Punto 11
plt.figure()

imagenA=np.copy(imagen)
imagenb=io.imread("bote.jpg")/255.0

imb=np.copy(imagenb)

def unionImagenes(imagenA,imagenB):
    imNueva=imagenA+imagenB
    return imNueva
  
plt.subplot(3,3,1)
plt.imshow(unionImagenes(imagenA, imb))


# Punto 12
def FactorImagenes1(imagenA,imagenB,Factor):
    return imagenA*Factor+imagenB


plt.subplot(3,3,2)
plt.imshow(FactorImagenes1(imagenA, imb, 0.5))


# Punto 13
def FactorImagenes2(imagenA,imagenB,Factor):
    return imagenA*Factor+(1-Factor)*imagenB


plt.subplot(3,3,3)
plt.imshow(FactorImagenes2(imagenA, imb, -0.5))


# Punto 14
plt.figure()

R=np.copy(imagenA)
G=np.copy(imagenA)
B=np.copy(imagenA)
R[:,:,0]=1
G[:,:,1]=1
B[:,:,2]=1

def promedio(imagenA):
    plt.subplot(3,3,1)
    return (R+G+B)/3
plt.imshow(promedio(imagenA))

# Punto 15
plt.figure("Average")
imageGris=np.copy(imagen)
imageGris.shape
plt.subplot(3,3,1)
plt.imshow(imageGris)


def averageGris(imageGris):
    R=imageGris[:,:,0]
    G=imageGris[:,:,1]
    B=imageGris[:,:,2]
    plt.subplot(3,3,2)
    return (R+G+B)/3

plt.imshow(averageGris(imageGris))    


# Punto 16
def luminosidad(imageGris):
    R=imageGris[:,:,0]
    G=imageGris[:,:,1]
    B=imageGris[:,:,2]
    plt.subplot(3,3,3)
    return 0.299*R +0.587*G+0.114*B


plt.imshow(luminosidad(imageGris))  

# Punto 17
def tonalidad(imageGris):
    R=imageGris[:,:,0]
    G=imageGris[:,:,1]
    B=imageGris[:,:,2]
    plt.subplot(3,3,4)
    return (np.max[R, G, B] + np.min[R,G,B] )/2

plt.imshow(tonalidad(imageGris))


plt.show()
