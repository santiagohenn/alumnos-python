import random,math

bacterias = int(input("Bacterias: "))
generaciones = int(input("Generaciones: "))

vivas = bacterias
for g in range(generaciones):
    print("Generacion",g,":",vivas)
    vivas = vivas * 2

vivas = bacterias
for g in range(generaciones):
    print("Generacion",g,":",vivas)
    vivas = vivas * 2
    muertas = 0
    for b in range(vivas):
        if random.randint(1,10) == 1:
            muertas = muertas + 1
    vivas = vivas - muertas
    

vivas = bacterias
for g in range(generaciones):
    print("Generacion",g,":",vivas)
    vivas = vivas * 2
    muertas = 0
    for b in range(vivas):
        if random.randint(1,2) == 1:
            muertas = muertas + 1
    vivas = vivas - muertas

