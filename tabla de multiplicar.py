# Solicita un número al usuario y muestra su tabla de multiplicar del 1 al 10

#Pedir el numero al usuario
num=int(input("Ponga por pantalla un numero del 1 al 10: "))

#validar solamente del 1 al 10

if num <= num <=10:
    #solamente del 1 al 10 solamente
    for b in range(1, 11):
        #multiplicar el numero que escogio el usuario y mostrar la tabla
        print(str (num)+"*"+str (b)+"="+str(num * b))

#en caso que haya puesto un numero mayor a 10 saldra este mensaje
else:
    print("Un numero del 1 al 10 porfavor: ")

