import libreria

def opc_ballet():
    print("su origen del ballet es de italia")
    contenido = "su origen del ballet es de italia" + "-"
    libreria.guardar_datos("info.txt",contenido, "a")
    print("los datos han sido guardados")

def opc_tango():
    print("su origen del tango es argentina")
    contenido = "su origen del tango es argentina" + "-"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("los datos han sido guardados")

def opc_marinera():
    print("su origen de la marinera es de peru")
    contenido = "su origen de la marinera es de peru" + "-"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("los datos han sido guardados")

def opc_pooldance():
    print("su origen del pool dance es de inglaterra")
    contenido = "su origen del pool dance es de inglaterra" + "\n"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("los datos han sido guardados")

opc = 0
max = 5
while (opc != max):
    print("########### TIPOS DE BAILE #############")
    print("1. BALLET: su origen")
    print("2. TANGO: su origen")
    print("3. MARINERA: su origen")
    print("4. POOL DANCE: su origen")
    print("5. SALIR: end of the program")
    print("########################################")

    opc = libreria.pedir_numero("ingrese la opcion: ", 1, 5)

    if (opc == 1):
        opc_ballet()

    if (opc == 2):
        opc_tango()

    if (opc == 3):
        opc_marinera()

    if (opc == 4):
        opc_pooldance()

# fin_menu
print("fin del programa")
