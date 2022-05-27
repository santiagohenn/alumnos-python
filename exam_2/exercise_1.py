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

