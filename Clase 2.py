#EJERCICIO 1
seg=int(input("Ingrese la cantidad de segundos:"))

minu=seg//60
sobra_minu=seg%60

hora=minu//60
sobra_hora=minu%60

print(f"{hora}:{sobra_hora}:{sobra_minu}")

#EJERCICIO 2
fosforo=int(input("Ingrese la cantidad de fósforos:"))
residuo=fosforo%40

cajas=fosforo/40
sobra_cajas=fosforo%40

paquetes=cajas/30
sobra_paquetes=cajas%30

cartones=paquetes/50
sobra_cartones=paquetes%50

furgones=cartones/30
sobra_furgones=cartones%30

print(f"Sobran fósforos={residuo}")
print(f"cajas={cajas}")
print(f"Sobran cajas={sobra_cajas}")

print(f"paquetes={paquetes}")
print(f"Sobran cajas={sobra_paquetes}")

print(f"cartones={cartones}")
print(f"Sobran cajas={sobra_cartones}")

print(f"furgones={furgones}")
print(f"Sobran cajas={sobra_furgones}")
if furgones>0:
    print(f"se van a ir {furgones}")
else:
    print(f"No se va ir ningun furgon")