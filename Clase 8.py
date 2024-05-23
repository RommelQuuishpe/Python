#--------------------------------------------------------------------------------------------------------------------------import random
#Definición de entradas

n=int(input('Ingrese el tamaño del Vector:'))
a=int(input("Ingrese tamaño mínimo: "))
b=int(input("Ingrese el valor máximo"))
vec=[]

#Ingreso de datos en el vector
for i in range(n):
    num=random.randint(a,b)
    vec.append(num)

#Imprimir
print("IMPRESION NORMAL")
print('[',end="")
for i in range(n):
    if i==n-1:
        print(vec[i], end="")
    else:
        print(vec[i], end=" ")
print(']')

#Ordenar de menor a mayor
for i in range(n):
    for j in range(n-1):
        if vec[j]>vec[j+1]:
            aux=vec[j]
            vec[j]=vec[j+1]
            vec[j+1]=aux

#Imprimir
print("IMPRESION ORDENADA")
print('[',end="")
for i in range(n):
    if i==n-1:
        print(vec[i], end="")
    else:
        print(vec[i], end=" ")
print(']')

#Calculo de la Mediana
if n%2==0:
    var1=n//2
    var2=(n-1)//2
    mediana=(vec[var1]+vec[var2])/2
else:
    var=n//2
    mediana=vec[var]
print(f'La mediana es {mediana}')
#--------------------------------------------------------------------------------------------------------------------------