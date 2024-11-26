#Crea una función que reciba un número y retorne True si es par y False si es impar.

#Pedimos al usuario que ingrese un numero por pantalla
num=int(input("Ingrese un numero si es par o impar:"))

if num % 2 == 0:
    print("es un par ¡True!")
else:
    print("es impar ¡False!")