# --------------- Declaracion de las clases
class articulo:
    def __init__(self,existencias,peso,valor,tipo):
        self.id_tipo = tipo
        self.stock = existencias
        self.peso = peso
        self.ganancia = valor
        self.razon_peso_ganancia = valor/peso

    def quitarArticulo(self):
        if self.stock >= 1:
            self.stock -= 1
    
    def hayDisponibilidad(self):
        if self.stock >= 1:
            return True
        else:
            return False

    def mostrarInfo(self):
        print("%d\t%d\t%d\t%d\t%f" % (self.id_tipo,self.stock,self.peso,self.ganancia,self.razon_peso_ganancia))

class mochila:
    def __init__(self,capacidad):
        self.capacidad = capacidad
        self.capacidad_disponible = self.capacidad
        self.articulos_totales = int(0)
        self.articulos_dentro = {}
        self.ganancia = 0
        # {"tipo":("cantidad","peso","ganancia")}

    def hayEspacioDisponible(self):
        if self.capacidad_disponible >= 0:
            return True
        else:
            return False

    def agregarArticulo(self,objeto):
        if self.hayEspacioDisponible() and self.capacidad_disponible >= objeto.peso:
            self.articulos_totales += 1
            self.capacidad_disponible -= objeto.peso
            self.ganancia += objeto.ganancia
            if not objeto.id_tipo in self.articulos_dentro:
                self.articulos_dentro[objeto.id_tipo] = list([1,objeto.peso,objeto.ganancia])
            else:
                self.articulos_dentro[objeto.id_tipo][0] += 1
        
    def mostrarContenido(self):
        print("\nCapacidad: ", self.capacidad)
        print("Espacio disponible: ", self.capacidad_disponible)
        print("Ganancia total: ", self.ganancia)
        print("Objetos dentro: ", self.articulos_totales,"\n")
        print("Contenido final de la mochila")
        print("Tipo\tStock\tValor U\tPeso U\tValor T\tPeso T")
        for tipo in self.articulos_dentro:
            print(tipo,"\t",self.articulos_dentro[tipo][0],"\t",self.articulos_dentro[tipo][2],"\t",self.articulos_dentro[tipo][1],
            "\t",self.articulos_dentro[tipo][2]*self.articulos_dentro[tipo][0],"\t",self.articulos_dentro[tipo][1]*self.articulos_dentro[tipo][0])
