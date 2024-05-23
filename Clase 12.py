#--------------------------------------------------------------------------------------------------------------------------
simpsons=["Homero","Marge","Bart"]
print(simpsons[0])

print(f"El tamaño de la lista es {len(simpsons)}")
simpsons.append("Lisa")
print(simpsons)
simpsons.insert(1,"Oscar")
print(simpsons)
simpsons.remove("Oscar")
print(simpsons)
#--------------------------------------------------------------------------------------------------------------------------
#ejercicio 2
import random
vec=[]
n=int(input("Ingrese el tamaño del vector:"))

for i in range(n):
    num=random.randint(1,10)
    vec.append(num)

print(vec)

while True:
    elim=int(input("Que elemento quieres eliminar:"))
    for i in vec:
        if elim in vec:
            vec.remove(elim)
    print(vec)
    opc=str(input("Quieres eliminar más elementos(si/no):"))
    if opc=="si":
        continue
    else:
        break
#--------------------------------------------------------------------------------------------------------------------------
#Slicing en Python.
weekdays=["mon", "tues", "wed", "thurs", "fri"]
print(weekdays[2:])
#--------------------------------------------------------------------------------------------------------------------------