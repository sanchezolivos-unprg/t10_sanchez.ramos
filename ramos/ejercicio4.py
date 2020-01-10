import libreria
def mautos():
    print("se eligio la opcion marca de autos")
    marca=libreria.pedir_nombre("ingrese marca")
    contenido=marca
    libreria.guardar_datos("info.txt",contenido,"a")
    print("se guardaron los datos")
def leermarca():
    print("se eligio la opcion leer marca de autos")

#--------------------MENU PRINCIPAL------------------
opc=0
max=3
while(opc!=max):
    print("###########MENU##########")
    print("1. marca de autos")
    print("2. leer marca de autos")
    print("3. salir")
    #eligir opciones del menu
    opc=libreria.pedir_numero("ingrese opcion:",1,3)
    #elaborar mapeo de opciones
    if(opc==1):
        mautos()
    if(opc==2):
        leermarca()
    #fin_if
print("fin del programa")
