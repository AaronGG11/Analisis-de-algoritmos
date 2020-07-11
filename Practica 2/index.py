# Garcia Gonzalez Aaron Antonio
# Fecha de entrega: Lunes XX de Septiembre de 2019
# Programa principal practica 2

import os

# Ejercicio 1. Por fuerza bruta, dado un arreglo haya los indices tales que A[i]=i
def coincidencias(A):
    auxiliar = []
    for i in range(len(A)):
        if i == A[i]:
            auxiliar.append(i)
    return auxiliar
    

#Ejercicio 1. Complejidad O(log[n])
def coincidenciaEficiente(A):
    tam = len(A)
    centro = 0
    inferior = 0
    superior = tam-1

    while(inferior <= superior):
        centro = (inferior + superior)//2
        if A[centro] == centro: 
            return centro
        elif centro < A[centro]:
            superior = centro - 1
        else: 
            inferior = centro + 1 



#Ejercicio 2. Por fuerza bruta
def polinomio1(A,x):
    resultado = 0
    for i in range(0,len(A)):
        resultado += A[i]*pow(x,i+1)
    
    return resultado

#Ejercicio 2. Complejidad menor
def polinomio2(A,x):
    resultado = 0
    acumulado = 1
    for i in range(0,len(A)):
        if i == 0:
            resultado += x*A[0]
            acumulado = 1
        else:
            acumulado *= x 
            resultado += x*A[i]*acumulado;
    return resultado 

#Ejercicio 3. Fuerza bruta, haya las inversiones dados los indices i,j donde i < j, y tambien ocurre que A[i]>A[j]
def listarInversiones(A):
    auxiliar = {}

    for i in range(len(A)):
        for j in range(len(A)):
            if (i<j and A[i]>A[j]):
                auxiliar[A[i]] = A[j]
    return auxiliar

# Por fuerza bruta
def quitarRepetidos(A):
    auxiliar = []

    for i in A:
        if i not in auxiliar:
            auxiliar.append(i);
    return auxiliar;







os.system ("clear") 
arreglo = []

print("Practica 2")
print("[1]. Programa que dado un arreglo haya los indices tales que A[i]=i")
print("[2]. Programa que evalaua un polinomio dado los coeficientes del mismo")
print("[3]. Programa que haya las inversiones dados los indices i,j donde i < j, y tambien ocurre que A[i]>A[j]")
print("[4]. Programa que elimina elementos repetidos de un arreglo dado");
opcion = int(input("     Selecciona una opcion: "))
if opcion > 4:
    exit(0)

tam = int(input("Tamaño del arreglo: "))

for x in range(tam):
    valor=int(input(("[%d]: " % (x))))
    arreglo.append(valor)

if opcion == 1:
    print("Coincidencias no eficiente: ", coincidencias(arreglo))
    print("Coincidencias eficiente: ", coincidenciaEficiente(arreglo))
elif opcion == 2:
    constante = int(input("Constante a evaluar: "))
    print("Coeficientes: ", arreglo)
    print("Resultado no eficiente: ", polinomio1(arreglo,2))
    print("Resultado eficiente: ", polinomio2(arreglo,2))
elif opcion == 3:
    print("Inversiones no eficiente: ", listarInversiones(arreglo))
else:
    print("Sin repetidor no eficiente: ", quitarRepetidos(arreglo));



