#Escribe un programa que solicite una contraseña y valide si es correcta (ejemplo: contraseña fija es 12345)

#Ponemos la contraseña fija
contraseña="12345boris"

#que ponga por pantalla la contraseña correcta
contrapuesta=input("ingrese la contraseña: ")

#si la contraseña fija es igual ala contraseña puesta por pantalla dara acceso en caso contrario no
if contrapuesta == contraseña:
    print("la contraseña es la correcta tienes acceso")
else:
    print("No tienes acceso no es la contraseña")
