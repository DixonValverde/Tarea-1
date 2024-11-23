#oSolicita una calificación numérica y devuelve la letra correspondiente:
#	90-100: A.
#	80-89: B.
#	70-79: C.
#	60-69: D.
#	Menor a 60: F.

#Lista de rangos de las calificaciones
posiciones={
    "A": range (90,101),
    "B": range (80,89),
    "C": range (70,79),
    "D": range (60,69),
    "E": range (0,59),
}
#Usuario escribe en pantalla
sistemacalifiacion=int(input("Ingresa porfavor un numero del 1 al 100 segun tu calificacion: "))

#calificar al rango que puso el usuario
for letra, rango in posiciones.items():
    if sistemacalifiacion in rango:
        print("Tu posicion de calificaciones es: ", letra)
        break
    #Si no pone el numnero correctamente
else:
    print("Porfavor ingrese un numero del 1 al 100: ")


