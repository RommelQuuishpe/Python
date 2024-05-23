#EJERCICIO 1
num=int(input("ingrese un número:"))

if num%2==0:
    print("El número es par")
else:
    print("El número es impar")

#EJERCICIO 2
print("Ecuación de primer grado")
a=int(input("Ingrese un número:"))
b=int(input("Ingrese un número:"))

if a!=0:
    x=-(b/a)
    print(x)
else:
    if b==0:
        print("Solución indeterminada")
    else:
        print("Solución imposible")

#EJERCICIO 3
print('1.- SUMA DE NUMEROS')
print('2.- MULTIPLICACION DE NUMEROS')
print('3.- DIVISION DE NUMEROS')
condicion=int(input('Ingrese un valor:'))

if condicion == 1:
    print("Suma de números")
    num1=int(input('Ingrese primer número:'))
    num2=int(input('Ingrese segundo número:'))
    suma=num1+num2
    print(f'La suma es {suma}')
elif condicion == 2:
    print("Multiplicación de números")
    num1=int(input('Ingrese primer número:'))
    num2=int(input('Ingrese segundo número:'))
    multi=num1*num2
    print(f'La suma es {multi}')
elif condicion == 3:
    print("División de Números")
    num1=int(input('Ingrese primer número:'))
    num2=int(input('Ingrese segundo número:'))
    division=num1/num2
    print(f'La suma es {division}')


else:
    print("Ingrese la opción correcta")

#EJERCICIO 4
cali=int(input("Ingrese una calificación:"))

if cali>=0 and cali<=50:
    print("La calificación es válida")
else:
    print("La calificación no es válida")

#EJERCICIO 5
edad=int(input("Ingrese su edad:"))

if edad>=18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

#EJERCICIO 6
number=int(input("Ingrese un número:"))

if number>=0:
    print("El número es positivo")
else:
    print("El número es negativo")