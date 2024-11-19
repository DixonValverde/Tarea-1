#	Solicita un número al usuario y determina si es par o impar.
#	Ejemplo: Entrada: 4 → Salida: "Es par".

nume = int(input("escriba un numero entero: "))
if nume == 0:
    print ("es cero..")
if nume % 2 == 0:
    print("es par!!")
else:
    print("es impar!!")

# Realizado por BDVA