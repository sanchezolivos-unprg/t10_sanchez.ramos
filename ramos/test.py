import libreria

assert(libreria.validar_entero("hola") == False)
assert(libreria.validar_entero("2544") == False)
assert(libreria.validar_entero(12) == True)
print("validar_entero OK")

assert (libreria.validar_rango("nombre", 1, 5) == False)
assert (libreria.validar_rango(0, 1, 5) == False)
assert (libreria.validar_rango(1, 1, 5) == True)
assert (libreria.validar_rango(2, 1, 3) == True)
assert (libreria.validar_rango(6, 1, 5) == False)
print("validar_rango ok")

assert (libreria.validar_nombre("5") == False)
assert (libreria.validar_nombre("ab") == False)
assert (libreria.validar_nombre("maria") == True)
print("validar_nombre OK")

opc=libreria.pedir_numero("Ingrese num:", 1, 2)
assert (libreria.validar_rango(opc, 1, 2) == True)
print("pedir_numero OK")
