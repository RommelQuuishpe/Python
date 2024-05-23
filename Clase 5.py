#EJERCICIO 1
n=int(input('Ingrese n:'))
i=n
while i>0:
    print(f'Iteración {i}')
    i=i-1

#EJERCICIO 2
n=int(input('Ingrese n:'))
acu=0
i=1
while i<=n:
    acu=acu+i
    print(f'{i}',end=",")
    i=i+1
print(f'La suma es:{acu}')


#EJERCICIO 13
n=int(input('Ingrese n:'))
acu=0
i=1
while i<=n:
    acu=acu+i
    if i==n:
        print(f'{i}',end="")
    else:
        print(f'{i}',end=",")
    i=i+1
print(f'\nLa suma es:{acu}')

#EJERCICIO 4
n=int(input('Ingrese n:'))
acu=0
i=1
while i<=n:
    acu=acu+1/i
    if i==n:
        print(f'{1/i}',end="")
    else:
        print(f'{1/i}',end=",")
    i=i+1
print(f'\nLa suma es:{acu}')

#EJERCICIO 5
import math as mate
n=int(input('Ingrese n:'))
facto=mate.factorial(n)
print(f'\nEl factorial de {n}!={facto}')

#EJERCICIO 6
acu=1
while i<=n:
    print(f'{i}',end=" ")
    acu=acu*i
    i=i+1
print(f'\nEl factorial de {n}!={acu}')

#EJERCICIO 7
#Serie Taylor: Exponencial
import math as mt
import matplotlib.pyplot as plt
acu=0
x=int(input('Ingrese el número x:'))
n=int(input('Ingrese el número n:'))
for i in range(0,n):
    acu=acu+(x**i)/(mt.factorial(i))
    plt.plot(i, acu,'ro')
print(f'La exponencial por sumatoria es {acu}')
expo=mt.exp(x)
print(f'La exponencial real es {expo}')
plt.title('GRAFICA DE EXPONENCIAL')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.grid()
plt.show()