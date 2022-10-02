'''
Diseñaremos un programa que calculará el area y el perimetro de un cuadrado.    		(40%)  

Nuestro programa deberá:

a) Solicitar al usuario el valor del lado del cuadrado (float) y almacenarlo en
una variable.
b) Imprimir el perímetro del cuadrado (cuatro veces el lado)
c) Imprimir el area del cuadrado (lado al cuadrado)
d) Ciclar infinitamente hasta que se ingrese el valor 0 como lado.
'''
lado = int(input("Ingrese el lado del cuadrado: "))
while lado != 0:
    print("El perimetro es:", 4*lado)
    print("El area es:", lado*lado)
    lado = int(input("Ingrese el lado del cuadrado: "))
print("Programa finalizado")

