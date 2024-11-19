#o	Solicita al usuario un número y determina si es positivo, negativo o cero.
#	Ejemplo: Entrada: -3 → Salida: "Es un número negativo".


nume=(int(input("ingresa un numero: ")))

if nume> 0:
    print("Es positivo")
elif nume < 0:
    print("Es negativo")
else:
    print("el numero es cero")
#Realizado por BDVA 