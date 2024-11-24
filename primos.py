#Encuentra e imprime todos los números primos entre 1 y 50

#Hacer la lista de numeros 
lista_primos = []
#Numero del 1 al 50
for num in range(1, 50):
    #Por el momento es primo
    es_primo = True
    #dividir el numero menor a el
    for i in range(2, num):
        #division a algun numero
        if num % i == 0:
            es_primo = False
            break
        #los que son primo los añadimos ala lista
    if es_primo:
        lista_primos.append(num)
print(lista_primos)