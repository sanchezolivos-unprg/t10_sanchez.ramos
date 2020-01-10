import libreria
def auniversidad():
    print("se eligio opcion agregar empresa")
    universidad=libreria.pedir_nombre("agregar nombre de la universidad")
    cantidad_alumnos=libreria.pedir_numero("ingresar la cantidad de alumnos",1,15000)
    contenido=universidad+"-"+str(cantidad_alumnos)+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    if(cantidad_alumnos>1000):
        print("es una universidad grande")
    else:
        print("es una universidad pequeña")
    print("los datos han sido guardados")

def lalumnos():
    datos = libreria.obtener_datos("info.txt")
    if ( datos != ""):
        print(datos)
    else:
        print("Archivo sin datos")



#MENU PRINCIPAL------>>
opc=0
max=3
while(opc!=max):
    print("#############MENU############")
    print("1. agregar universidad")
    print("2. leer  alumnos")
    print("3. salir")
    print("#############################")
    #elegir opciones del  menu
    opc=libreria.pedir_numero("ingrese opcion:",1,3)
    #elaborar el mapeo de opciones del menu
    if(opc==1):
        auniversidad()
    if(opc==2):
        lalumnos()
#fin_while

print("FIN DEL PROGRAMA")
