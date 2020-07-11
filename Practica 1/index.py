# Garcia Gonzalez Aaron Antonio
# Fecha de entrega: Lunes 26 de Agosto de 2019.
# Programa principal practica 1

# Funcion que multiplica dos numeros
def multiply(x,y):
    if y == 0: 
        return 0
    z = multiply(x,y/2)
    if not(y & 1):
        return 2*z
    else: 
        return x + 2*z

# Funcion que crea una matriz a partir de la dimencion de un arreglo 
def makeMatriz(A):
    B = []
    for i in range(len(A)):
        B.append([])
        for j in range(len(A)):
            B[i].append(0)
    return B

# Funcion que llena una matriz a partir de un arreglo, dado una matriz B[i][j],
# si i < j, entonces el valor en la posicion (i,j) en la matriz sera la suma de 
# A[i] hasta A[j], de lo contrario, es decir i>j, el valor no esta definido.
def strangeMatriz(A,B):
    for i in range(len(A)):
        for j in range(len(A)):
            if i < j:
                for k in range(i,j):
                    B[i][j] += k
            if i > j:
                B[i][j] = None
    return B

# Funcion que ordena un arreglo mediante el metodo de seleccion, es decir buscar
# buscar el menor de los numeros en cada iteracion y los coloca en el lugar correcto 
def selection(A):
    for i in range(len(A)):
        minimo=i
        for j in range(i,len(A)):
            if(A[j] < A[minimo]):
                minimo=j
        if(minimo != i):
            aux=A[i]
            A[i]=A[minimo]
            A[minimo]=aux
    return A

def algorithm1(a,b):
    u = a; v = b
    x1 = 1; y1 = 0
    x2 = 0; y2 = 1

    q = 0; r = 0; x = 0; y = 0; d = 0

    while u != 0:
        q = v/u
        r = v - (q*u)
        x = x2 - (q*x1)
        y = y2 - (q*y1)
        v = u
        u = r
        x2 = x1
        x1 = x
        y2 = y1
        y1 = y

    d = v
    x = x2
    y = y2

    return (d,x,y)

def algorithm2(a,p):
    u = a; v = p
    x1 = 1; x2 = 0

    q = 0
    r = 0 
    x = 0
    contador = 0

    while u != 1:
        q = v/u
        r = v - (q*u)
        x = x2 - (q*x1)
        v = u
        u = r
        x2 = x1 
        x1 = x
        print("Iterecacion: ", contador)
        print("q", q)
        print("v", v)
        print("u", u)
        print("x", x)
        print("x1", x1)
        print("x2", x2)
        print("r", r)
        print("p", p)
        contador += 1

    return x1 % p
         
A = [11,3,9,9,9,24,6,18,21,5,97]

print(multiply(13,76))
print(selection(A))
print(algorithm2(2,9))












