import libreria

def opcionSumar():
    x = libreria.pedir_numero("INGRESE EL PRIMER NUMERO: ", 0, 300)
    y = libreria.pedir_numero("INGRESE EL SEGUNDO NUMERO: ", 0, 300)
    print("la suma es: ", x + y)

def opcionRestar():
    x = libreria.pedir_numero("INGRESE EL PRIMER NUMERO: ", 0, 300)
    y = libreria.pedir_numero("INGRESE EL SEGUNDO NUMERO: ", 0, 300)
    print("la resta es: ", x - y)


opc=0
fin = 3
while(opc != fin):
    print("########## ADICION Y SUTRACION ###########")
    print("1. SUMAR: suma 2 numeros")
    print("2. RESTAR: resta 2 numeros")
    print("3. SALIR: fin del programa")
    print("##########################################")

    opc = libreria.pedir_numero("ingrese su opcion: ", 1, 3)

    if ( opc == 1):
        opcionSumar()
    if (opc == 2):
        opcionRestar()

# fin_menu
print("FIN DEL PROGRAMA")
