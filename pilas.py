class Pilas: 
                   
    def __init__(self,tam):
        self.lista=[]
        self.tope=0
        self.size=tam
    
    #Agregamos un elemento
    def push(self,pais):
        if self.tope < self.size:
            self.lista += [pais]
            self.tope += 1
        else:
            print("La Pila está Llena")
    
    #Identificar si la pila esta vacia
    def empty(self):
        return self.tope == 0
    
    #Eliminar un elemento
    def pop(self):
        if self.empty():
            return -1
        else:
            top = self.lista[-1]
            self.tope -= 1
            self.lista = self.lista[:-1]
            return top

    #Regresa la longitud de la pila        
    def longitud(self):
        return self.tope
    
    #Muestra los datos en la pila    
    def show(self):
        if self.empty():
            print("Pila vacia")
        else:                    
            for tope in self.lista:
                print("- {}".format(tope))    
    
    def buscar(self,buscado):
        if buscado in self.lista:
            return self.lista.index(buscado)
        else:
            return -1
    
               
    