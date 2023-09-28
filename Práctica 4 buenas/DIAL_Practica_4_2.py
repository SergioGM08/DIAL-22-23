#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''

    PRÁCTICA 4 (PARTE 2): PROGRAMACIÓN DINÁMICA, EJERCICIO 8.1

    ASIGNATURA: DISEÑO DE ALGORITMOS
    CURSO:      2022-2023
    SUBGRUPO:   U1 / U2

    APELLIDOS: González Montero
    NOMBRE:    Sergio

'''

import matplotlib.pyplot as plt
import numpy as np
import timeit
import time
import random
import math

# {P : (Para todo i: 0<= i < N : M[i]<M[i+1]) and (D : nat) and (Para todo j: 0<= j <= N : C[j]>=0)
def monedas_pd(M,C,D):
    infinito = float('inf')
    N = len(M)
    cuantos = [0] * N
    decision = [[None]*(D+1) for i in range(N+1)]
    monedas = [[None]*(D+1) for i in range(N+1)]

    for i in range(1,D+1):
        monedas[0][i] = infinito
    for i in range(0,N+1):
        monedas[i][0] = 0 
        
    #print(monedas)
    
    for i in range(1,N+1):
        for j in range(1,D+1):
            monedas[i][j] = infinito
            for k in range(0,min(C[i-1],j//M[i-1])+1):
                
                #print(i,j,k,monedas[i-1][j-(k*M[i-1])],monedas[i][j])
                #print(monedas[i-1][j-(k*M[i-1])] + k < monedas[i][j])
                
                
                if monedas[i-1][j-(k*M[i-1])] + k < monedas[i][j]:
                    monedas[i][j] = monedas[i-1][j-(k*M[i-1])] + k
                    decision[i][j] = k
                
                #print(monedas)
                
    #print(monedas)    
    #print(decision)        
    posible = (monedas[N][D] < infinito)
    if posible == True:
        numero = monedas[N][D]
    else:
        numero = 0 #Indicamos con un 0 que no podemos pagar la cantidad exacta
    
    if posible == True:
        cantidad = D
        i = N
        while (i >= 1 and cantidad > 0):
            #print(i)
            #print(decision)
            cuantos[i-1] = decision[i][cantidad]
            cantidad = cantidad - cuantos[i-1] * M[i-1]
            i -= 1
            #print(cantidad)
    
    return posible,numero,cuantos

### Coste { 0(N*D^2) en espacio y 0(N*D) en memoria}         

def main(): # Usare para los ejemplos el sistema monetario del euro
    
    M = [1, 2, 5, 10, 20, 50, 100, 200]
    C = [1, 3, 1, 4, 3, 2, 0, 2]
    
    D = 112
    
    posible, numero, cuantos = monedas_pd(M, C, D)
    
    print("¿Es posible pagar con la cantidad exacta?:", posible)
    print("Número de monedas:", numero)
    print("¿Cuáles se han utilizado?", cuantos)
    
    MAX_LEN = 10000  # Maximum length of input list.

    # Initialise results containers
    
    lengths_monedas = []
    times_monedas   = []
 
    for length in range(100, MAX_LEN, 100):
        
        # Generate random list
        
        M = [1, 2, 5, 10, 20, 50, 100, 200]
        C = [random.randrange(0, 75) for _ in range(8)]
        D = random.randrange(length-100,length)

        # Time execution (algoritmo 'monedas_pd')
        
        start = time.perf_counter()
        monedas_pd(M,C,D)
        end = time.perf_counter()

        # Store results
        
        lengths_monedas.append(length)
        times_monedas.append(end - start)


    # Plot results
    
    plt.style.use("dark_background")
    plt.figure().canvas.manager.set_window_title("Time Complexity")
    plt.xlabel("List Length")
    plt.ylabel("Execution Time (s)")
    plt.plot(lengths_monedas, times_monedas, label="monedas()")
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    ns = np.linspace(1, 100, 100, dtype = int)
    ts = [timeit.timeit('monedas_pd([1, 2, 5, 10, 20, 50, 100, 200],[random.randrange(0, 75) for _ in range(8)] , len(lst))',
                    setup='lst=list(range({})); random.shuffle(lst)'.format(n),
                    globals=globals(),
                    number=1000)
          for n in ns]

    plt.plot(ns, ts, 'or')

    degree = 5
    coeffs = np.polyfit(ns, ts, degree)
    p = np.poly1d(coeffs)
    plt.plot(ns, [p(n) for n in ns], '-b')    
