"""
Diseñaremos un programa de apuestas. Nuestro programa deberá:
a) Solicitar al usuario que apueste el valor que tendrá de un dado, es decir, un entero del 1 a 6.
b) Generar un resultado aleatorio para un dado y determinar si el usuario ganó o no la apuesta.
Impimir “Gana” o “Pierde” según el resultado del dado y la apuesta.
c) Ciclar 5 veces, es decir, pedir 5 apuestas. Para cada apuesta, almacenar el resultado en un diccionario,
donde la clave es el numero de jugada y el dato/valor es una lista o tupla que contenga la jugada del usuario,
el resultado del dado y un string: “gana” si el usuario gana la apuesta, o “pierde” si el usuario pierde la apuesta.
c) Programar una función llamada imprimir_resultados que tome de parámetro el diccionario e imprima los resultados de
la siguiente forma: “El usuario apuesta X, el dado sale Y. El usuario gana/pierde.”. Llamar a esta función
al final del programa.

Bonus: Si el usuario recibe 5 alfajores cuando gana la apuesta, y pierde 1 alfajor cuando pierde la apuesta, definir
una función llamada calcular_balance que tome el diccionario de resultados como parametro e imprima el balance de
alfajores para la ronda de apuestas. Llamar a esta función.
"""

## SOLUCION

import random as ran

def imprimir_resultados(resultados):
    for clave in resultados:
        apuesta,dado,resultado = resultados[clave]
        print("El usuario apuesta", apuesta, "el dado sale"
              ,dado,". El usuario",resultado)

def calcular_balance(resultados):
    alfajores = 0
    for clave in resultados:
        if resultados[clave][2] == "gana":
            alfajores += 5
        else:
            alfajores -= 1
    print("(Bonus) El balance de alfajores es:",alfajores)

# Programa principal

resultados = {}

for i in range(5):

    apuesta = int(input("Apostar al dado: "))
    dado = ran.randint(1,6)
    resultado = "pierde"

    if apuesta == dado:
        resultado = "gana"

    print(resultado)
    resultados[i] = (apuesta, dado, resultado)

imprimir_resultados(resultados)
calcular_balance(resultados)
