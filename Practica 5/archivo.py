# Funcion que lee la primera linea de un archivo
# Recibe como argumento el archivo
# Retorna la lista de tuplas ([ID_nodo,valor],...)
def leer_vertices_valor(archivo):
    linea = archivo.readline()
    lista_linea = linea.split()
    nuevo = []
    for dato in lista_linea:
        cadena = dato.replace(',','')
        nuevo.append((cadena[0],int(cadena[1])))

    return nuevo

# Funcion que le de la linea 1 a la n
# recibe como argumento el archivo
# retorna lista de tuplas con las aristas
# Esta funcion se manda a llamar despues de leer_vertices_valor
def leer_aristas(archivo):
    lineas = archivo.readlines()

    nuevo = []
    for linea in lineas:
        lista_linea = linea.split()
        for dato in lista_linea:
            nuevo.append(tuple(dato.replace(',','')))
    return nuevo

# Funcion que recibe como parametros el archivo donde se va a imprimir 
# y la lista de precios por cada vertice con formato para su visualizacion
# No hay valor de retorno 
def imprimirEnArchivo(archivo_destino,lista_resultado):
    archivo_destino.write("Arreglo completo con el costo para cada vértice\n")
    archivo_destino.write("costo[vertice] = precio mas barato alcanzable desde un vertice generador incluido el mismo\n")

    archivo_destino.write("ID vertice\tCosto minimo\t\tCamino a recorrer\n")
    for vertice in lista_resultado:
        archivo_destino.write('{3}{0:2s}{3} \t\t\t{3}{1:3d}{3} \t\t\t\t{3}{2:10s}{3}'.format(vertice[0], vertice[1], str(vertice[2]), ''))
        archivo_destino.write("\n")