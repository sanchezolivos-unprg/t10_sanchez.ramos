import libreria

def opc_cuaderno():
    print("ingreso la lista de cuaderno")

def  opc_libros():
    print("ingreso la lista de libros")

def opc_reglas():
    print("ingreso la lista de reglas")

def opc_lapiceros():
    print("ingreso la lista de lapiceros")


opc = 0
max = 5
while (opc != max):
    print("####### LISTA DE UTILES ESCOLARES ########")
    print("1. CUADERNO")
    print("2. LIBROS")
    print("3. REGLAS")
    print("4. LAPICEROS")
    print("5. SALIR: fin del programa")
    print("##########################################")

    opc = libreria.pedir_numero("ingrese la opcion: ",1, 5)

    if (opc == 1):
        opc_cuaderno()

    if (opc == 2):
        opc_libros()

    if (opc == 3):
        opc_reglas()

    if (opc == 4):
        opc_lapiceros()
# fin_menu
print("FIN DEL PROGRAMA")
