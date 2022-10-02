'''
Dadas las siguiente tabla de peliculas y sus datos:
Titulo              Horario      Sala
Jurassic World      22:15        1
Top Gun             21:40        2
Dr. Strange         19:30        3
Gemelo Siniestro    17:40        1

a) Construir un diccionario de peliculas, cuya clave sea el título de la pelicula y el valor una lista con dos elementos,
el primero la hora y el segundo los minutos, para el horario de la funcion. 
b) Agregar al diccionario, utilizando una instruccion, la pelicula Lightyear, cuya función es a las 20:30
en la sala 3.
c) Programar una función llamada cartelera que tome como parametro el diccionario de peliculas e imprima la cartelera de
la siguiente forma: “Titulo de la pelicula HH:MM”
d) Programar una función llamada elegir_pelicula que tome de parametro el diccionario de peliculas y devuelva un titulo al azar
(utilizar la biblioteca random). Imprimir dicho titulo con el mensaje: “La pelicula que vamos a ver es XXXXX”

Bonus: Mejorar el programa para que al final, en vez de informar solo el titulo de la pelicula elegida al azar, Imprima el titulo
y el horario de proyeccion: “La pelicula que vamos a ver es XXXXX y se proyecta a las HH:MM en la sala X”
(o un mensaje similar).
'''

import random as ran

def cartelera(dic):
    for titulo in dic:
        print(titulo,dic[titulo][0])

def elegir_pelicula(dic):
    return ran.choice(list(dic))
        
# Programa principal

pelis = {"Jurassic World": ["22:15", 1],
         "Top Gun": ["21:40", 2],
         "Dr. Strange": ["19:30", 3],
         "Gemelo Siniestro": ["17:40", 1]}
pelis["Lightyear"] = ["20:30", 3]
cartelera(pelis)
elegida = elegir_pelicula(pelis)
print("La pelicula que vamos a ver es",elegida)
print("(Bonus) La pelicula que vamos a ver es",elegida,"y se proyecta a las",pelis[elegida][0],"en la sala",pelis[elegida][1])
