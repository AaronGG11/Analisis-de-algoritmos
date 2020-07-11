# Equipo: García González Aarón Antonio
# Análisis de algoritmos
# Reporte de tercera practica de laboratorio 
# Fecha de entrega: 14-Octubre-2019
# Modulo con las funciones necesarias para calcular la ffts, ifft, suma y multiplicacion de polinomios

import math
import cmath

# Obtenemos la raiz principal 
def omega(p, q):
   return cmath.exp((2.0 * cmath.pi * 1j * q) / p)

# transformada rapida de fourier 
def fft(x):
    n = len(x)
    if n == 1:
        return x

    Feven = fft(x[0::2])
    Fodd = fft(x[1::2])
    combined = [0] * n

    for m in range(n//2):
        z = Feven[m] + omega(n, -m) * Fodd[m]
        p_r = round(z.real,2)
        p_c = round(z.imag,2)*1j
        combined[m] = p_r + p_c

        z = Feven[m] - omega(n, -m) * Fodd[m]
        p_r = round(z.real,2)
        p_c = round(z.imag,2)*1j
        combined[m + n//2] = p_r + p_c

    return combined

# Transformada rapida de fourier inversa
''' Dado que la IFFT es la solucion, entonces basta con multiplicar los conjugados 
    de las reaices n-esimas y dividir entre la suma de los grados mayores de los dos polinomios a 
    sumar respectivamente '''
def ifft(X):
   x = fft([x.conjugate() for x in X])
   return [x.conjugate()/len(X) for x in x]

# Sumar dos polinomios
def sumarPolinomios(A,B):
    grado_A = len(A)
    grado_B = len(B)
    resultado = []

    if(grado_A == grado_B):
        for i in range(0,grado_A):
            resultado.append(A[i]+B[i])
    elif(grado_A > grado_B): # El grado del polinomio A es mayor que el de B
        for i in range(0,grado_A):
            if i <= (grado_B - 1):
                resultado.append(A[i]+B[i])
            else: 
                resultado.append(A[i])
    else: # El grado del polinomio B es mayor que el de A
        for i in range(0,grado_B):
            if i <= (grado_A - 1):
                resultado.append(A[i]+B[i])
            else: 
                resultado.append(B[i])
    
    return resultado

# Multiplicacion de polinomios
'''
    ->Expresar cada uno de los números a multiplicar en base 10 y colocar los coeficientes de dicho
    polinomio en un vector.
    ->Completar, añadiendo ceros, el vector de coeficientes de cada uno de los números hasta la
    primera potencia de dos mayor o igual que 2n.
    ->Aplicar la FFT a cada vector obtenido de este modo.
    ->Multiplicar, coordenada a coordenada, los dos vectores obtenidos en el apartado anterior.
    ->Aplicar la FFT inversa al vector que resulta de la multiplicación anterior.
'''
def multiplicarPolinomios(A,B):
    fft_A = fft(A)
    fft_B = fft(B)
    tam_AB = len(fft_A)
    resultado = []
    for i in range(0,tam_AB):
        resultado.append(fft_A[i]*fft_B[i])
    return ifft(resultado)