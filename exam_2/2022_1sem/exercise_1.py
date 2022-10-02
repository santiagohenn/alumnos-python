"""
Diseñaremos un algoritmo de “viralidad” para una conocida red social. 

Dadas dos listas paralelas, una con cantidad de visitas (visitas) y otra con cantidad de “me gusta” (me_gusta) que reciben una serie de
publicaciones en un día: 

lista_visitas = [1000, 2500, 5000, 150000, 200000]
lista_me_gusta = [25, 2000, 1000, 50000, 100000]

a) Declarar las listas lista_visitas y lista_me_gusta en nuestro programa principal, debajo de una linea comentario con el texto “Programa principal”.
b) Nuestra red social determina a cuantos usuarios mostrará la publicacion al dia siguiente con esta formula:

cantidad = me_gusta * ( 1 + me_gusta / visitas ) 

Programar una función llamada obtener_cantidad que tome dos parametros de entrada: visitas y cantidad de me gusta, y retorne un entero (usar int() )
para la cantidad según la formula anterior. 

d) Programar una funcion llamada computar, que tome dos listas como parametros de entrada: lista_visitas y lista_me_gusta, y devuelva (retorne)
otra lista, con las cantidades a mostrar para cada par de elementos paralelos. Sugerencia: llamar a la funcion del inciso anterior dentro de esta función.

Imprimir los datos obtenidos. Por cada publicación tendremos un mensaje como el siguiente: “XXXX visitas y XXXX me gusta, mostrar a XXXX usuarios”.
Puede programar esto en la rutina principal o en una función, como Ud. desee.
"""

## SOlUCION:

def obtener_cantidad(visitas, me_gusta):
    cantidad = me_gusta * (1 + me_gusta / visitas)
    return int(cantidad)

def computar(lista_visitas, lista_me_gusta):
    cantidades = []
    for i in range(len(lista_visitas)):
        cant = obtener_cantidad(lista_visitas[i], lista_me_gusta[i])
        cantidades.append(cant)
    return cantidades

# Programa principal

lista_visitas = [1000, 2500, 5000, 150000, 200000]
lista_me_gusta = [25, 2000, 1000, 50000, 100000]
lista_cantidades = computar(lista_visitas, lista_me_gusta)

for i in range(len(lista_visitas)):
    print(lista_visitas[i],"visitas y",lista_me_gusta[i]
          ,"me gusta, mostrar a",lista_cantidades[i],"usuarios")

