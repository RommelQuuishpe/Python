#--------------------------------------------------------------------------------------------------------------------------import random
n=int(input('Ingrese el tamaño del vector:'))
vec=[]
suma=0
for i in range(n):
    num=random.randint(0,100)
    vec.append(num)
mayor=vec[0]
for i in range(n):
    suma=suma+vec[i]
    if vec[i]>mayor:
        mayor=vec[i]
        ind=i
promedio=suma/n
print(vec)
print(f'El mayor es {mayor} y se encuentra en {ind}')
print(f"El promedio es {promedio}")
#--------------------------------------------------------------------------------------------------------------------------
n=int(input('Ingrese el tamaño del Vector:'))
vec=[]

#Ingreso de datos en el vector
for i in range(n):
    num=rd.randint(0, 10)
    vec.append(num)

#IMPRESION de vector de manera iterativa
print("IMPRESION NORMAL")
print('[',end="")
for i in range(n):
    if i==n-1:
        print(vec[i], end="")
    else:
        print(vec[i], end=" ")
print(']')

#ORDENAMIENTO de vector - Método Burbuja
for i in range(n):
    for j in range(n-1):
        if vec[j]>vec[j+1]:
            vec[j],vec[j+1]=vec[j+1],vec[j]

#IMPRESION de vector de manera iterativa
print("IMPRESION ORDENADA")
print('[',end="")
for i in range(n):
    if i==n-1:
        print(vec[i], end="")
    else:
        print(vec[i], end=" ")
print(']')
#--------------------------------------------------------------------------------------------------------------------------