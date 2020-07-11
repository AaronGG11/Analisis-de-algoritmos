# --------------- Importacion de modulos a utilizar
from archivos_2 import *
from utilidades_2 import * 

# --------------- Declaracion de apuntador a archivo
name_file_INPUT = input("Teclee el nombre del archivo: ")

# --------------- Ejecutable
seq = leerDatos(name_file_INPUT)
subseq = subsequence(seq)
print("\nLista original: ", seq)
print("Subsecuencia máxima: ", subseq,"\n")