from Mi_libreria import *
plt.rcParams['image.cmap']='gray' # Permite ver imagenes en escala de grises 
Size=(20,30)
ImgNegra=np.zeros(Size)
plt.imshow(ImgNegra,vmin=0,vmax=1)
plt.show()

ImgBlanca = np.zeros(Size)
ImgDegradado = ImgBlanca 
i=0
c=1
d=0.1
while (i<50):
    j=0
    while(j<20):
        ImgDegradado[j,i]=d
        j=j+1
    i=i+1
    c=c+1
    if c==6:
        d=d+0.1
        c=1
plt.figure()
plt.imshow(ImgDegradado,vmin=0,vmax=1)