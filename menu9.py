import libreria

def opc_ballet():
    print("su origen del ballet es de italia")

def opc_tango():
    print("su origen del tango es argentina")

def opc_marinera():
    print("su origen de la marinera es de peru")

def opc_pooldance():
    print("su origen del pool dance es de inglaterra")

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
