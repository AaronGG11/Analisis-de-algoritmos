# --------------- Importacion de modulos a utilizar
from archivos import *
from problema_De_La_Mochila import *

# --------------- Declaracion de apuntador a archivo
name_file_INPUT = input("Teclee el nombre del archivo: ")

# --------------- Declaracion de variables a utilizar

capacidad,numero_articulos,peso_articulos,ganancia_articulos = leerDatos(name_file_INPUT)
backpack = mochila(capacidad)
articulos = []
for i in range(0,len(ganancia_articulos)):
    # lista de articulos, ordenada descendentemente con base a la razon ganancia peso
    articulos.append(articulo(numero_articulos[i],peso_articulos[i],ganancia_articulos[i],i+1))

articulos.sort(key=lambda tup: tup.razon_peso_ganancia,reverse=True) 

print("Tipo\tStock\tPeso\tValor\tRazón")
for articulo in articulos:
    articulo.mostrarInfo()

for articulo in articulos:
    if articulo.peso <= backpack.capacidad_disponible:
        for cantidad in range(0,articulo.stock):
            if articulo.hayDisponibilidad():
                articulo.quitarArticulo()
                backpack.agregarArticulo(articulo)

backpack.mostrarContenido()

    