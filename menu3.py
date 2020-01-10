import libreria

def precioguitarra():
    a = libreria.pedir_numero("ingrese el precio de la guitarra: ", 0, 500)
    print("el precio es: " + str(a) + " " + "$")
    contenido = str(a) + "-" + "\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("se han guardado los datos")

def preciobateria():
    b = libreria.pedir_numero("ingrese el precio de la bateria: ", 0, 500)
    print("el precio de la bateria es: " + str(b) + " " + "$")
    contenido = str(b)
    libreria.guardar_datos("info.txt",contenido,"a")
    print("se han guardado los datos")

opc = 0
final = 3
while (opc != final):
    print("=====================================")
    print("1. GUITARRA: el precio de la guitarra")
    print("2. BATERIA: el precio de la bateria")
    print("3. SALIR: fin del programa")
    print("=====================================")

    opc = libreria.pedir_numero("ingrese la opcion : ", 1, 3)

    if (opc == 1):
        precioguitarra()

    if (opc == 2):
        preciobateria()

# fin_menu
print("Fin Del Programa")
