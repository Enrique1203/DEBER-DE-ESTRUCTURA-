def pedirPais():
    dato=input("Ingrese un pais: ")
    return dato

def pedirPosicion(longitud, op):
    if op == 1:
        longitud-=1
    while True:
        posicion=int(input("Ingrese la posicion a insertar: "))
        if posicion <= longitud and posicion>=0:
            break
        else:
            print("Posicion fuera de rango [0 al {}].".format(longitud))
    return posicion

def pedirPaisPos(longitud):
    dato=pedirPais()
    pos=pedirPosicion(longitud,0)
    return dato, pos
    
