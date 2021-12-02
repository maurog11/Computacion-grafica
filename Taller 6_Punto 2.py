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

pygame.init()
MiVentana = pygame.display.set_mode((800,650))
pygame.display.set_caption("Punto 2") 

Rectangulo(MiVentana, Morado,[210,475],[410,565]) # Rectangulo Grande Casa
Rectangulo(MiVentana, Morado,[120,474],[210,565]) # Rectangulo Pequeño Casa
LineaBres(MiVentana, Morado,[450,10],[450,565]) # Linea Central Torre
LineaBres(MiVentana, Morado,[450,110],[520,120]) # Linea Diagonal Derecha Pequeña Punta
LineaBres(MiVentana, Morado,[520,120],[580,565]) # Linea Larga Piso a Diagonal Pequeña
LineaBres(MiVentana, Morado,[450,85],[540,99]) # Linea Diagonal Derecha Grande Punta
LineaBres(MiVentana, Morado,[540,99],[520,120]) # Linea Diagonal Pequeña
LineaBres(MiVentana, Morado,[450,10],[540,99]) # Linea Union Punta Derecha
LineaBres(MiVentana, Morado,[380,120],[450,110]) # Linea Diagonal Izquierda Pequeña Punta
LineaBres(MiVentana, Morado,[360,99],[450,85]) # Linea Diagonal Izquierda Grande Punta
LineaBres(MiVentana, Morado,[360,99],[380,120]) # Linea Diagonal Pequeña
LineaBres(MiVentana, Morado,[360,99],[450,10]) # Linea Union Punta Izquierda
TrianguloEquilatero(MiVentana, Morado, [120,474], 90) # Pared
LineaBres(MiVentana, Morado,[165,397],[365,397]) # Techo Casa 
LineaBres(MiVentana, Morado,[365,397],[410,475]) # Techo Casa
LineaBres(MiVentana, Morado,[380,120],[340,397]) # Linea Larga Techo a Diagonal Pequeña
LineaBres(MiVentana, Morado,[400,565],[620,565]) # Linea Base Torre
LineaBres(MiVentana, Morado,[590,564],[620,564]) # Linea Esquina Base Torre
LineaBres(MiVentana, Morado,[100,565],[120,565]) # Linea Esquina Base Casa
LineaBres(MiVentana, Morado,[100,564],[120,564]) # Linea ESquina Base Casa
LineaBres(MiVentana, Naranja,[475,186],[476,246]) # Linea Ventana Alta Derecha
LineaBres(MiVentana, Naranja,[475,186],[510,188]) # Linea Ventana Alta Derecha
LineaBres(MiVentana, Naranja,[510,188],[511,248]) # Linea Ventana Alta Derecha
LineaBres(MiVentana, Naranja,[476,246],[511,248]) # Linea Ventana Alta Derecha
LineaBres(MiVentana, Naranja,[477,312],[478,372]) # Linea Ventana Media Derecha
LineaBres(MiVentana, Naranja,[477,312],[512,314]) # Linea Ventana Media Derecha
LineaBres(MiVentana, Naranja,[512,314],[513,374]) # Linea Ventana Media Derecha
LineaBres(MiVentana, Naranja,[478,372],[513,374]) # Linea Ventana Media Derecha
LineaBres(MiVentana, Naranja,[480,438],[481,498]) # Linea Ventana Baja Derecha
LineaBres(MiVentana, Naranja,[480,438],[515,440]) # Linea Ventana Baja Derecha
LineaBres(MiVentana, Naranja,[515,440],[516,500]) # Linea Ventana Baja Derecha
LineaBres(MiVentana, Naranja,[481,498],[516,500]) # Linea Ventana Baja Derecha
LineaBres(MiVentana, Naranja,[425,186],[424,246]) # Linea Ventana Alta Izquierda
LineaBres(MiVentana, Naranja,[390,188],[425,186]) # Linea Ventana Alta Izquierda
LineaBres(MiVentana, Naranja,[391,188],[390,248]) # Linea Ventana Alta Izquierda
LineaBres(MiVentana, Naranja,[389,248],[424,246]) # Linea Ventana Alta Izquierda
LineaBres(MiVentana, Naranja,[423,312],[422,372]) # Linea Ventana Media Izquierda
LineaBres(MiVentana, Naranja,[388,314],[423,312]) # Linea Ventana Media Izquierda
LineaBres(MiVentana, Naranja,[389,314],[388,374]) # Linea Ventana Media Izquierda
LineaBres(MiVentana, Naranja,[387,374],[422,372]) # Linea Ventana Media Izquierda
LineaBres(MiVentana, Naranja,[421,438],[420,498]) # Linea Ventana Baja Izquierda
LineaBres(MiVentana, Naranja,[390,440],[421,438]) # Linea Ventana Baja Izquierda
LineaBres(MiVentana, Naranja,[410,498],[420,498]) # Linea Ventana Baja Izquierda


pygame.display.update()
time.sleep(5)