def validar_entero(n):
    if (isinstance(n, int)):
        return True
    else:
        return False

def validar_rango(n, ri, rf):
    if ( validar_entero(n) == True):
        if (n >= ri and n <= rf):
            return True
        else:
            return False
    else:
        return False

def pedir_numero(msg, ri, rf):
    n=""
    while( validar_rango(n, ri, rf) == False):
       n=input(msg)
       if ( n.isdigit() == True):
           n = int(n)
    #fin_while
    return n
#fin_pedir_numero

def validar_nombre(nombre):
    if ( isinstance(nombre, str)):
        if (len(nombre) >= 3):
            return True
        else:
            return False
    else:
        return False

def pedir_nombre(msg):
    nombre=""
    while ( validar_nombre(nombre) == False ):
        nombre=input(msg)
    #fin_while
    return nombre
#fin_pedir_nombre

def guardar_datos(nombre_archivo, contenido, modo):
    archivo=open(nombre_archivo, modo)
    archivo.write(contenido)
    archivo.close()

def obtener_datos(nombre_archivo):
    archivo=open(nombre_archivo)
    contenido = archivo.read()
    archivo.close()
    return contenido

def obtener_datos_lista(nombre_archivo):
    archivo=open(nombre_archivo)
    lista = archivo.readlines()
    archivo.close()
    return lista

def validar_byte(byte):
    # 1. Ocupa 8 caracteres
    if ( len(byte) != 8):
        return False

    # 2. La cadena debe ser digitos
    if ( byte.isdigit() == False ):
        return False

    # 3. Cada caracter debe ser 0 o 1
    for bit in byte:
        if ( bit != "0" and bit != "1" ):
            return False
        #fin_if
    #fin_for

    # Si llego hasta aqui, es porque es un Byte correcto
    return True
#fin_validar_byte

def pedir_byte(msg):
    byte=""
    while( validar_byte(byte) == False):
        byte=input(msg)
    return byte
#fin_pedir_byte

def mascara(bit1, bit2):
    if ( bit1 == "1" and bit2 == "1" ):
        return "1"
    else:
        return "0"

def enmascarar(byte1, byte2):
    mask=""
    for i in range(8):
        mask += mascara(byte1[i], byte2[i])
    #fin_for
    return mask
