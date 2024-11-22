#9.	Calculadora básica 
#	Solicita dos números y una operación (+, -, *, /) y realiza el cálculo correspondiente.
# Ejemplo: Entrada: 3, 2, '+' → Salida: "Resultado: 5".

#El ingreso de 2 numeros para la operaciones
numero1=int(input("Escriba el primer numero: "))
numero2=int(input("Escriba el segundo numero: "))
print("---------------------------------------------------------------------------------------")
#Elegir la operacion
ope=input("Eliga la siguientre operacion (SUMA + )(RESTA - ) (MULTIPLICACION * ) (DIVISION / )")
print("----------------------------------------------------------------------------------------")
#Calcular los numeros de las operaciones
if ope == "+":
    resultado= numero1 + numero2
elif ope == "-":
    resultado= numero1 - numero2
elif ope == "*":
    resultado= numero1 * numero2
elif ope == "/":
    if numero2 == 0:
#para no dividir 0
        print("no sirve el cero para una division")
    resultado= numero1 / numero2
#en caso de poner otro simbolo
else:
    print("Eliga la operacion que aparece en pantalla")
# el resultado
print("el resultado es: ",resultado)
