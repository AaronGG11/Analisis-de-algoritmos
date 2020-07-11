def convertirListaEntera(elemento=0):
    return int(elemento)


# Funcion que recibe como parametro el archivo origen que contiene las frecuencias 
# retornara un diccionario con los valores de frecuencias y clave
def leerDatos(nombre_archivo_origen):
    n_a_t = None # numero articulos tipo
    p_a_t = None # peso articulos tipo
    g_a_t = None # ganancia articulos tipo
    capacidad = 0
    contador = 1

    with open(nombre_archivo_origen) as archivo:
        # recorre línea a línea el archivo
        for linea in archivo:
            if contador == 2:
                capacidad = int(linea.rstrip('\n'))
            if contador == 4:
                n_a_t = list(map(convertirListaEntera,linea.rstrip('\n').split()))
            if contador == 6:
                p_a_t = list(map(convertirListaEntera,linea.rstrip('\n').split()))
            if contador == 8:
                g_a_t = list(map(convertirListaEntera,linea.rstrip('\n').split()))

            contador += 1   

    return capacidad,n_a_t, p_a_t, g_a_t
