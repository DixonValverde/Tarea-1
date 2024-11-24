# Solicita un número entero y muestra su versión invertida

#Pedir por pantalla 2 numeros
print("-----------------------ejemplo : 15 = 51-----------------------")
numero = input("Introduce un numero que tenga 2 o mas digitos en la linea  para invertirlo: ")

#invertir el numero ingresado
invertido = numero[::-1]
print("El numero invertido es: ",invertido)