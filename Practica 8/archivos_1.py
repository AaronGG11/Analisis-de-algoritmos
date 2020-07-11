# Funcion que recibe como parametro el archivo origen que contiene las frecuencias 
# retornara un diccionario con los valores de frecuencias y clave
def leerDatos(nombre_archivo_origen):
    resultado = []

    with open(nombre_archivo_origen) as archivo:
        # recorre línea a línea el archivo
        for linea in archivo:
            resultado.append(linea.rstrip('\n').split())
    
    return resultado
