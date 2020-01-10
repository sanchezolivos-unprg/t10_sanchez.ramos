from sanchez import libreria


# el precio de los celulares ultima generacion del 2019
def precio_samsung():
    print("el precio del celular samsung ultima generacion es de 1150 soles")
    contenido = "el precio del celular samsung ultima generacion es de 1150 soles" + "-"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("los datos han sido guardados")

def precio_huawei():
    print("el precio del celular huawei ultima generacion es de 1200 soles")
    contenido = "el precio del celular huawei ultima generacion es de 1200 soles" + "-"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("los datos han sido guardados")

def precio_iphone():
    print("el precio del celular iphone ultima generacion es de 2500 soles")
    contenido = "el precio del celular iphone ultima generacion es de 2500 soles" + "-"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("los datos han sido guardados")

def precio_motorola():
    print("el precio del celular motorola ultima generacion es de 910 soles")
    contenido = "el precio del celular motorola ultima generacion es de 910 soles" + "\n"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("los datos han sido guardados")

opc = 0
end = 5
while (opc != end):
    print("############# MARCAS DE CELULARES ##############")
    print("1. SAMSUNG: PRECIO ")
    print("2. HUAWEI: PRECIO ")
    print("3. IPHONE: PRECIO ")
    print("4. MOTOROLA: PRECIO ")
    print("5. SALIR: end of the program")
    print("################################################")

    opc = libreria.pedir_numero("ingrese la opcion: ", 1, 5)

    if (opc == 1):
        precio_samsung()

    if (opc == 2):
        precio_huawei()

    if (opc == 3):
        precio_iphone()

    if (opc == 4):
        precio_motorola()

# fin_menu
print("fin del programa")