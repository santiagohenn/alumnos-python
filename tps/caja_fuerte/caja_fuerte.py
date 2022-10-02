pwd = "apellido"
intentos = 0
user_in = input("Ingrese apellido: ") # Primer intento (intento 0)
while pwd != user_in.lower() and intentos < 2:  # Segundo y tercer intento (1 y 2)
    intentos += 1
    print("El usuario no existe")
    user_in = input("ingrese apellido: ")

if pwd == user_in.lower():
    print("Acceso correcto. Dinero en cuenta: $", len(pwd)*100)
else:
    print("El usuario no existe, acceso bloqueado")
