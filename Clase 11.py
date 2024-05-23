#--------------------------------------------------------------------------------------------------------------------------import random as rd
m=int(input('Ingrese las filas:'))
n=int(input('Ingrese las columnas:'))
A=[] #INICIALIZANDO MATRIZ

#INSERTAR DATOS EN MATRIZ
for i in range(m):
    filas=[]
    for j in range(n):
        num=rd.randint(0, 10)
        filas.append(num)
    A.append(filas)

#IMPRIMIR MATRIZ
for i in range(m):
    print('[',end='')
    for j in range(n):
        if j==n-1:
            print(f'{A[i][j]}', end='')
        else:
            print(f'{A[i][j]}', end=',')
    print(']')

#SUMAR FILA ALEATORIA
alea1=rd.randint(0, m-1)
suma1=0
for j in range(n):
    suma1=suma1+A[alea1][j]
print(f'La suma de la fila {alea1} es {suma1}')

#SUMAR COLUMNA ALEATORIO
alea2=rd.randint(0, n-1)
suma2=0
for i in range(m):
    suma2=suma2+A[i][alea2]
print(f'La suma de la columna {alea2} es {suma2}')

#SUMA DIAGONAL PRINCIPAL
suma_diagonal_prin=0
if m==n:
    for i in range (m):
        for j in range (n):
            if i==j:
                suma_diagonal_prin+=A[i][j]
    print(f"La suma de la diagonal es: {suma_diagonal_prin}")
else:
    print("Solo podemos sumar la diagonal de matrices cuadradas")

#SUMA DIAGONAL SECUNDARIA
suma_diagonal_sec=0
if m==n:
    for i in range(m):
        for j in range(n):
             if i+j==n-1:
               suma_diagonal_sec+=A[i][j]
    print(f'La suma de la diagonal secundaria es {suma_diagonal_sec}')
else:
    print('No se puede sumar la diagonal de una matriz no cuadrada')


#SUMA FILAS
sumafilas=[]
sumacolumnas=[]
for i in range(m):
    sumaf=0
    for j in range(n):
        sumaf+=A[i][j]
    sumafilas.append(sumaf)
print(f"Las sumas de las filas es {sumafilas}")


#SUMA COLUMNAS
for i in range(n):
    sumac=0
    for j in range(m):
        sumac+=A[j][i]
    sumacolumnas.append(sumac)
print(f"Las sumas de las columnas es {sumacolumnas}")

#EL NUMERO MAYOR DE CADA FILA Y SU INDICE
matrizf=[]
for i in range(m):
    filas1=[]
    mayor=A[i][0]
    count=0
    for j in range(n):
        if A[i][j]>mayor:
            mayor=A[i][j]
            count=j

    filas1.append(mayor)
    filas1.append(count)
    matrizf.append(filas1)

print(f"Los números mayores son los siguientes y se encuentran en las posiciones {matrizf}")

#EL NUMERO MAYOR DE CADA COLUMNA Y SU INDICE
matrizc=[]
for i in range(n):
    columnas=[]
    mayorc=A[0][i]
    countc=0
    for j in range(m):
        if A[j][i]>mayorc:
            mayorc=A[j][i]
            countc=j
    columnas.append(mayorc)
    columnas.append(countc)
    matrizc.append(columnas)

print(f"Los números mayores son los siguientes y se encuentran en las posiciones {matrizc}")
  #--------------------------------------------------------------------------------------------------------------------------