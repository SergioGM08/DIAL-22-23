# -*- coding: utf-8 -*-

'''

    PRÁCTICA 4 (PARTE 1): DIVIDE Y VENCERÁS, EJERCICIO 6.3

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


def subsec_sum_max(A, c, f): # O(nlog(n))
    
    if c > f:
        return float('-inf')
    
    elif c == f:
        ssm = A[c]
    
        
    else:
        
        m = (c + f)//2 
        max1 = subsec_sum_max(A, c, m)
        max2 = subsec_sum_max(A, m+1, f)
        aux_max1, aux_max2 = A[m], A[m+1]
        temp1, temp2 = A[m], A[m+1]
        i = m
        
        while i-1 >= c:
            
            temp1 += A[i-1]
            i -= 1
            
            if temp1 > aux_max1:
                aux_max1 = temp1
                
        j = m+1 
        
        while j+1 <= f:
            
            temp2 += A[j+1]
            j += 1 
            
            if temp2 > aux_max2:
                aux_max2 = temp2
                
        max3 = aux_max1 + aux_max2
        ssm = max(max(max1, max2), max3)
        
    return ssm


def main():
    
    MAX_LEN = 1000  # Maximum length of input list
    
    # Initialise results containers
    
    lengths = []
    times = []
    
    for length in range(0, MAX_LEN, 100) :
        
        # Generate random list
        
        A = [random.randint(-99, 99) for _ in range(length)] # Lista aleatoria
        # Time execution
        
        start = time.perf_counter()
        c = 0
        f = len(A) - 1
        subsec_sum_max(A, c, f)
        end = time.perf_counter()

        # Store results
        
        lengths.append(length)
        times.append(end - start)

    # Plot results
    
    plt.style.use("dark_background")
    plt.figure().canvas.manager.set_window_title("Subsecuencia de suma máxima - Time Complexity")
    plt.xlabel("List Length")
    plt.ylabel("Execution Time (s)")
    plt.plot(lengths, times, label="subsec_sum_max()")

    plt.legend()
    plt.tight_layout()
    plt.show()
    

    # Polynomial fit
    
    degree = 5
    ns = np.linspace(1, 3000, 100, dtype = int)
    plt.title("Orden del método")

    
    ts = [timeit.timeit('subsec_sum_max(lst, 0, len(lst)-1)',
                    setup='lst=list(range({})); random.shuffle(lst)'.format(n),
                    globals=globals(),
                    number=1000)
          for n in ns]

    
    plt.plot(ns, ts, 'or')
    
    coeffs = np.polyfit(ns, ts, degree)
    p = np.poly1d(coeffs)
    plt.plot(ns, [p(n) for n in ns], '-g', label = "ssm")

    
    plt.legend(loc = "upper left")
    











