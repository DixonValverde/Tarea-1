#   8.	Clasificación de edades
# 	Solicita una edad y clasifica al usuario como niño (0-12), adolescente (13-17) o adulto (18+)

#hacer ingresar la edad
Edad = int(input("Ingresar su edad porfavor: "))
#clasificar las edades 
#Poner una edad realmente real y logico 
if Edad < 0 or Edad >= 100:
    print ("Ingrese su edad correctamente")
elif 0<= Edad <=12:
    print("eres un niño!!")
elif 13 <= Edad <=17:
    print("un adolescente eres!!")
elif Edad >=18:
    print("Ya eres un adulto!!")



    