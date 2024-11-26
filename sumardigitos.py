#Solicita un número entero y calcula la suma de sus dígitos

#solicitar el numero por pantalla
num=input("escriba un numero por pantalla: ")


#sumar los digitos ingresado
suma = sum(int(digito) for digito in num)
#que aparezca en pantalla el resultado
print("La suma de los dígitos es : " ,suma,num)
