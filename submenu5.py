import libreria

def nombre_estudiante():
    x = libreria.pedir_nombre("ingrese el nombre del estudiante: ")
    contenido = x + "-"
    libreria.guardar_datos("info.txt",contenido, "a")
    print("se han guardado los datos")

def edad_estudiante():
    y = libreria.pedir_numero("ingrese la edad del estudiante: ", 1, 100)
    contenido = str(y) + "-"
    libreria.guardar_datos("info.txt",contenido, "a")
    print("se han guardado los datos")

def carrera_profesional():
    z = libreria.pedir_nombre("ingrese el nombre de la carrera profesional: ")
    contenido = z + "\n"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("se han guardado los datos")

def datospersonales():
    opc = 0
    max = 4
    while (opc != max):
        print("============= DATOS PERSONALES ===============")
        print("1. NOMBRE")
        print("2. EDAD")
        print("3. CARRERA PROFESIONAL")
        print("4. SALIR")
        print("==============================================")

        opc = libreria.pedir_numero("ingrese la opcion: ", 1, 4)

        if (opc == 1):
            nombre_estudiante()
        if (opc == 2):
            edad_estudiante()
        if (opc == 3):
            carrera_profesional()

def datos_fisicos():
    print("se ingresaron los datos fisicos")
    contenido = "se ingresaro los datos fisicos" + "\n"

opc = 0
max = 3
while (opc != 3):
    print("############# ESTUDIANTE ###############")
    print("1. DATOS PERSONALES")
    print("2. DATOS FISICOS")
    print("3. SALIR: fin del programa")
    print("####################################")

    opc = libreria.pedir_numero("ingrese la opcion: ", 1, 3)

    if (opc == 1):
        datospersonales()
    if (opc == 2):
        datos_fisicos()
    # fin_if
# fin while
print("fin del programa")
