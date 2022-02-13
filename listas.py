class Lista:
    def __init__(self,):
        self.lista=[]
    #Agregar al final de la lista     
    def push(self, pais):
        self.lista.append(pais)
    
    def empty (self):
        return len(self.lista) == 0 
        
    #Agrega el dato en la posicion indicada
    def insertar(self,pais,pos):
        self.lista.insert(pos,pais)

    #Elimina el ultimo elemento de la lista y regresa el pais elimindo
    def pop(self):
        if self.empty():
            dato=-1
        else:
            dato=self.lista.pop()
        return dato
    
    #Elimina el pais de la posicion indicada 
    def eliminar(self, pos):
        dato=self.lista[pos]
        lis_aux=self.lista[0:pos]+self.lista[pos+1:]
        self.lista=lis_aux
        return dato
    
    #Busca el pais indicado
    def buscar(self, pais):
        if pais in self.lista:
            return self.lista.index(pais)
        else:
            return -1
 
    #Muestra los datos
    def show(self):
        if self.empty():
            print("La lista esta vacia.")
        else:
            for i in self.lista:
                print("-",i)
    

"""        
lis_paises=Lista(["Ecuador", "Peru"])
lis_paises.push("Mexico")
lis_paises.show()
print(lis_paises.pop())
print(lis_paises.eliminar(1))
lis_paises.show()
lis_paises.insertar("Guatemala",1)
lis_paises.show()
lis_paises.buscar("Mexico")
"""