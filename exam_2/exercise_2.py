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
