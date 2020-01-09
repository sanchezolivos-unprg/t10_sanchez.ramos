import libreria

def nombre_alumno():
    nombre = libreria.pedir_nombre("ingrese el nombre del alumno: ")
    print("el nombre del alumno es: ", nombre)

def edad_alumno():
    edad= libreria.pedir_numero("ingrese la edad del alumno: ", 0, 80)
    print("la edad del alumno es de: " + str(edad) + " " + "Años")

def nombre_colegio():
    colegio= libreria.pedir_nombre("ingrese el nombre del colegio: ")
    print("el colegio es: ", colegio)
# fin_def

opc=0
max=4
while (opc != 4):
    print("######### DATOS DEL ALUMNO ##########")
    print("1. ALUMNO: Nombre")
    print("2. EDAD: Edad Del Alumno")
    print("3. COLEGIO: Nombre Del Colegio")
    print("4. SALIR: Fin Del Programa")
    print("#####################################")

    opc = libreria.pedir_numero("ingrese la opcion: ", 1, 4)

    if (opc == 1):
        nombre_alumno()

    if (opc == 2):
        edad_alumno()

    if (opc == 3):
        nombre_colegio()
# fin_menu

print("Fin Del Programa")

