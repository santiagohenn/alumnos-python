'''
Dada esta lista:

	lista = [ "Argentina", "Peru" , "Rusia" , "Uruguay" , "Ecuador", "Brasil", "Marte" ]

a) Declarar la lista en nuestro programa principal, debajo de una linea comentario con el texto “Programa principal”.
b) Reemplazar, con una instrucción, el ultimo elemento de la lista por "Alemania".
c) Programar una función llamada primer_letra que tome de parametro la lista y retorne una lista que contenga la primer
letra de cada pais. Imprimir la lista que retorna esta función.
d) Programar una función llamada empieza_a que tome de parámetro la lista y devuelva la cantidad de países cuyo nombre
empieza con A. Imprimir el resultado con el mensaje “paises que empiezan con A: X”
'''

def primer_letra(lista):
    letras = []
    for pais in lista:
        letras.append(pais[0])
    return letras

def empieza_a(lista):
    cuenta = 0
    for letra in primer_letra(lista):
        if letra.lower() == "a":
            cuenta += 1
    return cuenta

# Programa principal

lista = [ "Argentina", "Peru" , "Rusia" , "Uruguay" , "Ecuador", "Brasil", "Marte" ]
lista[len(lista) - 1] = "Alemania"
print(primer_letra(lista))
cantidad = empieza_a(lista)
print("Paises que empiezan con A:",cantidad)
