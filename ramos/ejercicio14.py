import libreria
def econstructura():
    print("se eligio la opcion de empresa constructora")
    nombre_empresa=libreria.pedir_nombre("agregar nombre empresa")
    empleados=libreria.pedir_numero("ingresar numeros de empleados",1,50000)
    ingreso_promedio=libreria.pedir_numero("ingresar el sueldo promedio de lo empleados",1,10000)
    contenido=nombre_empresa+"-"+str(empleados)+"-"+str(ingreso_promedio)+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    if(empleados>1000):
        print("la empresa es una gran empresa constructura")
    print("los datos han sido guardados")
def einmoviliaria():
    print("se eligio la opcion de empresa inmoviliaria ")
    nombre_empresa=libreria.pedir_nombre("agregar nombre empresa")
    empleados=libreria.pedir_numero("ingresar numeros de empleados",1,50000)
    ingreso_promedio=libreria.pedir_numero("ingresar el sueldo promedio de lo empleados",1,10000)
    contenido=nombre_empresa+"-"+str(empleados)+"-"+str(ingreso_promedio)+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    if(empleados<1000):
        print("es una mediana empresa inmoviliaria")


#----------------------SUBMENU----------------------------------------------------#
def aempresa():
    opc=0
    max=3
    while(opc!=max):
        print("###############SUBMENU##############")
        print("1. empresa constructura")
        print("2. empresa de inmoviliaria")
        print("3. salir")
    #elegir opciones del menu
        opc=libreria.pedir_numero("ingrese opcion",1,3)
    #elaborar el mapeo de opciones del submenu
        if(opc==1):
            econstructura()
        if(opc==2):
            einmoviliaria()



def leerempresa():
    datos = libreria.obtener_datos("info.txt")
    if ( datos != ""):
        print(datos)
    else:
        print("Archivo sin datos")



#-----------------------------------MENU PRINCIPAL----------------------------#
opc=0
max=3
while(opc!=max):
    print("#############MENU############")
    print("1. agregar empresa")
    print("2. leer empresa")
    print("3. salir")
    print("#############################")
    #elegir opciones del  menu
    opc=libreria.pedir_numero("ingrese opcion:",1,3)
    #elaborar el mapeo de opciones del menu
    if(opc==1):
        aempresa()
    if(opc==2):
        leerempresa()

print("FIN DEL PROGRAMA")
