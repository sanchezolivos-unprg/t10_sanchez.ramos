import libreria
def nikes():
    print("opcion de submenu nike sport elegida")
    cliente=libreria.pedir_nombre("nombre del cliente")
    talla=libreria.pedir_numero("ingrese talla",1,60)
    contenido=cliente+"-->"+str(talla)+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("los datos han sido guardados")

def nikev():
    print("opcion de submenu nike verano elegida")
    cliente=libreria.pedir_nombre("nombre del cliente")
    talla=libreria.pedir_numero("ingrese talla",1,60)
    contenido=cliente+"-->"+str(talla)+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("los datos han sido guardados")

#-----------------SUBMENU----------------------
def nike():
    print("se eligio a la marca nike")
    opc=0
    max=3
    while(opc!=max):
        print("##########SUBMENU#########")
        print("1. nike sport")
        print("2. nike verano")
        print("3. salir")
        print("##########################")
        #elegir opciones del submenu
        opc=libreria.pedir_numero("ingrese opcion",1,3)
        #elaborar el mapeo de opciones
        if(opc==1):
            nikes()
        if(opc==2):
            nikev()

def adidas():
    print("se eligio la opcion marca adidas")

#MENU PRINCIPAL ----->
opc=0
max=3
while(opc!=max):
    print("#############MENU##########")
    print("1. marca nike")
    print("2. marca adidad")
    print("3. salir")
    print("###########################")
    #eligir opciones del menu
    opc=libreria.pedir_numero("ingrese opcion:",1,3)
    #elaborar el mapeo de opciones del menu
    if(opc==1):
        nike()
    if(opc==2):
        adidas()

print("fin del programa")
