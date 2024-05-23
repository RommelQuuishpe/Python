#EJERCICIO 1
i=1
while i<6:
    print(f'{i}')
    i=i+1
#--------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 2
n=int(input('Ingrese n:'))
for i in range(1,n+1):
    if i==n:
        print(f'{i}', end="")
    else:
        print(f'{i}', end=",")

#--------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 3
#ingrese n edades por teclado, calcular la suma de las edades ingresadas y su promedio
n=int(input("Ingrese la cantidad de edades a ingresar:"))
acum_e=0
i=1
while i<=n:
    edad=int(input("Ingrese su edad:"))
    acum_e+=edad
    i+=1
prom=acum_e/n
print(f"La suma de las edades es {acum_e}")
print(f"El promedio de las edades {prom}")

#--------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 4
#Ingrese n edades por teclado, contar cuantos son mayores de edad
n=int(input("Ingrese la cantidad de edades a ingresar:"))
acum_mayor=0
i=1
contador=0
while i<=n:
    edad=int(input("Ingrese su edad:"))
    if edad>=18:
        acum_mayor+=edad
        contador+=1
    i+=1
prom=acum_mayor/contador
print(f"Hay {contador} mayores de edad")
print(f"El promedio de las edades mayores es {prom}")

#--------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 5
#Ingrese n edades por teclado, y calcule cual es el mayor y cual el menor
n=int(input("Ingrese la cantidad de edades a ingresar:"))
acum_mayor=0
i=1
contador=0
bigger=0
less=200
while i<=n:
    edad=int(input("Ingrese su edad:"))
    if edad>bigger:
        bigger=edad
    if edad<less:
        less=edad

    i+=1

print(f"El mayor de las edades es {bigger}")
print(f"El mayor de las edades es {less}")

#--------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 6
#Ingrese n edades por teclado, y calcule cual es el mayor y cual el menor de los mayores de 18
n=int(input("Ingrese la cantidad de edades a ingresar:"))
acum_mayor=0
i=1
contador=0
bigger=0
less=200
while i<=n:
    edad=int(input("Ingrese su edad:"))
    if edad>=18:
        if edad>bigger:
            bigger=edad
        if edad<less:
            less=edad
    i+=1

print(f"El mayor de las edades es {bigger}")
print(f"El mayor de las edades es {less}")

#--------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 7
#Ingrese n edades por teclado, y calcule cual es el mayor y cual el menor de los mayores de 18 y menores de 18
n=int(input("Ingrese la cantidad de edades a ingresar:"))
acum_mayor=0
i=1
contador=0
bigger=0
less=200
bigger_men18=0
less_men18=200
while i<=n:
    edad=int(input("Ingrese su edad:"))
    if edad>=18:
        if edad>bigger:
            bigger=edad
        if edad<less:
            less=edad
    else:
        if edad>bigger_men18:
            bigger_men18=edad
        if edad<less_men18:
            less_men18=edad
    i+=1
print(f"El mayor de las edades de 18 es {bigger}")
print(f"El menor de las edades de 18 es {less}")
print(f"El mayor de las edades menores 18 es {bigger_men18}")
print(f"El menor de las edades menores 18 es {less_men18}")

#--------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 8
import random
n=int(input("Ingrese la cantidad de edades a ingresar:"))
pares_cont=0
acum_pares=0
mayor_impar=0
menor_impar=150
for i in range (n):
    num=random.randint(0,100)
    if num%2==0:
        pares_cont+=1
        acum_pares+=num
    else:
        if num>mayor_impar:
            mayor_impar=num

        if num<menor_impar:
            menor_impar=num
promedio=acum_pares/pares_cont
print(f"La cantidad de pares es {pares_cont} y su promedio es {promedio}")
print(f"El mayor de los impares es {mayor_impar}")
print(f"El menor de los impares es {menor_impar}")

#--------------------------------------------------------------------------------------------------------------------------