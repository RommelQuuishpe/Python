#--------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 1
def areaT(base, altura):
    area=(base*altura)/2
    return area

print(areaT(3, 5))
x=int(input('Ingrese la base:'))
y=int(input('Ingrese la altura:'))
print(areaT(x,y))
#--------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 2
def areaT(base, altura):
    area=(base*altura)/2
    return area

def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

def Sumita(num1,num2):
    sume=num1+num2
    return sume

print(areaT(3, 5))
x=int(input('Ingrese la base:'))
y=int(input('Ingrese la altura:'))
print(areaT(x,y))
print(fact(0))
print(Sumita(7,8))
#--------------------------------------------------------------------------------------------------------------------------
## Modulo1.py ##
def areaT(base, altura):
    area=(base*altura)/2
    return area

def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

def Sumita(num1,num2):
    sume=num1+num2
    return sume

def coef(x,y):
    cb=(fact(x))/(fact(y)*fact(x-y))
    return cb
#--------------------------------------------------------------------------------------------------------------------------
## Principal.py ##
from Modulo1 import coef
print('CALCULO COEFICIENTE BINOMIAL')
a=int(input('Ingrese a:'))
b=int(input('Ingrese b:'))
coefi=coef(a,b)
print(f'El coeficiente binomial es {coefi}')
#--------------------------------------------------------------------------------------------------------------------------