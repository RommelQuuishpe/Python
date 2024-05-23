import random
m=int(input("Ingrese las filas:"))
n=int(input("Ingrese las columnas:"))
A=[]
for i in range (m):
  filas=[]
  for j in range(n):
    num=random.randint(0,10)
    filas.append(num)
  A.append(filas)
print (A)
for i in A:
  for j in i:
    print(j, end="\t")
  print()

#suma primera fila
suma=0
for i in range(n):
  if i==0:
    for j in A[i]:
      suma+=j
print(f"La suma es {suma}")

#suma fila aleatoria
suma1=0
alea=random.randint(1,m-1)
for i in range(n):
  suma1+=A[alea][i]

print(f"La fila aletoria es {alea}")
print(f"La suma es {suma1}")

#suma diagonal
if m==n:
  diagonal=0
  for i in range(n):
    for j in range(m):
      if i==j:
        diagonal+=A[i][j]
  print(f"La suma de la diagonal es {diagonal}")
#--------------------------------------------------------------------------------------------------------------------------
import random as rd
import  matplotlib.pyplot as plt
#Definición de entradas
n=int(input('Ingrese el tamaño del Vector:'))
vec1=[]
vec2=[]

#Ingreso de datos en el vector
for i in range(n):
    num1=rd.randint(0, 10)
    vec1.append(num1)
    num2=rd.randint(0, 10)
    vec2.append(num2)
print(vec1)
print(vec2)
plt.plot(vec1,vec2, 'ro')
plt.show()
#--------------------------------------------------------------------------------------------------------------------------
import random as rd

#Definición de entradas
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

print("IMPRESION ALREVEZ")
print('[',end="")
n = len(vec)
for i in range(n-1,-1,-1):
    if i==0:
        print(vec[i], end="")
    else:
        print(vec[i], end=" ")
print(']')

print("OTRA FORMA IMPRESION ALREVEZ - FORMA ITERATIVA")
print('[',end="")
for i in range(len(vec)):
    if i==n-1:
        print(vec[-i-1], end="")
    else:
        print(vec[-i-1], end=" ")
print(']')