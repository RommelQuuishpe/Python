#EJERCICIO 1
num=float(input('Ingrese el Número:'))
if num%1==0:
    print('Sin decimal')
else:
    print('Con Decimal')

#EJERCICIO 2
nombre=input('Ingrese el user:')
passwd=input('Ingrese la clave:')
if (nombre=='renato' and passwd=='puce'):
    print('Ingrese al sistema')
else:
    print('No puedes ingresar al sistema')

#EJERCICIO 3
a=int(input('Ingrese el lado 1:'))
b=int(input('Ingrese el lado 2:'))
c=int(input('Ingrese el lado 3:'))
if a+b>c and a+c>b and b+c>a:
    print("Es triángulo")
else:
    print('No es un triángulo')

#EJERCICIO 4
A=int(input('Ingrese A:'))
B=int(input('Ingrese B:'))
C=int(input('Ingrese C:'))
if A>B:
    if A>C:
        mayor=A
    else:
        mayor=C
else:
    if B>C:
        mayor=B
    else:
        mayor=C
print(f'El mayor es {mayor}')

#EJERCICIO 5
i=5
while i>0:
    print(f'{i}',end=" ")
    i=i-1