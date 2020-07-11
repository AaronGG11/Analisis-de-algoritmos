def convertirListaEntera(elemento=0):
    return int(elemento)


# Funcion que recibe como parametro el archivo origen que contiene las frecuencias 
# retornara un diccionario con los valores de frecuencias y clave
def leerDatos(nombre_archivo_origen):
    numero = None
    numeros = None
    contador = 1

    with open(nombre_archivo_origen) as archivo:
        # recorre línea a línea el archivo
        for linea in archivo:
            if contador == 2:
                numero = int(linea.rstrip('\n'))
            if contador == 4:
                numeros = list(map(convertirListaEntera,linea.rstrip('\n').split()))
            contador += 1   

    return numero,numeros
