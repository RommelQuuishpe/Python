#--------------------------------------------------------------------------------------------------------------------------
n=int(input('Ingrese el número de personas:'))
i=1
acu=0
mayor=0
while i<=n:
    peso=float(input('Ingrese el peso:'))
    acu=acu+peso
    if peso>mayor:
       mayor=peso
    i=i+1
promedio=acu/n
print(f'El promedio es {promedio}')
print(f'El mayor es {mayor}')
#--------------------------------------------------------------------------------------------------------------------------
horas=int(input('Ingrese las horas:'))
tarifa=int(input('Ingrese la tarifa:'))
if horas<=1:
    precio=tarifa
elif horas>1 and horas<=3:
    precio=tarifa+(horas-1)*0.75*tarifa
elif horas>3 and horas<=5:
    precio=tarifa+2*tarifa*0.75+(horas-3)*0.50*tarifa
elif horas>5:
    precio=tarifa+2*tarifa*0.75+2*tarifa*0.50+(horas-5)*0.25*tarifa

print(f'El precio final es {precio}')
#--------------------------------------------------------------------------------------------------------------------------
n=int(input('Ingrese la cantidad de notas:'))
cont1=0
cont2=0
cont3=0
for i in range(n):
    nota=int(input('Ingrese la nota:'))
    if nota>=0 or nota<=10:
        if nota>=0 and nota<4:
            cont1=cont1+1
        elif nota>=4 and nota<7:
            cont2=cont2+1
        elif nota>=7 and nota<=10:
            cont3=cont3+1
    else:
        print('Calificación Incorrecta')
        continue
print(f'Intervalo 1:{cont1}')
print(f'Intervalo 2:{cont2}')
print(f'Intervalo 3:{cont3}')
#--------------------------------------------------------------------------------------------------------------------------