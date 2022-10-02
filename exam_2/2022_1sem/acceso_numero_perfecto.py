continuar = True
intentos = 1

while continuar:
    usuario = int(input("Ingrese el usuario: "))
    pwd = int(input("Ingrese la pwd: "))
    num = usuario + pwd

    suma = 0
    for i in range(1, int(num/2)+1):
        if num % i == 0:
            suma = suma + i

    if suma == num:
        print("Acceso correcto")
        continuar = False
        break
    else:
        intentos += 1
        if intentos > 3:
            print("Acceso bloqueado")
            continuar = False
            break
        print("Acceso incorrecto")
        
    
