import libreria

def nike():
    #1.-elegir la marca de ropa
    #2.-pedir nombre del cliente
    #3.-pedir talla del cliente
    #4.- guardar datos
    print("se eligio la marca nike")
    cliente=libreria.pedir_nombre("nombre del cliente")
    talla=libreria.pedir_numero("ingrese talla",1,60)
    contenido=cliente+"-->"+str(talla)+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("los datos han sido guardados")
def adidas():
    print("se eligio la marca adidas")

#MENU PRINCIPAL ----->
opc=0
max=3
while(opc!=max):
    print("#############MENU##########")
    print("1. marca nike")
    print("2. marca adidad")
    print("3. salir")
    #eligir opciones del menu
    opc=libreria.pedir_numero("ingrese opcion:",1,3)
    #elaborar el mapeo de opciones del menu
    if(opc==1):
        nike()
    if(opc==2):
        adidas()
#fin_while
