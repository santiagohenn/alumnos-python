"""
Programaremos una cartelera de cine!.

Dadas las siguiente tabla de peliculas y sus datos:
Titulo          Duracion (minutos)          Año de estreno
Alien           116                         1979
Avatar          162                         2009
Frozen          102                         2013
Dune            156                         2021

a) Construir un diccionario de peliculas, cuya clave sea el título de la pelicula y el valor una tupla con dos elementos,
el primero la duración de la pelicula y el segundo, el año de estreno. 
b) Programar una función llamada imprimir_peliculas que tome como parametro el diccionario de peliculas e imprima su contenido,
separado por comas: “titulo,duración,año”. Ejecutar esta funcion en el programa principal. 
c) Programar una función llamada obtener_titulos que tome el diccionario de peliculas como parametro y devuelva una lista que
contenga solo los títulos de las mismas.
d) Programar una función llamada elegir_pelicula que tome de parametro la lista de titulos y devuelva un titulo al azar
(utilizar la biblioteca random). Imprimir dicho titulo con el mensaje: “La pelicula que vamos a ver es XXXXX”

Bonus: Mejorar el programa para que al final, en vez de informar solo el titulo de la pelicula elegida al azar, Imprima el titulo,
la duración y el año de la siguiente manera: “La pelicula que vamos a ver es XXXXX, dura MMM minutos y se estrenó en AAAA”
(o un mensaje similar).
"""

## SOLUCION

import random as ran

def imprimir_peliculas(pelis):
    for titulo in pelis:
        print(titulo, pelis[titulo][0], pelis[titulo][1],sep = ",")
        
def obtener_titulos(pelis):
    titulos = []
    for titulo in pelis:
        titulos.append(titulo)
    return titulos

def elegir_pelicula(titulos):
    return titulos[ran.randint(0, len(titulos) - 1)]

# Programa principal

pelis = {"Alien": (116, 1979), "Avatar": (162, 2009), "Frozen": (102, 2013), "Dune": (156, 2021)}
imprimir_peliculas(pelis)
titulos = obtener_titulos(pelis)
elegida = elegir_pelicula(titulos)
print("La pelicula que vamos a ver es",elegida)
print("(Bonus) La pelicula que vamos a ver es",elegida,", dura",pelis[elegida][0],
      "minutos y se estreno en",pelis[elegida][1])
