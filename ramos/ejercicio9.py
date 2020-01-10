import libreria
def apollogaseosa():
    print("se eligio la opcion arroz con pollo y gaseosa")
    cliente=libreria.pedir_nombre("ingrese el nombre del cliente:")
    cuenta=libreria.pedir_numero("ingrese cuenta",1,100)
    contenido=cliente+"-"+ str(cuenta) + "\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("los datos han sidos guardados")
def apollosopa():
    print("se eligio arroz con pollo y sopa")
    cliente=libreria.pedir_nombre("ingrese el nombre del cliente:")
    cuenta=libreria.pedir_numero("ingrese cuenta",1,100)
    contenido=cliente+"-"+ str(cuenta) + "\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("los datos han sidos guardados")

#SUBMENU---->
def arrozp():
    opc=0
    max=3
    print("##########SUBMENU###########")
    print("1. arroz con pollo y gaseosa")
    print("2. arroz con pollo y sopa")
    print("3. salir")
    #elegir opciones del submenu
    opc=libreria.pedir_numero("ingrese opcion:",1,3)
    #elaborar el mapeo de opciones
    if(opc==1):
        apollogaseosa()
    if(opc==2):
        apollosopa()

def ceviche():
    print("se eligio la ceviche")
def achaufa():
    print("se eligio arroz chaufa")


#MENU PRINCIPAL------>
opc=0
max=4
while(opc!=max):
    print("#########MENU##########")
    print("1.- arroz con pollo")
    print("2.- ceviche")
    print("3.- arroz chaufa")
    print("4.- salir")
    print("#######################")
    #elegir opciones del menu
    opc=libreria.pedir_numero("ingrese opcion:",1,4)
    #elaborar el mapeo de opciones
    if(opc==1):
        arrozp()
    if(opc==2):
        ceviche()
    if(opc==3):
        achaufa()
    #fin_if
#fin_while
