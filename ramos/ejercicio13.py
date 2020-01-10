import libreria
def msamsung():
    print("se eligio la opcion samsung del submenu")
    modelo1=libreria.pedir_nombre("ingrese marca")
    modelo2=libreria.pedir_nombre("ingrese marca2")
    contenido=modelo1+"-"+modelo2+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("se guardaron los datos")
def mmotorola():
    print("se eligio la opcion motorola  del submenu")
    modelo1=libreria.pedir_nombre("ingrese marca")
    modelo2=libreria.pedir_nombre("ingrese marca2")
    precio=libreria.pedir_numero("ingrese precio",1,1000)
    contenido=modelo1+"-"+modelo2+"-"+str(precio)+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("se guardaron los datos")

#-----------------------SUBMENU-------------------------#
def mcelulares():
    print("se eligio la opcion marca de celulares")
    opc=0
    max=3
    while(opc!=max):
        print("###########SUBMENU############")
        print("1. samsung")
        print("2. motorola")
        print("3. salir")
    #elegir opciones del menu
    opc=libreria.pedir_numero("ingrese opcion",1,3)
    #elaborar el mapeo de opciones del submenu
    if(opc==1):
        msamsung()
    if(opc==2):
        mmotorola()


def leermarca():
    print("se eligio la opcion leer marca de celulares")

#-----------------------MENU PRINCIPAL --------------#

opc=0
max=3
while(opc!=max):
    print("###########MENU##########")
    print("1. marca de celulares")
    print("2. leer marca de celulares")
    print("3. salir")
    print("#########################")
    #eligir opciones del menu
    opc=libreria.pedir_numero("ingrese opcion:",1,3)
    #elaborar mapeo de opciones
    if(opc==1):
        mcelulares()
    if(opc==2):
        leermarca()
    #fin_if
print("fin del programa")
