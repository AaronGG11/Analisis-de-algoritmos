from random import *

# Ordanimiento burbuja
def burbuja(A):
    for i in range(1,len(A)):
        for j in range(0,len(A)-i):
            if(A[j] > A[j+1]):
                aux = A[j]
                A[j] = A[j+1]
                A[j+1] = aux
    return A

# Ordenamiento por insercion 
def insercion(A):
    for i in range(0,len(A)):
        actual = A[i]
        posicion = i
        
        while((posicion>0) and (actual<A[posicion-1])):
            A[posicion] = A[posicion-1]
            posicion -= 1
        A[posicion] = actual
    return A

# Ordenamiento por mezclas

# Modulo que ordena pares dados
def merge(left,rigt):
    result = []
    i, j = 0, 0
    
    while i<len(left) and j<len(rigt):
        if(left[i] < rigt[j]):
            result.append(left[i])
            i+=1
        else:
            result.append(rigt[j])
            j+=1
    result += left[i:]
    result += rigt[j:]
    
    return result
 
# Modulo que ordena parte y ordena los pares     
def mergeSort(A):
    if(len(A) <= 1):
        return A
    
    mid = int(len(A)/2)
    left = mergeSort(A[:mid])
    right = mergeSort(A[mid:])
    return merge(left,right)
    

# Ordenamiento rapido 
def quickSort(A):
    if len(A) <= 1: return A
    smaller, equal, larger = [], [], []
    pivot = A[randint(0,len(A)-1)]
    
    for x in A:
        if x < pivot: smaller.append(x)
        elif x == pivot: equal.append(x)
        else: larger.append(x)
    
    return quickSort(smaller) + equal + quickSort(larger)
            