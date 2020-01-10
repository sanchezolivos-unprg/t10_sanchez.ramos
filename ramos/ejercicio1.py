import libreria
def arrozp():
    print("se eligio arroz con pollo")
    cliente=libreria.pedir_nombre("ingrese el nombre del cliente:")
    cuenta=libreria.pedir_numero("ingrese cuenta",1,100)
    contenido=cliente+"-"+ str(cuenta) + "\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("los datos han sidos guardados")
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
