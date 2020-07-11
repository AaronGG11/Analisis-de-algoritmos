import os
from fourierTransform import *

A = []
B = []
os.system("clear")

print("\n--------------- Practica 3 - Divide y venceras ---------------")
grado_A = int(input("Teclee el grado del polinomio A: ")) + 1
# le sumamos uno debido a que el grado empieza en 0
for i in range(0,grado_A):
    valor=int(input("A"+str(i)+": "))
    A.append(valor)

grado_B = int(input("Teclee el grado del polinomio B: ")) + 1
# le sumamos uno debido a que el grado empieza en 0
for i in range(0,grado_B):
    valor=int(input("B"+str(i)+": "))
    B.append(valor)

# Acondicionamos los polinomios para que tengan el mismo tamaño + 1
if len(A) == len(B):
    print("")
elif(len(A)<len(B)):
    for i in range(len(B)-len(A)):
        A.append(0)
else: 
    for i in range(len(A)-len(B)):
        B.append(0)

diferiencia_grado = (grado_A + grado_B) - len(A) - 1
for i in range(diferiencia_grado):
    A.append(0)
    B.append(0)



print("---------- Polinomios capturados----------") 
print("A: ", A)
print("B: ", B)

print("---------- Suma de los polinomios ----------")
print(sumarPolinomios(A,B))

print("---------- Multiplicacion de los polinomios ----------")
print(multiplicarPolinomios(A,B),"\n")



