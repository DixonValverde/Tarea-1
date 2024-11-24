#	Factorial de un número:
#	Calcula el factorial de un número ingresado por el usuario (n!).
#	Ejemplo: Entrada: 5 → Salida: 120.

#Ingresar un numero por pantalla
num=int(input("Escriba un numero que usted desee: "))

#comenzar desde 1
factorial=1
#contador
b=1

#calcular el factoria con bucle while
while (b <= num):
    #multiplicar el numero ingresado por b
    factorial=factorial * b
    #incrementar el numero 
    b=b + 1
#calculo y imprimo por pantalla lo que escribio el usuario
print ("El factorial de " + str (num) + "es: " + str(factorial))

