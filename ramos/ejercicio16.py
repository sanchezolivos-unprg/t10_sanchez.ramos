import libreria
def upublica():
    print("eligio la opcion de universidad publica")
    universidad=libreria.pedir_nombre("agregar nombre de la universidad")
    ingresar_valoracion=libreria.pedir_numero("ingresar la valoracion de la universidad",1,100)
    contenido=universidad+"-"+str(ingresar_valoracion)+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    if(ingresar_valoracion>50):
        print("la universidad tiene prestigio")
    else:
        print("la universidad no tiene prestigio")
    print("los datos han sido guardados")
def uprivada():
    print("eligio la opcion de universidad privada")
    universidad=libreria.pedir_nombre("agregar nombre de la universidad")
    ingresar_valoracion=libreria.pedir_numero("ingresar la valoracion de la universidad",1,100)
    contenido=universidad+"-"+str(ingresar_valoracion)+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    if(ingresar_valoracion>50):
        print("la universidad tiene prestigio")
    else:
        print("la universidad no tiene prestigio")
    print("los datos han sido guardados")

#--------------------SUBMENU DE OPCIONES-------------------------
def auniversidad():
    print("se eligio la opcion agregar universidad")
    opc=0
    max=3
    while(opc!=max):
        print("###################SUBMENU###################")
        print("1. universidad publica")
        print("2. universidad privada")
        print("3. salir")
        #eligir opciones del menu
        opc=libreria.pedir_numero("ingrese opcion:",1,3)
        #elaborar el mapeo de opciones
        if(opc==1):
            upublica()
        if(opc==2):
            uprivada()
        #fin_if

def luniversidad():
    datos = libreria.obtener_datos("info.txt")
    if ( datos != ""):
        print(datos)
    else:
        print("Archivo sin datos")



#---------------------------------MENU PRINCIPAL--------------------------->>
opc=0
max=3
while(opc!=max):
    print("#############MENU############")
    print("1. agregar universidad")
    print("2. leer  universidad")
    print("3. salir")
    print("#############################")
    #elegir opciones del  menu
    opc=libreria.pedir_numero("ingrese opcion:",1,3)
    #elaborar el mapeo de opciones del menu
    if(opc==1):
        auniversidad()
    if(opc==2):
        luniversidad()

print("FIN DEL PROGRAMA")
