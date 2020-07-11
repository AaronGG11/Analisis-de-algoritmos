# Practica 4: Algortimos ávidos
# Programa 1: Codificacion binaria de Huffman
# Fecha: 31/10/2019
# Autores: Aaron Garcia, Echecatzin Vallejo

# --------------- Importacion de modulos a utilizar
from archivos import *
from huffman1 import *

# --------------- Declaracion de apuntador a archivo
name_file_INPUT = input("Teclee el nombre del archivo con las frecuencias: ")
name_file_OUTPUT = open("output.txt", "w")

# --------------- Creacion de las frecuencias
diccionario_de_frecuencias = defaultdict(float)
diccionario_de_frecuencias = generarDiccionarioFrecuencias(name_file_INPUT)

# --------------- Creacion de la codificacion
codificacion_sin_formato = codificarHuffman(diccionario_de_frecuencias)
imprimirEnArchivo(name_file_OUTPUT,codificacion_sin_formato,diccionario_de_frecuencias)
print("Operacion exitosa, archivo generado: [output.txt]\n")
name_file_OUTPUT.close()
