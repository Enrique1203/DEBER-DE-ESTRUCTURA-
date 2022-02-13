class Cola:
    def __init__ (self):
        self.lista=[]
    
    def push(self,pais):
        self.lista.append(pais)
        
    def empty (self):
        return len(self.lista) == 0
    
    def pop(self):
        if self.empty():
            return -1
        else:
            return self.lista.pop(0)
    
    def show(self):
        if self.empty():
            print("Cola vacia")
        else:                    
            for i in self.lista:
                print("- {}".format(i))
    
    def buscar(self,buscado):
        if buscado in self.lista:
            return self.lista.index(buscado)
        else:
            return -1
    
    def longitud(self):
        return len(self.lista)    
