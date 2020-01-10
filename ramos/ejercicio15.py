import libreria

def nota01():
    n1=libreria.pedir_numero("Ingrese nota1:",0,20)
    return n1

def nota02():
    n2=libreria.pedir_numero("Ingrese nota2:",0,20)
    return n2
#CALCULAR EL PROMEDIO Y VERIFICAR SI ESTA APROBADO O DESAPROBADO
def promedio(n1,n2):
    promedio=(n1+n2)/2
    alumno=libreria.pedir_nombre("ingrese nombre del alumno")
    edad=libreria.pedir_numero("ingrese edad:",1,100)
    contenido=alumno+"-"+str(edad)+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("se guardaron los datos")
    if(promedio>10):
        print("el alumno esta aprobado")
    else:
        print("el alumno esta desaprobado")
    print("el promedio es",promedio)


#  Variables
nota1,nota2,prom=0,0,0.0

# ----------------MENU PRINCIPAL---------------------
opc=0
max=4
while (opc != max):
    # 1.  Impresion del menu
    print("############# MENU ###############")
    print("1.  Ingrese Nota 01")
    print("2.  Ingrese Nota 02")
    print("3.  Calcular promedio")
    print("4.  Salir")
    print("##################################")

    # 2. Eleccion de la opcion del menu
    opc=libreria.pedir_numero("Ingrese opcion:",1,4)

    # 3. Mapeo de las opciones
    if (opc == 1):
        nota1 = nota01()
    if (opc == 2):
        nota2 = nota02()
    if (opc == 3):
        prom=promedio(nota1,nota2)

# fin_menu
print("Fin del programa")