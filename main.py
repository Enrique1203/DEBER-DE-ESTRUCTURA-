import os
from varios import Menu
import solicitud as soli
from listas import Lista
from pilas import Pilas
from colas import Cola


men=Menu()
lis1=["1) Listas", "2) Pilas", "3) Colas","4) Salir"]
list2=["1) Push", "2) Agregar en posicion", "3) Pop", "4) Eliminar una posicion", "5) Buscar", "6) Mostrar", "7) Salir"]
list3=["1) Push", "2) Pop", "3) Buscar", "4) Longitud", "5) Mostrar", "6) Salir"]
opcion=""

while opcion != 4:
    os.system("cls")
    opcion=men.menus(lis1,"PAISES")
    
    if opcion == "1":
        lis_pais=Lista()
        opc=""
        while opc != "7":
            os.system("cls")
            opc=men.menus(list2,"PAISES EN LISTAS")
            os.system("cls")
            
            if opc == "1":
               print("*"*5,"INGRESO DE PAIS","*"*5)
               pais=soli.pedirPais()
               lis_pais.push(pais)
               input("Pais ingresado satisfactoriamente, presiones una tecla para continuar...")
            elif opc =="2":
                print("*"*5,"INGRESO DE PAIS POR POSICION","*"*5)
                if lis_pais.empty():
                    print("La lista esta vacia, se agregara en el primer elemento.")
                    pais=soli.pedirPais()
                    lis_pais.push(pais)
                else:
                    log=len(lis_pais.lista)
                    pais, pos=soli.pedirPaisPos(log)
                    lis_pais.insertar(pais, pos)
                input("Pais ingresado satisfactoriamente, presiones una tecla para continuar...")
            elif opc == "3":
                print("*"*5,"ELIMINAR PAIS","*"*5)
                pais_el=lis_pais.pop()
                if pais_el == -1:
                    print("La lista se encuenta vacia.")
                else:
                    print("El pais eliminado fue: {}".format(pais_el))
                input("Presiones una tecla para continuar...")
            elif opc == "4":
                print("*"*5,"ELIMINAR PAIS POR POSICION","*"*5)
                if lis_pais.empty():
                    print("La lista esta vacia.")
                else:
                    log=len(lis_pais.lista)
                    pos=soli.pedirPosicion(log,1)
                    eli=lis_pais.eliminar(pos)
                    print("El pais {} que se encontaba en la posicion {} ha sido eliminado".format(eli,pos))
                input("Presiones una tecla para continuar...")
            elif opc == "5":
                print("*"*5,"BUSCAR UN PAIS EN LA LISTA","*"*5)
                pais=soli.pedirPais()
                encon=lis_pais.buscar(pais)
                if encon == -1:
                    print("No se encontro en la lista.")
                else:
                    print("El pais {} se encuentra en la posicion {} de la lista.".format(pais,encon))
                input("Presiones una tecla para continuar...")
            elif opc == "6":
                print("*"*5,"MOSTRAR PAISES EN LA LISTA","*"*5)
                lis_pais.show()
                input("Presiones una tecla para continuar...")
            elif opc == "7":
                break
    
    elif opcion == "2":
        os.system("cls")
        tam=int(input("Ingrese el tamaño de la pila a trabajar: "))
        pila_pais=Pilas(tam)
        opc=""
        while opc != "6":
            os.system("cls")
            opc=men.menus(list3,"PAISES EN PILAS")
            os.system("cls")
            
            if opc == "1":
               print("*"*5,"INGRESO DE PAIS A LA PILA","*"*5)
               pais=soli.pedirPais()
               pila_pais.push(pais)
               input("Pais ingresado satisfactoriamente, presiones una tecla para continuar...")
            elif opc == "2":
                print("*"*5,"ELIMINAR PAIS DE LA PILA","*"*5)
                pais_el=pila_pais.pop()
                if pais_el == -1:
                    print("La pila se encuenta vacia.")
                else:
                    print("El pais eliminado fue: {}".format(pais_el))
                input("Presiones una tecla para continuar...")
            elif opc == "3":
                print("*"*5,"BUSCAR UN PAIS EN LA PILA","*"*5)
                pais=soli.pedirPais()
                encon=pila_pais.buscar(pais)
                if encon == -1:
                    print("No se encontro en la pila.")
                else:
                    print("El pais {} se encuentra en la posicion {} de la pila.".format(pais,encon))
                input("Presiones una tecla para continuar...")
            elif opc == "4":
                lo=pila_pais.longitud()
                print("*"*5,"LONGITUD DE LA PILA DE PAISES","*"*5)
                print("La longitud de la pila es de {} elemento(s)".format(lo))
                input("Presiones una tecla para continuar...")
            elif opc == "5":
                print("*"*5,"MOSTRAR PAISES DE LA PILA","*"*5)
                pila_pais.show()
                input("Presiones una tecla para continuar...")
            elif opc == "6":
                break
    
    elif opcion == "3":
        cola_pais=Cola()
        opc=""
        while opc != "6":
            os.system("cls")
            opc=men.menus(list3,"PAISES EN COLAS")
            os.system("cls")
            
            if opc == "1":
               print("*"*5,"INGRESO DE PAIS A LA COLA","*"*5)
               pais=soli.pedirPais()
               cola_pais.push(pais)
               input("Pais ingresado satisfactoriamente, presiones una tecla para continuar...")
            elif opc == "2":
                print("*"*5,"ELIMINAR PAIS DE LA COLA","*"*5)
                pais_el=cola_pais.pop()
                if pais_el == -1:
                    print("La cola se encuenta vacia.")
                else:
                    print("El pais eliminado fue: {}".format(pais_el))
                input("Presiones una tecla para continuar...")
            elif opc == "3":
                print("*"*5,"BUSCAR UN PAIS EN LA COLA","*"*5)
                pais=soli.pedirPais()
                encon=cola_pais.buscar(pais)
                if encon == -1:
                    print("No se encontro en la cola.")
                else:
                    print("El pais {} se encuentra en la posicion {} de la cola.".format(pais,encon))
                input("Presiones una tecla para continuar...")
            elif opc == "4":
                print("*"*5,"LONGITUD DE LA COLA DE PAISES","*"*5)
                lo=cola_pais.longitud()
                print("\nLa longitud de la cola es de {} elemento(s)\n".format(lo))
                input("Presiones una tecla para continuar...")
            elif opc == "5":
                print("*"*5,"MOSTRAR PAISES DE LA COLA","*"*5)
                cola_pais.show()
                input("Presiones una tecla para continuar...")
            elif opc == "6":
                break   
    
    elif opcion == "4":
        print("Terminando programa...")
        break             