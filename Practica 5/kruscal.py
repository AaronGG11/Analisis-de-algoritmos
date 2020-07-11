from collections import defaultdict 

class Grafo: 
    def __init__(self,vertices): 
        self.vert= vertices #Numero de vertices del grafo
        self.grafo = [] #EL grafo xd

    def addArista(self,origen,destino,peso): #se van agregando los pares de nodos al grafo 
        self.grafo.append([origen,destino,peso])
    
    def buscar(self, padre, i):
        if padre[i] == i: 
            return i 
        return self.buscar(padre, padre[i]) 

    def union(self, padre, rango, x, y): #Esta funcion hace union de dos conjuntos de x,y 
        a = self.buscar(padre, x) 
        b = self.buscar(padre, y)  
        if rango[a] < rango[b]: #agrega los arboles de rango menor a la raiz del de rango mayor
            padre[a] = b 
        elif rango[a] > rango[b]: 
            padre[b] = a 
        else :  #si su rango es el mismo, entonces uno se vuelve raiz y se incrementa el rango
            padre[b] = a 
            rango[a] += 1

    def ARM(self): 
        resultado =[]
        i = 0
        e = 0 
        padre = []
        rango = [] 
        self.grafo = sorted(self.grafo,key=lambda item: item[2], reverse = True) #Lo del key es una funcion lambda que hace el sort basandose en el peso (item[2])
        # donde self.grafo[i] es el de peso mayor
        for nodo in range(self.vert): 
            padre.append(nodo) 
            rango.append(0)  

        while e < self.vert -1 : #hace las iteraciones para ir armando el arbol (esto es el algoritmo)
            # es decir que haya una arista menos que el numero de vertices
            origen,destino,peso =  self.grafo[i] 
            i = i + 1
            x = self.buscar(padre, origen) 
            y = self.buscar(padre ,destino) 
            if x != y: #verificar que no se hagan ciclos
                e = e + 1       
                resultado.append([origen,destino,peso]) 
                self.union(padre, rango, x, y) 
                #print(rango)
                #print(padre)

        print ("El resultado para el arbol recubridor Maximo usando Kurskal es: ")

        for origen,destino,peso  in resultado: 
            print ("%d -- %d == %d" % (origen,destino,peso))
        #print(rango) 
        #print(padre)

#PRUEBAS grafo recibe el numero de vertices y se agregan las aristas en sentido origen, destino, peso
g = Grafo(9) 
g.addArista(0, 1, 4) # vertice origen, destino, valor 
g.addArista(1, 2, 8) 
g.addArista(2, 3, 7) 
g.addArista(3, 4, 9) 
g.addArista(4, 5, 10) 
g.addArista(5, 6, 2) 
g.addArista(6, 7, 1) 
g.addArista(7, 8, 7) 
g.addArista(0, 7, 8)
g.addArista(1, 7, 11) 
g.addArista(2, 8, 2) 
g.addArista(6, 8, 6) 
g.addArista(2, 5, 4)
g.addArista(3, 5, 14)
g.ARM() 
  