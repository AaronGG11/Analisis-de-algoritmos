# --------------- Importacion de modulos a utilizar
from utilidades_grafos import *
from archivo import *

# --------------- Declaracion de apuntador a archivo
name_file_INPUT  = open("input.txt", "r")
name_file_OUTPUT = open("output.txt", "w")

# --------------- Ejecutable
G = nx.DiGraph()
lista_de_nodos_valor = leer_vertices_valor(name_file_INPUT)
agregarVerticeValor(lista_de_nodos_valor,G)
lista_de_aristas = leer_aristas(name_file_INPUT)
G.add_edges_from(lista_de_aristas)
costos_recorrido = obtenerCostoPorVertice(G)
imprimirEnArchivo(name_file_OUTPUT,costos_recorrido)
print("Operacion exitosa, archivo generado: [output.txt]\n")

name_file_INPUT.close()
name_file_OUTPUT.close()