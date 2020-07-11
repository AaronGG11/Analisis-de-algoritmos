# Funcion que recibe como parametro el archivo origen que contiene las frecuencias 
# retornara un diccionario con los valores de frecuencias y clave
def generarDiccionarioFrecuencias(nombre_archivo_origen):
    lineas = {}

    with open(nombre_archivo_origen + ".txt") as archivo:
        # recorre línea a línea el archivo
        for linea in archivo:
            lineas[linea.rstrip('\n').split()[0]] = float(linea.rstrip('\n').split()[1])

    return lineas

# Funcion qeu recibe como parametros el archivo donde se va a imprimir la codificacion, 
# la codificacion previamente reliazada y la lista de frecuencias, imprime en el archivo indicado
# la codificacion con formato para su visualizacion
# No hay valor de retorno 
def imprimirEnArchivo(archivo_destino,codificacion,diccionario_frecuencias):
    archivo_destino.write("Symbolo\tFrecuencia\t\tCódigo Huffman\n")
    for p in codificacion:
        archivo_destino.write("%s\t%s\t\t%s\n" % (p[0], diccionario_frecuencias[p[0]], p[1]))
