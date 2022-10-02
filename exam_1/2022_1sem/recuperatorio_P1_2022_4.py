'''
Diseñaremos un programa de rendimiento academico
Nuestro programa deberá:
a) Solicitar al usuario que ingrese cinco notas.
b) Imprimir el promedio de las cinco notas, con el mensaje “Promedio: ” seguido del promedio.
c) Encontrar e imprimir la mayor nota, con el mensaje “Mejor nota: ”, seguido de la mayor nota.
d) Si se promociona con 7 o más, imprimir la cantidad de materias promocionadas con el mensaje
“Materias promocionadas: ”
e) Si cualquier nota igual o menor a 2 es un aplazo, imprimir la cantidad de materias aplazadas
con el mensaje “Materias aplazadas: ”

Bonus: Si se promocionaron todas las materias, imprimir el mensaje “No hay que rendir finales!”
(Este programa se puede resolver usando una lista, pero no es necesario)

'''

suma = 0
mejor = -1
promo = 0
for i in range(5):
    nota = int(input("Nota: "))
    suma = suma + nota
    if nota > mejor:
        mejor = nota
    if nota >= 7:
        promo = promo + 1

print("Promedio:", suma/5)
print("Mejor nota:", mejor)

if promo >= 5:
    print("No hay que rendir finales!")
