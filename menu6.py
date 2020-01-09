import libreria

def precio_fresa():
    a = libreria.pedir_numero("ingrese la cantidad de kilos de fresas: ", 0, 100)
    print("el total del precio de fresas es de: " + str(a * 2) + " " + "$")

def precio_platano():
    b = libreria.pedir_numero("ingrese la cantidad de kilos de platanos: ", 0, 100)
    print("el total del precio de platanos es de: " + str(b * 3) + " " + "$")

def precio_manzana():
    c = libreria.pedir_numero("ingrese la cantidad de kilos de manzanas: ", 0, 100)
    print("el total del precio de manzanas es de: " + str(c * 2) + " " + "$")

def precio_mango():
    d = libreria.pedir_numero("ingrese la cantidad de kilos de mangos: ", 0, 100)
    print("el total del precio de mangos es de: " + str(d * 3) + " " + "$")

opc = 0
max = 5
while (opc != max):
    print("############## FRUTAS ###############")
    print("1. FRESA: precio de la fresa por kilo")
    print("2. PLATANO: precio del platano por kilo")
    print("3. MANZANA: precio de la manzana por kilo")
    print("4. MANGO: precio del mango por kilo")
    print("5. SALIR: fin del programa")
    print("#####################################")

    opc = libreria.pedir_numero("ingrese la opcion: ", 1, 5)

    if (opc == 1):
        # el precio de la fresa por kilo es de 2 soles
        precio_fresa()

    if (opc == 2):
        # el precio del platano por kilo es de 3 soles
        precio_platano()

    if (opc == 3):
        # el precio de la manzana por kilo es de 2 soles
        precio_manzana()

    if (opc == 4):
        # el precio del mago por kilo es de 3 soles
        precio_mango()

# fin_menu
print("fin del programa")
