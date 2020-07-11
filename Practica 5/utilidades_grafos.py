import networkx as nx

# Funcion que lista todos los vertices que son iniciales o no accesibles desde otro vertice
# Recibe dos argumentos (1: lista de aristas (a,b) y 2: lista de nodos)
# Retorna una lista con los identificadores de los vertices que cumplen
def generarNodosIniciales(grafo):
    # Requerimos saber los vertices de inicio, ya que no es ciclico
    # Los nodos de incio tienen salidas pero no entradas
    lista_aristas = grafo.edges()
    lista_nodos = list(nodo[0] for nodo in grafo.nodes())
    nodos_id = {}
    llaves = []
    resultado = []
    
    for x in list(nodo[0] for nodo in lista_nodos):
        nodos_id[x] = 0
    
    llaves = list(nodos_id.keys())
    for arista in lista_aristas:
        if(arista[0] in llaves):
            nodos_id[arista[0]] += 1
        if(arista[1] in llaves):
            nodos_id[arista[1]] += 1

    return list( k for k, v in nodos_id.items() if v == 1)

# Funcion que agrega vertices a un grafo, vertice, peso
# recibe como argumento la lista de vertices y el mismo grafo
# no regresa nada
def agregarVerticeValor(lista,grafo):
    for vertice in lista:
        grafo.add_node(vertice[0],weight = vertice[1])

# Funcion que obtiene el menor precio dado un nodo final
# recibe 3 argumentos, 1: el nodo destino, 2: el mismo grafo y 3: lista de los nodos con valor
# retorna una tupla con el camino a seguir y el valor del mismo
def obtenerMenorPrecioParticular(nodo_destino,grafo):
    nodos_iniciales = generarNodosIniciales(grafo)
    dic_valor_nodos = dict(grafo.nodes(data='weight', default=1))
    conexiones = nx.single_target_shortest_path(grafo,nodo_destino) 
    candidatos = {}
    candidatos_valor = {}
    contador = None

    for clave in conexiones: # para sacar las conexiones de cada inicializador
        if clave in nodos_iniciales:
            candidatos[clave] = conexiones[clave]


    for clave in candidatos: # vamos calculando los valores
        contador = 0
        for camino in candidatos[clave]:
            contador += dic_valor_nodos[camino]
        candidatos_valor[contador] = candidatos[clave]
        
    return min(candidatos_valor.keys()),candidatos_valor[min(candidatos_valor.keys())]

# Funcion que obtiene el menor precio de cada nodo
# recibe 2 argumentos, 1: el mismo grafo y 2: lista de los nodos con valor
# retorna una tupla con el camino a seguir y el valor del mismo
def obtenerCostoPorVertice(grafo):
    resultados = []
    vertices = grafo.nodes()
    for vertice in vertices:
        resultados.append(list(vertice)+list(obtenerMenorPrecioParticular(vertice,grafo)))

    return resultados
