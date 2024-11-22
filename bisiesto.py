#Solicita un año y determina si es bisiesto (divisible entre 4 pero no entre 100, excepto si es divisible entre 400)

#Que ponga por pantalla el año que desee
año = int(input("ponga un año que desee: "))
#la division si es divisible para 400 o no
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    #si año o no bisiesto
    print("Es un año bisiesto")
else:
    print("No es un año bisiesto")
#fin
