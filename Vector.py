#Elaborar una funcion que permita sumar los datos de un vector
#  v=[3,4,7,1,9,12,8,1]

v=[3,4,7,1,15,12,8,1,2,9]

def suma(v,n):
    i=0
    s=0
    while(i<n):
        s=v[i]+s
        i=i+1
    return(s)


#Funcion que retorna el mayor valor de un vector


def mayor(v,n):
    m=v[0] 
    i=0
    while(i<n):
        if(v[i]>=m):
            m=v[i]
        i=i+1
    return m

print("El vector es:",v)
x=suma(v,10)
print("La suma del vector es:",x)
r=mayor(v,10)
print("El mayor elemento del vector es:",r)


