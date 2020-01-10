from sanchez import libreria


def opc_electronica():
    profesion = libreria.pedir_nombre("ingrese el nombre de la primera carrera profesional: ")
    contenido = profesion + "-"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("los datos han sido guardados")

def opc_civil():
    profesion2 = libreria.pedir_nombre("ingrese el nombre de la segunda carrera profesional: ")
    contenido = profesion2 + "-"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("los datos han sido guardados")

def opc_mecanicaelectrica():
    profesion3 = libreria.pedir_nombre("ingrese el nombre de la tercera carrera profesional: ")
    contenido = profesion3 + "-"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("los datos han sido guardados")

def opc_computinformatica():
    profesion4 = libreria.pedir_nombre("ingrese el nombre de la cuarta carrera profesional: ")
    contenido = profesion4 + "\n"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("los datos han sido guardados")

# submenu_2
def opc_carreprofesionales():
    opc = 0
    max = 5
    while (opc != max):
        print("########## CARRERAS PROFEDIONALES ##############")
        print("1. INGENIERIA ELECTRONICA")
        print("2. INGENIERIA CIVIL")
        print("3. INGENIERIA MECANICA ELECTRICA")
        print("4. INGENIERIA EN COMPUTACION E INFORMATICA")
        print("5. SALIR")
        print("################################################")

        opc = libreria.pedir_numero("ingrese la opcion: ", 1, 5)

        if (opc == 1):
            opc_electronica()
        if (opc == 2):
            opc_civil()
        if (opc == 3):
            opc_mecanicaelectrica()
        if (opc == 4):
            opc_computinformatica()

def mecanicaautomo():
    print("se eligio la opcion carrera carpinteria")

def mecaniproduccion():
    print("se eligio la opcion carrera mecanica de produccion")

opc = 0
max = 4
while (opc != max):
    print("============ CARRERAS TECNICAS ==============")
    print("1. ELECTRONICA")
    print("2. CARPINTERIA")
    print("3. MECANICA DE PRODUCCION")
    print("4. SALIR: END OF THE PROGRAM")
    print("=============================================")

    opc = libreria.pedir_numero("ingrese la opcion: ", 1, 4)

    if (opc == 1):
        opc_carreprofesionales()
    if (opc == 1):
        mecanicaautomo()
    if (opc == 1):
        mecaniproduccion()
    # fin_if
# fin_while
print("fin del programa")
