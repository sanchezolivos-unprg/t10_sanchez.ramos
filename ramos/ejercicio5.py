import libreria
def mcelulares():
    print("se eligio la opcion marca de celulares")
    marca1=libreria.pedir_nombre("ingrese marca")
    marca2=libreria.pedir_nombre("ingrese marca2")
    contenido=marca1+"-"+marca2+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("se guardaron los datos")

def leermarca():
    print("se eligio la opcion leer marca de celulares")

#---------------------MENU---------------------------------
opc=0
max=3
while(opc!=max):
    print("###########MENU##########")
    print("1. marca de celulares")
    print("2. leer marca de celulares")
    print("3. salir")
    #eligir opciones del menu
    opc=libreria.pedir_numero("ingrese opcion:",1,3)
    #elaborar mapeo de opciones
    if(opc==1):
        mcelulares()
    if(opc==2):
        leermarca()
    #fin_if
#FIN_MENU
print("fin del programa")
