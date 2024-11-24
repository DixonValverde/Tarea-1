# 15) Control de acceso:
# Solicita un nombre de usuario y contraseña, y valida si ambos son correctos.
#  Permite tres intentos antes de bloquear el acceso


#Usuario y contraseñas correctamentes del programa y 3 intentos para ponerla
usereal="ADMIN"
contraseña_verdadera="1234"
intentos=3

# Por pantalla escribir usuario y contraseña

print("---------------------------------------------------")
print("******AVISO ESCRIBA CON MAYUSCULAS EL USUARIO******")
print("******************TIENES 3 INTENTOS****************")
print("---------------------------------------------------")
while intentos >0:
    user=input("porfavor ingrese su usuario: ")
    contraseña=input("porfavor ponga la contraseña : ")

    #Si el usuario y contraseña son correctos le da la bienvenido al usuario

    if user == usereal and contraseña == contraseña_verdadera:
        print("bievenido usuario", user) 
        break
    #Mensaje cuando pone mal contraseña o usuario antes lo que se le acabe los intentos
    else:
        intentos-=1
        print ("usuario y contraseña incorrecta intentelo nuevamente", intentos)

#Mensaje cuando se acabe los intentos
if intentos == 0:
    print("acceso denegado")
