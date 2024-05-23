#--------------------------------------------------------------------------------------------------------------------------
#Ejercicio 1
import random
m=int(input("Ingrese cuantas filas desea: "))
n=int(input("Ingrese cuantas columnas desea: "))
matriz=[]
for i in range(m):
    filas=[]
    for j in range(n):
        num=random.randint(1,10)
        filas.append(num)
    matriz.append(filas)    
#Impresión matriz
for i in matriz:
    for j in i:
        print(j,end=" ")
    print()
#Medias
medias=[]
for i in range(n):
    acum=0
    for j in range(m):
        acum+=matriz[j][i]
        media=acum/m
    medias.append(media)
print(f"Las medias de las columnas son: ")
print(medias)

#Medianas
#Orden de la matriz para calcular la mediana
medianas=[]   
for e in matriz:
    for r in range(len(e)):
        for t in range(len(e)-1):
            if e[t]>e[t+1]:
                e[t],e[t+1]=e[t+1],e[t]
    print(e)
for p in range(m):
    for l in range(n):
        if n%2==0:
            mediana=(matriz[p][n//2]+matriz[p][(n//2)-1])/2  
        else:
            mediana=matriz[p][n//2]
        medianas.append(mediana)
        break

print("Las medianas de las filas son: ")
print(medianas)
#--------------------------------------------------------------------------------------------------------------------------