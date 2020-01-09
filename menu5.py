import libreria

def opcion_triangulo():
    print("el area del triangulo es: b.h/2")

def opcion_circulo():
    print("el area del circulo es: pi*r**2")

def opcion_cuadrado():
    print("el area del cuadrado es: lado*lado")

def opcion_rectangulo():
    print("el area del rectangulo es: ancho*haltura")

def opcion_trapecio():
    print("el area del trapecio es: (base mayor + base menor)*(haltura)/2" )

opc = 0
max = 6
while (opc != max):
    print("######### AREA DE FIGURAS GEOMETRICAS ###########")
    print("1. TRIANGULO: area del triangulo")
    print("2. CIRCULO: area del circulo")
    print("3. CUADRADO: area del cuadrado")
    print("4. RECTANGULO: area del rectangulo")
    print("5. TRAPECIO: area del trapecio")
    print("6. SALIR")
    print("#################################################")

    opc = libreria.pedir_numero("ingrese la opcion: ", 1, 6)

    if (opc == 1):
        opcion_triangulo()

    if (opc == 2):
        opcion_circulo()

    if (opc == 3):
        opcion_cuadrado()

    if (opc == 4):
        opcion_rectangulo()

    if (opc == 5):
        opcion_trapecio()

# fin_menu
print("fin del programa")
