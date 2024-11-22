#Genera un número aleatorio entre 1 y 10 y solicita al usuario que adivine el número
# Usa if para verificar si acertó o no.


#Usamos la libreria random que nos ayuda a escoger numeros aleatorios
import random
#Elige los numeros del 1 al 10
numAL=random.randint (1,11)
#mensaje que saldra en pantalla del usuario
print("---Juego tienes que adivinar un numero tienes un solo intento---")
participante=int(input("Ponga un numero del 1 al 10 que usted desee: "))

if participante==numAL:
    print("Felicitaciones has adivinado el numero")
else:
    print("Ese no es el numero", numAL )

