def ultimo_planeta(lista):
    print("Quinto planeta:", lista[len(lista)-1])

def suma_letras(lista):
    cont = 0
    for planeta in lista:
        cont = cont + len(planeta)
    return cont

# Programa principal

lista = [ "Mercurio" ,  "Venus" ,  "Tierra" ,  "Marte" ]
lista.append("Jupiter")
ultimo_planeta(lista)
print("Suma de Letras:",suma_letras(lista))
