#--------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 1
def areaT(base, altura):
    area=(base*altura)/2
    return area

def fact(n):
    f=1
    print(f'Calculo del factorial de {n}')
    for i in range(1,n+1):
        f=f*i
    print(f'El factorial de {n} es {f}')
    return f

def Sumita(num1,num2):
    sume=num1+num2
    return sume

def coef(x,y):
    cb=(fact(x))/(fact(y)*fact(x-y))
    return cb

a=int(input('Ingrese el valor de a:'))
b=int(input('Ingrese el valor de b:'))
respuesta=coef(a,b)
print(f'El coeficiente binomial es {respuesta}')
#--------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 2
## Modulo ##
import random
def crearVector(n):
    vec=[]
    for i in range(n):
        num=random.randint(0, 10)
        vec.append(num)
    return vec

def imprimeVector(vec):
    #IMPRESION de vector de manera iterativa
    n=len(vec)
    print("IMPRESION NORMAL")
    print('[',end="")
    for i in range(n):
        if i==n-1:
            print(vec[i], end="")
        else:
            print(vec[i], end=" ")
    print(']')
#--------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 3
## Funcion_Vector.py ##
import random
def crearVector(n):
    vec=[]
    for i in range(n):
        num=random.randint(0, 10)
        vec.append(num)
    return vec

def imprimeVector(vec):
    #IMPRESION de vector de manera iterativa
    n=len(vec)
    print("IMPRESION NORMAL")
    print('[',end="")
    for i in range(n):
        if i==n-1:
            print(vec[i], end="")
        else:
            print(vec[i], end=" ")
    print(']')
    
def productoPunto(a,b):
    n=len(a)    
    suma=0
    for i in range(n):
        suma=suma+a[i]*b[i]
    return suma

def menorVector(vec):
    menor=1000
    n=len(vec)
    for i in range(n):
        if vec[i]<menor:
            menor=vec[i]
    return menor

def mayorVector(vec):
    mayor=0
    n=len(vec)
    for i in range(n):
        if vec[i]>mayor:
            mayor=vec[i]
    return mayor

def ordenaVector(vec):
    #Ordenar de menor a mayor
    n=len(vec)
    for i in range(n):
        for j in range(n-1):
            if vec[j]>vec[j+1]:
                aux=vec[j]
                vec[j]=vec[j+1]
                vec[j+1]=aux
    return vec
#--------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 4
import Funcion_Vector as fb
x=int(input('Ingrese el tamaño del vector:'))
a=fb.crearVector(x)
fb.imprimeVector(a)
b=fb.crearVector(x)
fb.imprimeVector(b)
#--------------------------------------------------------------------------------------------------------------------------
