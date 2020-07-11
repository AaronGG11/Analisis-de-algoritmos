A = [1,5,2]
B = [6,1,4,3]

# Funion que multiplica los coeficientes de dos polinomios, reotrna los coeficientes de dicha multiplicacion
def multiplicacion(A,B):
    resultado = [0]*(len(A)+len(B)-1)
    for p1,x1 in enumerate(A):
        for p2,x2 in enumerate(B):
            resultado[p1+p2] += x1*x2
    return resultado

