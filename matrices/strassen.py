#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import ceil, log

# Funcion que imprime una matriz que recibe como argumento
def imprimirMatriz(matrix):
    for line in matrix:
        print("\t".join(map(str, line)))

# Funcion que multiplica 2 matrices que recibe como argumento mediante el uso de 3 ciclos for
def multiplicarMatrizIKJ(A, B):
    n = len(A)
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for k in range(n):
            for j in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


# Funcion que suma 2 matrices que recibe como argumento 
def sumarMatrices(A, B):
    n = len(A)
    C = [[0 for j in range(0, n)] for i in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            C[i][j] = A[i][j] + B[i][j]
    return C


# Funcion que resta 2 matrices que recibe como argumento 
def restarMatrices(A, B):
    n = len(A)
    C = [[0 for j in range(0, n)] for i in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            C[i][j] = A[i][j] - B[i][j]
    return C

'''Funcion realiza la multiplicacion de dos matrices que recibe como argumento, mediante el 
    algoritmo de strassen pero unicamente para matrices de cuadradas de tamaño 2^n '''
def strassenPowerTwo(A, B):
    n = len(A)

    if n <= 1: # Caso base, cuando tenemos una matriz de tamaño 1x1
        return multiplicarMatrizIKJ(A, B)
    else:
        # inicializando las nuevas sub matrices con 0's
        nuevo_tam = n//2 
        
        a11 = [[0 for j in range(0, nuevo_tam)] for i in range(0, nuevo_tam)]
        a12 = [[0 for j in range(0, nuevo_tam)] for i in range(0, nuevo_tam)]
        a21 = [[0 for j in range(0, nuevo_tam)] for i in range(0, nuevo_tam)]
        a22 = [[0 for j in range(0, nuevo_tam)] for i in range(0, nuevo_tam)]

        b11 = [[0 for j in range(0, nuevo_tam)] for i in range(0, nuevo_tam)]
        b12 = [[0 for j in range(0, nuevo_tam)] for i in range(0, nuevo_tam)]
        b21 = [[0 for j in range(0, nuevo_tam)] for i in range(0, nuevo_tam)]
        b22 = [[0 for j in range(0, nuevo_tam)] for i in range(0, nuevo_tam)]

        aResult = [[0 for j in range(0, nuevo_tam)] for i in range(0, nuevo_tam)]
        bResult = [[0 for j in range(0, nuevo_tam)] for i  in range(0, nuevo_tam)]

        # dividiendo las matrices en 4 submatrices
        for i in range(0, nuevo_tam):
            for j in range(0, nuevo_tam):
                a11[i][j] = A[i][j]            # arriba izquierda
                a12[i][j] = A[i][j + nuevo_tam]    # arriba derecha
                a21[i][j] = A[i + nuevo_tam][j]    # abajo izquierda
                a22[i][j] = A[i + nuevo_tam][j + nuevo_tam] # abajo derecha

                b11[i][j] = B[i][j]            # arriba izquierda
                b12[i][j] = B[i][j + nuevo_tam]   # arriba derecha
                b21[i][j] = B[i + nuevo_tam][j]    # abajo izquierda
                b22[i][j] = B[i + nuevo_tam][j + nuevo_tam] # abajo derecha

        # Calculating p1 to p7:
        aResult = sumarMatrices(a11, a22)
        bResult = sumarMatrices(b11, b22)
        p1 = strassenPowerTwo(aResult, bResult) # p1 = (a11+a22) * (b11+b22)

        aResult = sumarMatrices(a21, a22)      # a21 + a22
        p2 = strassenPowerTwo(aResult, b11)  # p2 = (a21+a22) * (b11)

        bResult = restarMatrices(b12, b22) # b12 - b22
        p3 = strassenPowerTwo(a11, bResult)  # p3 = (a11) * (b12 - b22)

        bResult = restarMatrices(b21, b11) # b21 - b11
        p4 =strassenPowerTwo(a22, bResult)   # p4 = (a22) * (b21 - b11)

        aResult = sumarMatrices(a11, a12)      # a11 + a12
        p5 = strassenPowerTwo(aResult, b22)  # p5 = (a11+a12) * (b22)

        aResult = restarMatrices(a21, a11) # a21 - a11
        bResult = sumarMatrices(b11, b12)      # b11 + b12
        p6 = strassenPowerTwo(aResult, bResult) # p6 = (a21-a11) * (b11+b12)

        aResult = restarMatrices(a12, a22) # a12 - a22
        bResult = sumarMatrices(b21, b22)      # b21 + b22
        p7 = strassenPowerTwo(aResult, bResult) # p7 = (a12-a22) * (b21+b22)

        # calculating c21, c21, c11 e c22:
        c12 = sumarMatrices(p3, p5) # c12 = p3 + p5
        c21 = sumarMatrices(p2, p4)  # c21 = p2 + p4

        aResult = sumarMatrices(p1, p4) # p1 + p4
        bResult = sumarMatrices(aResult, p7) # p1 + p4 + p7
        c11 = restarMatrices(bResult, p5) # c11 = p1 + p4 - p5 + p7

        aResult = sumarMatrices(p1, p3) # p1 + p3
        bResult = sumarMatrices(aResult, p6) # p1 + p3 + p6
        c22 = restarMatrices(bResult, p2) # c22 = p1 + p3 - p2 + p6

        # Agrupando los resultados obtenidos en una única matriz
        C = [[0 for j in range(0, n)] for i in range(0, n)]
        for i in range(0, nuevo_tam):
            for j in range(0, nuevo_tam):
                C[i][j] = c11[i][j]
                C[i][j + nuevo_tam] = c12[i][j]
                C[i + nuevo_tam][j] = c21[i][j]
                C[i + nuevo_tam][j + nuevo_tam] = c22[i][j]
        return C


'''Funcion realiza la multiplicacion de dos matrices que recibe como argumento, mediante el 
    algoritmo de strassen para matrices cuadradas paras e impares '''
def strassen(A, B):
    # validamos los arguemntos y sus dimensiones
    assert type(A) == list and type(B) == list
    assert len(A) == len(A[0]) == len(B) == len(B[0])

    sigueintePotencia2 = lambda n: 2**int(ceil(log(n,2)))
    n = len(A)
    m = sigueintePotencia2(n)
    APrep = [[0 for i in range(m)] for j in range(m)]
    BPrep = [[0 for i in range(m)] for j in range(m)]
    for i in range(n):
        for j in range(n):
            APrep[i][j] = A[i][j]
            BPrep[i][j] = B[i][j]
    CPrep = strassenPowerTwo(APrep, BPrep)
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = CPrep[i][j]
    return C

A = [[1,1,1,1],[1,1j,-1,-1j],[1,-1,1,-1],[1,-1j,-1,1j]]
B = [[1,1,1,1],[1,-1j,-1,1j],[1,-1,1,-1],[1,1j,-1,-1j]]
C = strassen(A,B)
imprimirMatriz(C)