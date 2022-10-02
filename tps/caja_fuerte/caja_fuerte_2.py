pwd = "apellido"
intentos = 0

while intentos < 3:
    user_in = input("ingrese apellido: ")

    if user_in.lower() == pwd:
        print("Acceso correcto")
        print("Dinero en cuenta: $", len(pwd)*100)
        break
    else:
        print("El usuario no existe")

    intentos = intentos + 1

if intentos >= 3:
    print("Acceso bloqueado")
