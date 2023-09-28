#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''

    PRÁCTICA 4 (PARTE 1): ALGORITMOS VORACES, EJERCICIO 7.3

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

#{P: (Para todo i: 0<=i<=n :(Para todo j:0<=j<=n,j != i :T[i] != T[j]))}
def procesos(T):
    n = len(T)
    sol = [0] * n
    Tiempo_total = 0
    i = 0
    for valor, ind in sorted([(T[i], i) for i in range(n)]) :
        Tiempo_total += (n-ind+1)*T[ind]
        sol[i] = ind
        i += 1
    return sol,Tiempo_total

# Complejidad O(n) en memoria y O(nlog(n)) en tiempo

def main():
    
    T = [1,3,2,4,6,5,8,10,9]
    
    sol, Tiempo_total = procesos(T)
    
    print("Orden de selecciÃ³n:", sol)
    print("Tiempo total:", Tiempo_total)
    
    MAX_LEN = 1000  # Maximum length of input list.

    # Initialise results containers
    
    lengths_procesos = []
    times_procesos   = []
 
    for length in range(0, MAX_LEN, 2):
        
        # Generate random list
        
        T = [random.randrange(1, 50, 10) for _ in range(length)]

        # Time execution (algoritmo 'queHace1')
        
        start = time.perf_counter()
        procesos(T)
        end = time.perf_counter()

        # Store results
        
        lengths_procesos.append(length)
        times_procesos.append(end - start)


    # Plot results
    
    plt.style.use("dark_background")
    plt.figure().canvas.manager.set_window_title("Time Complexity")
    plt.xlabel("List Length")
    plt.ylabel("Execution Time (s)")
    plt.plot(lengths_procesos, times_procesos, label="procesos()")
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    ns = np.linspace(1, 1000, 100, dtype = int)
    ts = [timeit.timeit('procesos(lst)',
                    setup='lst=list(range({})); random.shuffle(lst)'.format(n),
                    globals=globals(),
                    number=1000)
          for n in ns]

    plt.plot(ns, ts, 'or')

    degree = 5
    coeffs = np.polyfit(ns, ts, degree)
    p = np.poly1d(coeffs)
    plt.plot(ns, [p(n) for n in ns], '-b')