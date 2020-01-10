from sanchez import libreria


def prec_pes2020():
    x = libreria.pedir_numero("ingrese la cantidad de horas de juego: ", 1, 24)
    print("total a pagar: " + str(x * 3) + " " + "$")
    contenido = str(x) + "-"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("se guardaron los datos")

def prec_gtasanandreas():
    y = libreria.pedir_numero("ingrese la cantidad de horas de juego: ", 1, 24)
    print("total a pagar: " + str(y * 2) + " " + "$")
    contenido = str(y) + "-"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("se guardaron los datos")

def prec_leftfordead():
    z = libreria.pedir_numero("ingrese la cantidad de horas de juego: ", 1, 24)
    print("total a pagar: " + str(z * 2.5) + " " + "$")
    contenido = str(z) + "\n"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("se guardaron los datos")

opc = 0
end = 4
while (opc != end):
    print("############ GAMES EN PLAY STATION 4 ##############")
    print("1. PES 2020: precio por horas")
    print("2. GTA SAN ANDREAS: precio por horas")
    print("3. LEFT FOR DEAD: precio por horas ")
    print("4. SALIR ")
    print("###################################################")

    opc = libreria.pedir_numero("ingrese la opcion: ", 1, 4)

    if (opc == 1):
        # la hora por jugar el pes 2020 es de 3 soles
        prec_pes2020()

    if (opc == 2):
        # la hora por jugar el GTA SAN ANDREAS es de 2 soles
        prec_gtasanandreas()

    if (opc == 3):
        # la hora por jugar LEFT FOR DEAD es de 2.50 soles.
        prec_leftfordead()

# fin_menu
print("fin del programa")
