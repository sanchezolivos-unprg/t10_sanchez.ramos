import libreria

def econtratado():
    print(" se eligio la opcion del empleado contratado")
    empleado=libreria.pedir_nombre("ingrese nombre del empleado")
    sueldo=libreria.pedir_numero("ingrese sueldo",1,2000)
    if(sueldo>1500):
        print("tienes bonos adicionales")
    contenido=empleado+"-->"+str(sueldo)+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("los datos han sido guardados")
def enombrado():
    print(" se eligio la opcion del empleado nombrado")
    empleado=libreria.pedir_nombre("ingrese nombre del empleado")
    sueldo=libreria.pedir_numero("ingrese sueldo",1,3000)
    if(sueldo>2500):
        print("tienes bonos adicionales")
    contenido=empleado+"-->"+str(sueldo)+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("los datos han sido guardados")

def aempleado():
    print("se eligio la opcion agregar empleado")
    opc=0
    max=3
    while(opc!=max):
        print("###############SUBMENU#############")
        print("1. empleado contratado")
        print("2. empleado nombrado")
        print("3. salir")
        print("###################################")
        #elegir opciones del submenu
        opc=libreria.pedir_numero("ingrese opcion:",1,3)
        #elaborar el mapeo de opciones del submenu
        if(opc==1):
            econtratado()
        if(opc==2):
            enombrado()

#MENU PRINCIPAL------->

def aempresa():
    print("se eligio la opcion agregar empresa")
opc=0
max=3
while(opc!=max):
    print("#############MENU############")
    print("1. agregar empleado")
    print("2. agregar empresa")
    print("3. salir")
    print("#############################")
    #eligir opciones del menu
    opc=libreria.pedir_numero("ingrese opcion:",1,3)
    #elaborar el mapeo de opciones
    if(opc==1):
        aempleado()
    if(opc==2):
        aempresa()

print("FIN DEL PROGRAMA")