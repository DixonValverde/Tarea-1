# Solicita calificaciones al usuario (hasta que ingrese -1) y calcula el promedio.

num1=int(input("Ingrese la primera nota: "))
num2=int(input("Ingrese la segunda nota: "))
num3=int(input("Ingrese la tercera nota: "))


termina=input("ingrese -1 para acabar el promedio")


if termina=="-1":
    promedio= (num1 + num2 + num3) / 3
    print("el pormedio es: " ,promedio)
else:
    print("el programa solo puede de 3 notas")





