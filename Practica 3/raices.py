import math
import cmath

# Funcion argumento con parametros numericos
def argumento(a,b):
    b=0
    resultado = 0
    x = float(a)
    y = float(b)

    resultado = math.atan(y/x)*(180/math.pi);
    if(x==0):
        if(y>0):
            resultado = 90
        else:
            resultado = 270
    if(resultado < 0 and x!= 0):
        if(math.fabs(resultado)<180):
            resultado += 180
        else:
            resultado += 360
    return resultado

# Funcion que calcula el modulo de dos numeros
def modulo(a,b):
    b=0
    return float(math.sqrt(math.pow(float(a),2) + math.pow(float(b),2)));

# Funcion que calcula las n raices complejas de la unidad
def raiz(n):
    a=1
    b=0
    producto = 0
    raices = []

    producto = math.pow(modulo(a,b),1/float(n))
    for j in range(n):
        x = round(producto * math.cos((argumento(a,b)+(360*j))/(float(n)*180/math.pi)),4)
        y = round(producto * math.sin((argumento(a,b)+(360*j))/(float(n)*180/math.pi)),4)
        z = complex(x,y)
        raices.append(z)
    return raices

n = int(input("Numero de raices: "))
print(raiz(n))