from archivos_1 import *


class Actividad: 
    def __init__(self, inicio, finalizacion, valor, identificador): 
        self.inicio  = inicio 
        self.finalizacion = finalizacion 
        self.valor  = valor 
        self.id = identificador

    def mostraraActividad(self):
        print("ID de actividad: ", self.id)
        print("Hora de inicio: ", self.inicio)
        print("Hora de finalización: ", self.finalizacion)
        print("Valor de actividad: ", self.valor, "\n")
  
  
# Una función basada en la búsqueda binaria para encontrar la ultima actividad 
# (antes de la actividad actual) que no entre en conflicto con la actividad actual. 
# "index" es el índice de la actividad actual. Esta función devuelve -1 si todos 
# las actividades anteriores al índice entran en conflicto con ella. Las actividades
# de matriz [] se ordenan en orden creciente de tiempo de finalización.
def binarySearch(actividades, inicio_index): 
  
    # Inicializamo 'lo'y 'hi' para busqueda binaria
    lo = 0
    hi = inicio_index - 1
  
    # Realizar búsqueda binaria iterativamente 
    while lo <= hi: 
        mid = (lo + hi) // 2
        if actividades[mid].finalizacion <= actividades[inicio_index].inicio: 
            if actividades[mid + 1].finalizacion <= actividades[inicio_index].inicio: 
                lo = mid + 1
            else: 
                return mid 
        else: 
            hi = mid - 1
    return -1
  
# La función principal que devuelve el máximo posible.
#   valor de una variedad dada de actividades
def Planificar(actividades): 
    
    # Ordenar actividades según el tiempo de finalización 
    actividades = sorted(actividades, key = lambda j: j.finalizacion) 
  
    # Creamos una matriz para almacenar soluciones de subproblemas. table[i] 
    # almacena el valor para trabajos hasta arr[i] (incluendo arr[i]) 
    n = len(actividades)  
    table = [0 for _ in range(n)] 
    tareas = []
    aux = []
  
    table[0] = actividades[0].valor; # la primera por default no tiene predecesor
  
    # Rellenar entradas en la tabla [] usando la propiedad recursiva
    for i in range(1, n): 
        # Encuentra valor incluyendo la actividad actual
        valor_inicial = actividades[i].valor 
        l = binarySearch(actividades, i) # busca el predecesor anterior mas cercano

        if (l != -1): # si tiene predecesor
            valor_inicial += table[l]; 
  
        # Almacenar máximo de incluir y excluir
        table[i] = max(valor_inicial, table[i - 1]) 



    return table
  

def generarListaActividades():
    resultado = []
    actividades_sin_formato = leerDatos("input_1.txt")
    for act in actividades_sin_formato:
        resultado.append(Actividad(int(act[0]),int(act[1]),int(act[2]),str(act[3])))
    return resultado


# Código de controlador para probar la función anterior
lista_de_actividades_2 = generarListaActividades()

print("Valor optimo: ") 
print(Planificar(lista_de_actividades_2))



