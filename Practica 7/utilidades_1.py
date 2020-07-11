import itertools as it

# Funcion que retorna la suma de cada uno de los elementos de una list
# Recibe como parametro la lista
def obtenerSuma(secuencia):
    cont = 0
    for i in secuencia:
        cont += i

    return cont 

# Funcion que rellena una lista con el numero minimo de otra lista
# Recibe como parametro el numero n, los numeros posibles, y las combinaciones obtenidas previamente
def llenaConMinimo(n,nums,combinaciones):
    for secuencia in combinaciones:
        while(obtenerSuma(secuencia) < n):
            secuencia.append(min(nums))

# Funcion que genera una lista de listas, cada una de estas listas contiene 
#   numeros iguales con las que se puede representar x
# Recibe como parametro el numero x y la lista de numeros posibles
def obtenerIguales(x,numeros):
    # posibles juntos
    result = []
    for i in numeros:   
        cont = x
        aux = []
        while (cont/i >= 1):
            cont -= i
            aux.append(i)
        
        if len(aux) > 1:
            result.append(aux)
    llenaConMinimo(x,numeros,result)
    return result

# Funcion que genera una lista con las posibles combinaciones entre el minimo y los demas numeros
# Recibe como parametro el numero a calcular combinaciones y la lista de numeros disponibles
def generaCombinaciones(x,nums):
    result = []

    for i in nums:
        aux = []
        if i != min(nums):
            for j in range(1,int(x/i)+1):
                aux = []
                for k in range(0,j):
                    aux.append(i)
                result.append(aux)
    llenaConMinimo(x,nums,result)

    return result

# Funcion que genera una lista con las posibles combionaciones entre nuemros que no contienen el minimo
# Recibe como parametro l nuemro a calcular combinaciones y la lista de numeros disponibles
def llenaCombinacion(n,nums):
    posibles = []
    for i in range(2,len(nums)+1):
        aux = list(it.permutations(nums,i))
        cont = 0
        for sec in aux:
            cont = 0
            for ind in sec:
                cont += ind
            if cont <= n:
                posibles.append(list(sec))

    for i in posibles:
        i.sort()

    posibles = set(tuple(x) for x in posibles)
    posibles = [ list(x) for x in posibles ]

    llenaConMinimo(n,nums,posibles)

    return posibles
        
# Funcion que genera las combinaciones totales que dan solucion al problema 
# Recibe como parametro todas las optenidas por la funcion "llenaCombinacion" 
# para posteriormente obtener permutaciones y discriminar todas las direntes
def generaCombinacionesFinales(candidatas):
    result = []
    for secuencia in candidatas:
        aux = list(it.permutations(secuencia))
        aux = set(tuple(x) for x in aux)
        aux = [ list(x) for x in aux ]
        for sec in aux:
            result.append(sec)

    return result