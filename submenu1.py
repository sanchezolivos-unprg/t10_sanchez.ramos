import libreria

def opc_game1():
    juego1 = libreria.pedir_nombre("ingrese el nombre del juego 1: ")
    contenido = juego1 + "-"
    libreria.guardar_datos("info.txt",contenido, "a")
    print("los datos han sido guardados")

def opc_game2():
    juego2 = libreria.pedir_nombre("ingrese el nombre del juego 2: ")
    contenido = juego2 + "-"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("los datos han sido guardados")

def opc_game3():
    juego3 = libreria.pedir_nombre("ingrese el nombre del juego 3: ")
    contenido = juego3 + "\n"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("los datos han sido guardados")

# submenu_1
def opc_games():
    opc = 0
    max = 4
    while (opc != max):
        print("########### GAMES DE VIDEOJUEGOS ##########")
        print("1. GAME 1")
        print("2. GAME 2")
        print("3. GAME 3")
        print("4. SALIR")
        print("###########################################")

        opc = libreria.pedir_numero("ingrese la opcion: ",1, 4)

        if (opc == 1):
            opc_game1()

        if (opc == 2):
            opc_game2()

        if (opc == 3):
            opc_game3()

def soccer_1995():
    print("se eligio el juego super mario bross")

def crash_carr():
    print("se eligio el juego crash carrera")

opc = 0
max = 4
while (opc != max):
    print("================== JUEGOS DE VIDEO JUEGOS ===================")
    print("1. SUPER MARIO BROSS")
    print("2. SOCCER 1995")
    print("3. CRASH CARRERA")
    print("4. SALIR: END THE PROGRAM")
    print("=============================================================")

    opc = libreria.pedir_numero("ingrese la opcion: ", 1, 4)

    if (opc == 1):
        opc_games()

    if (opc == 2):
        soccer_1995()

    if (opc == 3):
        crash_carr()
    # fin_if
# fin_while
print("fin del programa")
