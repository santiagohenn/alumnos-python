"""
Diseñaremos un algoritmo de sorting u ordenamiento.

Dada esta lista de paises:

lista_paises = [ "Argentina", "Uruguay" , "Chile" , "Peru" , "Brasil" ]

a) Declarar la lista en nuestro programa principal, debajo de una linea comentario con el texto “Programa principal”.
b) Programar una función llamada ordenar_alfabeticamente que tome de parametro la lista
y la ordene alfabeticamente, de la A a la Z.
c) Programar una funcion llamada ordenar_largo que tome de parametro la lista y la ordene según el largo del nombre
del país, de menor a mayor.
d) Imprimir las listas ordenadas. 

"""

## SOLUCION

import random as ran

def ordenar_alfabeticamente(lista):
    for i in range(len(lista) - 1):
        for j in range(len(lista) - 1 - i):
            if lista[j] > lista[j+1]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
    return lista
        
def ordenar_largo(lista):
    for i in range(len(lista) - 1):
        for j in range(len(lista) - 1 - i):
            if len(lista[j]) > len(lista[j+1]):
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
    return lista

# Programa principal

lista_paises = [ "Argentina", "Uruguay" , "Chile" , "Peru" , "Brasil" ]
print(ordenar_alfabeticamente(lista_paises))
print(ordenar_largo(lista_paises))
