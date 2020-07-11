def producto_matricial(p):
    """Return m and s.
 
    m[i][j] e sel numero minimo de multiplicaciones escalares que se necesitan realizar 
        con el producto de matrices A(i), A(i + 1), ..., A(j).
 
    s[i][j] es el índice de la matriz después del cual el producto se divide en un
     paréntesis óptimo del producto matriz.
 
    p[0... n] es una lista tal que la matriz A (i) tiene dimensiones p [i - 1] x p [i].
    """
    length = len(p) # len(p) = numero de matrices + 1
 
    # m[i][j] es el número mínimo de multiplicaciones necesarias para calcular el
    # producto de matrices A(i), A(i+1), ..., A(j)
    # s[i][j] es la matriz después de la cual el producto se divide en el mínimo
    # numero de multiplicaciones necesarias
    m = [[-1]*length for _ in range(length)]
    s = [[-1]*length for _ in range(length)]
 
    vaproductos_matriz(p, 1, length - 1, m, s)
 
    return m, s
 
 
def vaproductos_matriz(p, start, end, m, s):
    """Return minimum number of scalar multiplications needed to compute the
    product of matrices A(start), A(start + 1), ..., A(end).
 
    El número mínimo de multiplicaciones escalares necesarias para calcular el
    producto de matrices A(i), A(i + 1), ..., A(j) esta almacenado en m[i][j].
 
    El índice de la matriz después del cual el producto anterior se divide en un óptimo
    el paréntesis se almacena en s[i][j].
 
    p[0... n] es una lista tal que la matriz A (i) tiene dimensionesp[i - 1] x p[i].
    """
    if m[start][end] >= 0:
        return m[start][end]
 
    if start == end:
        q = 0
    else:
        q = float('inf')
        for k in range(start, end):
            temp = vaproductos_matriz(p, start, k, m, s) \
                   + vaproductos_matriz(p, k + 1, end, m, s) \
                   + p[start - 1]*p[k]*p[end]
            if q > temp:
                q = temp
                s[start][end] = k
 
    m[start][end] = q
    return q
 
 
def imprimir_palentizacion(s, start, end):
    """ Imprimimos el paréntesis óptimo del producto matriz A (inicio) x
    A(inicio + 1) x ... x A(final).
 
    s[i][j] es el índice de la matriz después del cual el producto se divide en un
    paréntesis óptimo del producto matriz.
    """
    if start == end:
        print('A[{}]'.format(start), end='')
        return
 
    k = s[start][end]
 
    print('(', end='')
    imprimir_palentizacion(s, start, k)
    imprimir_palentizacion(s, k + 1, end)
    print(')', end='')
 
 
n = int(input('Teclea el número de matrices: '))
p = []
for i in range(n):
    temp = int(input('Teclea el numero de filas de la matriz {}: '.format(i + 1)))
    p.append(temp)
temp = int(input('Teclea el número de columnas de la matrix {}: '.format(n)))
p.append(temp)
 
m, s = producto_matricial(p)
print("-------------------------- Matriz ----------------------------")
for i in m:
    print(i)
print("--------------------------------------------------------------")
print('#De multiplicaciones escalares necesarias:', m[1][n])
print('Palentización óptima: ', end='')
imprimir_palentizacion(s, 1, n)
print("\n")
