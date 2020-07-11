def coincidenciaEficienteB(A):
    tam = len(A)
    centro = 0
    inferior = 0
    superior = tam-1
    resultado = []

    while(inferior <= superior):
        centro = (inferior + superior)//2
        if A[centro] == centro: 
            
            return centro
        elif centro < A[centro]:
            # centro < A[centro]
            # en este punto, desde centro hasta el final del array, ya no habra coincidencias
            # por lo tanto hay que buscar desde cero hasta centro
            superior = centro - 1
        else: 
            # centro > A[centro]
            # en este punto, desde cero hasta centro no habra coincidencias
            # por lo tanto hay que buscar desde el centro hasta el final del arreglo 
            inferior = centro + 1 
            


E = [-6,-5,-4,-3,-2,-1,0,1,8]
print(coincidenciaEficienteB(E))
