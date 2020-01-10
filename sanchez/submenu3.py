from sanchez import libreria


def verdura1():
    x  = libreria.pedir_nombre("ingrese el nombre de la verdura: ")
    contenido = x + "-"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("los datos han sido guardados")

def verdura2():
    y = libreria.pedir_nombre("ingrese el nombre de la verdura: ")
    contenido = y + "\n"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("los datos han sido guardados")

def opc_verduras():
    opc = 0
    max = 3
    while (opc != 3):
        print("========== VERDURAS ==============")
        print("1. VERDURA 1")
        print("2. VERDURA 2")
        print("3. SALIR")
        print("==================================")

        opc = libreria.pedir_numero("ingrese la opcion: ", 1, 3)

        if (opc == 1):
            verdura1()
        if (opc == 2):
            verdura2()

def opc_frutas():
    print("se escogio frutas")

opc = 0
max = 3
while (opc != max):
    print("################ MENU ################")
    print("1. VERDURAS")
    print("2. FRUTAS")
    print("3. SALIR: FIN DEL PROGRAMA")
    print("######################################")

    opc = libreria.pedir_numero("ingrese la opcion: ", 1, 3)

    if (opc == 1):
        opc_verduras()
    if (opc ==2):
        opc_frutas()
    # fin_if
# fin_while
print("fin del programa")
