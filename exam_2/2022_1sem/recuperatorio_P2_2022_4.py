'''
Dadas las siguiente tabla de peliculas y sus datos:
Titulo          Duracion      Año de estreno
Alien           116           1979
Jurassic Park   127           1993
Harry Potter    152           2001
Avengers        143           2012

a) Construir, en el programa principal, un diccionario de peliculas, cuya clave
sea el título de la pelicula y el valor una lista con dos elementos: el primero
la duración de la pelicula y el segundo, el año de estreno. 
b) Agregar al diccionario, usando una instrucción, la pelicula Titanic,
con una duración de 195 minutos, estrenada en 1997. 
c) Imprimir, en el programa principal, el titulo, la duración y el año de estreno
de cada pelicula, separado por guiones. Utilizar un ciclo for y la instrucción print.
d) Programar una función llamada mas_vieja que tome de parametro el diccionario de
peliculas y retorne el nombre de la pelicula mas vieja. Llamar esta función desde el
programa principal e imprimir el valor de retorno con el mensaje:
“La pelicula mas vieja es ” seguido del nombre de la pelicula de mayor antiguedad.

Bonus: Programar una función llamada maraton que tome de parametro el diccionario de peliculas
e imprima cuanto tardaría en ver todas las peliculas, una atras de otra.
'''

def mas_larga(dic):
    duracion = 0
    titulo_mas_larga = ""
    for titulo in dic:
        if dic[titulo][0] > duracion:
            duracion = dic[titulo][0]
            titulo_mas_larga = titulo
    return titulo_mas_larga

def mas_vieja(dic):
    estreno = 2023
    titulo_mas_vieja = ""
    for titulo in dic:
        if dic[titulo][1] < estreno:
            estreno = dic[titulo][1]
            titulo_mas_vieja = titulo
    return titulo_mas_vieja

def maraton(dic):
    suma = 0
    for titulo in dic:
        suma = suma + dic[titulo][0]
    print("(Bonus) La maraton duraría",suma,"minutos")
        
# Programa principal

pelis = {"Alien": [116, 1979],
         "Jurassic Park": [127, 1993],
         "Harry Potter": [152, 2001],
         "Avengers": [143, 2012]}

#pelis["Batman"] = [176, 2022]
pelis["Titanic"] = [195, 1997]

for titulo in pelis:
    print(titulo,pelis[titulo][0],pelis[titulo][1],sep = "-")

print("La pelicula mas vieja es:",mas_vieja(pelis))
# print("La pelicula mas larga es",mas_larga(pelis))
maraton(pelis)
