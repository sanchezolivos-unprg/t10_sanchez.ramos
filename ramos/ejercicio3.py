import libreria
def aempleado():
    print("se eligio la opcion agregar empleado")
    #1.-pedir el nombre del empleado
    #2.-pedir sueldo del empleado
    #4.- guardar datos
    empleado=libreria.pedir_nombre("ingrese nombre del empleado")
    sueldo=libreria.pedir_numero("ingrese sueldo",1,2000)
    if(sueldo>1500):
        print("tienes bonos adicionales")
    contenido=empleado+"-->"+str(sueldo)+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("los datos han sido guardados")

def aempresa():
    print("se eligio la opcion agregar empresa")
opc=0
max=4
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
    #fin_if

print("FIN DEL PROGRAMA")
