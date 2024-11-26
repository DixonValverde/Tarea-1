#Solicita el día y mes de nacimiento y determina el signo zodiacal del usuario.

#solicitar por pantalla el mes y dia de nacimiento
print("************************************************************")
mes = input("Ingrese su mes de nacimiento en letras:" )
dia = int(input("Ingrese su día de nacimiento en numeros: "))
print("************************************************************")

# verificacion del dia y mes de nacimiento

if (mes=="marzo" or mes=="abril"):
    if (dia>=1 and dia<=21):
        print("su signo es aries")
    elif (dia>=22 and dia<=30):
        print("su signo es tauro")
elif (mes=="mayo"):
    if (dia>=1 and dia<=20):
        print("su signo es tauro")
    elif (dia>=21 and dia<=31):
        print("su signo es geminis")
elif (mes=="junio"):
    if (dia>=1 and dia<=21):
        print("su signo es geminis")
    elif(dia>21 and dia <=30):
        print("su signo es cancer")
elif (mes=="julio"):
    if (dia>=1 and dia <=22):
        print("su signo es cancer")
    elif (dia>22 and dia <=31):
        print("su signo es leo")
elif (mes=="agosto"):
    if (dia>=1 and dia <=23):
        print("su signo es leo")
    elif (dia>23 and dia <=31):
        print("su signo es virgo	")
elif (mes=="septiembre"):
    if (dia>=1 and dia <=23):
        print("su signo es virgo	")
    elif(dia>23 and dia <=30):
        print("su signo es libra")
elif (mes =="octubre"):
    if (dia>=1 and dia <=23):
        print("su signo es libra")
    elif(dia>23 and dia <=31):
        print("su signo es escorpio")
elif (mes=="noviembre"):
    if (dia>=1 and dia <=22):
        print("su signo es escorpio")
    elif(dia>22 and dia <=30):
        print("su signo es Sagitario")
elif (mes=="diciembre"):
    if (dia>=1 and dia <=23):
        print("su signo es sagitario")
    elif(dia>23 and dia <=31):
        print("su signo es capricornio")
elif (mes=="enero"):
    if (dia>=1 and dia <=19):
        print("su signo es capricornio")
    elif(dia>23 and dia <=31):
        print("su signo es acuario")
elif (mes=="febrero"):
    if (dia>=1 and dia <=19):
        print("su signo es acuario")
    elif(dia>19 and dia <=29):
        print("su signo es piscis")
        # En caso de poenr mal los datos del usuario
else:
    print("Revise sus datos y intetelo de nuevo porfa")
    #Este codido fue de github pero inspirado y mejorado por mi 
    