from sanchez import libreria


def guitarra():
    x = libreria.pedir_nombre("ingrese el nombre del instrumento de cuerda: ")
    contenido = x + "-"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("se guardaron los datos")

def violin():
    y = libreria.pedir_nombre("ingrese el nombre del instrumento de cuerda: ")
    contenido = y + "-"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("se guardaron los datos")

def arpa():
    z = libreria.pedir_nombre("ingrese el nombre del instrumento de cuerda: ")
    contenido = z + "\n"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("se guardaron los datos")

def opc_instrumentos1():
    opc = 0
    max = 4
    while (opc != max):
        print("============= INTRUMENTOS DE CUERDAS ==============")
        print("1. ISTRUMENTO DE CUEDA 1")
        print("2. ISTRUMENTO DE CUEDA 2")
        print("3. ISTRUMENTO DE CUEDA 3")
        print("4. SALIR")
        print("===================================================")

        opc = libreria.pedir_numero("ingrese la opcion: ", 1, 4)

        if (opc == 1):
            guitarra()
        if (opc == 2):
            violin()
        if (opc == 3):
            arpa()

def opc_instrumentos2():
    print("se eligio el instrumentos de viento")

opc = 0
max = 3
while (opc != 3):
    print("############### INSTRUMENTOS MUSICALES ##############")
    print("1. INSTRUMENTOS DE CURDAS")
    print("2. INSTRUMENTOS DE VIENTO")
    print("3. SALIR: END OF THE PROGRAM")
    print("#####################################################")

    opc = libreria.pedir_numero("ingrese la opcion: ", 1, 3)

    if (opc == 1):
        opc_instrumentos1()
    if (opc == 2):
        opc_instrumentos2()
    # fin_if
# fin_while
print("fin del programa")
