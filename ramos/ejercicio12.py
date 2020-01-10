import libreria

def autosdeportivos():
    print("se eligio la opcion autos deportivos")
    marca=libreria.pedir_nombre("ingrese marca")
    precio=libreria.pedir_numero("ingrese precio",1,1000000)
    contenido=marca+"-"+str(precio)+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("se guardaron los datos")
def autoscarrera():
    print("se eligio la opcion autos de carrera")
    marca=libreria.pedir_nombre("ingrese marca")
    precio=libreria.pedir_numero("ingrese precio",1,1000000)
    contenido=marca+"-"+str(precio)+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("se guardaron los datos")

#-----------------SUBMENU------------------------------------
def mautos():
    print("se eligio la opcion marca de autos")
    opc=0
    max=3
    print("###########SUBMENU##########")
    print("1. marca de autos deportivos")
    print("2. marca de autos de carrera")
    print("3. salir")
    print("############################")
    #elegir opciones del submenu
    opc=libreria.pedir_numero("ingrese opcion",1,3)
    #elaborar el mapeo de opciones del submenu
    if(opc==1):
        autosdeportivos()
    if(opc==2):
        autoscarrera()


def leermarca():
    print("se eligio la opcion leer marca de autos")

opc=0
max=3
while(opc!=max):
    print("###########MENU##########")
    print("1. marca de autos")
    print("2. leer marca de autos")
    print("3. salir")
    print("##########################")
    #eligir opciones del menu
    opc=libreria.pedir_numero("ingrese opcion:",1,3)
    #elaborar mapeo de opciones
    if(opc==1):
        mautos()
    if(opc==2):
        leermarca()
    #fin_if
print("fin del programa")
