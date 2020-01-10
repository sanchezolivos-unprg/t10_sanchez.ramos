from sanchez import libreria


def opc_fcbarcelona():
    print("el mejor club de la liga española y del mundo")
    contenido = "el mejor club de la liga española y del mundo" + "-"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("los datos han sido guardados")

def opc_juventus():
    print("el mejor club de la liga italiana")
    contenido = "el mejor club de la liga italiana" + "-"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("los datos han sido guardados")

def opc_bayermunich():
    print("el mejor club de la liga alemana")
    contenido = "el mejor club de la liga alemana" + "-"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("los datos han sido guardados")

def opc_liverpol():
    print("el mejor club de la liga inglesa")
    contenido = "el mejor club de la liga inglesa" + "-"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("los datos han sido guardados")

def opc_realmadrid():
    print("el segundo mejor club de la liga española")
    contenido = "el segundo mejor club de la liga española" + "\n"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("los datos han sido guardados")

opc = 0
max = 6
while (opc != max):
    print("######### LOS MEJORES CLUBES DEL MUNDO #########")
    print("1. FC BARCELONA")
    print("2. JUVENTUS")
    print("3. BAYER MUNICH")
    print("4. LIVERPOL")
    print("5. REAL MADRID ")
    print("6. SALIR: end of the program")
    print("################################################")

    opc = libreria.pedir_numero("ingrese la opcion: ", 1, 6)

    if (opc == 1):
        opc_fcbarcelona()

    if (opc == 2):
        opc_juventus()

    if (opc == 3):
        opc_bayermunich()

    if (opc == 4):
        opc_liverpol()

    if (opc == 5):
        opc_realmadrid()
# fin_menu
print("fin del programa")
