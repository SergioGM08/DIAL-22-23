#!/usr/bin/env python3
# -*- coding: utf-8 -*-



'''

    PRÁCTICA 1: ANÁLISIS DE LA EFICIENCIA DE ALGORITMOS (PYTHON)

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



# EJEMPLO: MÁXIMO COMÚN DIVISOR



def mcd_rec(a, b):
    
    if a > b :
        return mcd_rec(a - b, b)
    elif a == b :
        return a
    else :
        return mcd_rec(a, b - a)



def mcd_rec2(a, b):
    
    if b == 0 :
        return a
    else :
        return mcd_rec2(b, a % b)
    
    

def mcd_iter(a, b):
    
    a1 = a
    b1 = b
    
    while a1 != b1 :
        
        if a1 > b1 :
            a1 = a1 - b1
        else :
            b1 = b1 - a1
            
    return a1



def main():
    
    MAX_LEN = 500  # Maximum length of input list.

    # Initialise results containers:
    
    lengths_mcd_rec  = []
    times_mcd_rec    = []
    
    lengths_mcd_rec2 = []
    times_mcd_rec2   = []
    
    lengths_mcd_iter = []
    times_mcd_iter   = []
    

    for length in range(0, MAX_LEN, 10):
        
        # Generate random values:
        
        a = random.randint(length, 10*length)
        b = random.randint(length, 10*length)

        # Time execution (mcd_rec):
        
        start = time.perf_counter()
        mcd_rec(a, b)
        end = time.perf_counter()

        # Store results (mcd_rec):
        
        lengths_mcd_rec.append(length)
        times_mcd_rec.append(end - start)

        # Time execution (mcd_rec2):
        
        start = time.perf_counter()
        mcd_rec2(a, b)
        end = time.perf_counter()

        # Store results (mcd_rec2):
        
        lengths_mcd_rec2.append(length)
        times_mcd_rec2.append(end - start)
        
        # Time execution (mcd_iter):
        
        start = time.perf_counter()
        mcd_iter(a, b)
        end = time.perf_counter()

        # Store results (mcd_iter):
        
        lengths_mcd_iter.append(length)
        times_mcd_iter.append(end - start)
        
        
        
    # Plot results
    
    plt.style.use("dark_background")
    plt.figure().canvas.manager.set_window_title("Algoritmos de MCD - Time Complexity")
    plt.xlabel("List Length")
    plt.ylabel("Execution Time (s)")
    plt.plot(lengths_mcd_rec, times_mcd_rec, label="mcd_rec()")
    plt.plot(lengths_mcd_rec2, times_mcd_rec2, label="mcd_rec2()")
    plt.plot(lengths_mcd_iter, times_mcd_iter, label="mcd_iter()")
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    
    # Polynomial fit
    
    ns = np.linspace(1, 100000, 100, dtype = int)
    ts = [timeit.timeit('mcd_rec2(lst[0], lst[len(lst) - 1])',
                    setup='lst=list(range({})); random.shuffle(lst)'.format(n),
                    globals=globals(),
                    number=1000)
          for n in ns]

    plt.plot(ns, ts, 'or')

    degree = 5
    coeffs = np.polyfit(ns, ts, degree)
    p = np.poly1d(coeffs)
    plt.plot(ns, [p(n) for n in ns], '-b')



'''

EJERCICIO: Programa en Python los algoritmos 'queHace1', 'queHace2' y 'queHace3'
que has programado anteriormente en C++. Usa el código anterior para visualizar 
los tiempos de ejecución de estos tres programas, para determinar cuál es más 
eficiente en la práctica, así como para visualizar la función de coste que 
define, para cada algoritmo, su orden de complejidad.

'''
def queHace1(v):
    mejor = 0;
    for i in range(0, len(v)):
        for j in range(i, len(v)):
            suma = 0;
            for k in range (i, len(v)):
                suma = suma + v[k];
                if  suma > mejor:
                    mejor = suma;
    return mejor;

def queHace2(v):
    mejor = 0;
    for i in range(0, len(v)):
        suma = 0;
        for k in range (i, len(v)):
            suma = suma + v[k];
            if  suma > mejor:
                mejor = suma;
    return mejor;

def queHace3(v):
    i = 0; mejor = 0; suma = 0;
    while (i < len(v)):
        suma = max((suma + v[i]), v[i]);
        mejor = max (mejor,suma);
        i += 1;
    return mejor

def main1():
    
    MAX_LEN = 500  # Maximum length of input list.

    # Initialise results containers:
    
    lengths_queHace1  = []
    times_queHace1    = []
    
    lengths_queHace2 = []
    times_queHace2   = []
    
    lengths_queHace3 = []
    times_queHace3   = []
    

    for length in range(0, MAX_LEN, 10):
        
        # Generate random values:
        
        v = random.sample(range(100000), 50)

        # Time execution (queHace1):
        
        start = time.perf_counter()
        queHace1(v)
        end = time.perf_counter()

        # Store results (queHace1):
        
        lengths_queHace1.append(length)
        times_queHace1.append(end - start)

        # Time execution (queHace2):
        
        start = time.perf_counter()
        queHace2(v)
        end = time.perf_counter()

        # Store results (queHace2):
        
        lengths_queHace2.append(length)
        times_queHace2.append(end - start)
        
        # Time execution (queHace3):
        
        start = time.perf_counter()
        queHace3(v)
        end = time.perf_counter()

        # Store results (queHace3):
        
        lengths_queHace3.append(length)
        times_queHace3.append(end - start)
        
        
        
    # Plot results
    
    plt.style.use("dark_background")
    plt.figure().canvas.manager.set_window_title("Algoritmos queHaceX - Time Complexity")
    plt.xlabel("List Length")
    plt.ylabel("Execution Time (s)")
    plt.plot(lengths_queHace1, times_queHace1, label="queHace1()")
    plt.plot(lengths_queHace2, times_queHace2, label="queHace2()")
    plt.plot(lengths_queHace3, times_queHace3, label="queHace3()")
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    
    # Polynomial fit
    """
    Sólamente mostramos el órden de complejidad de la más eficiente, queHace3,
    ya que si se generan gráficas de las tres funciones, visualmente no queda
    un resultado apreciable. Para ver una comparativa de todas a la vez,
    sólo hay que quitar el comillado triple que encontramos debajo.
    """
    
    degree = 5
    ns = np.linspace(1, 1000, 100, dtype = int)
    
    """
    ts = [timeit.timeit('queHace1(lst)',
                    setup='lst=list(range({})); random.shuffle(lst)'.format(n),
                    globals=globals(),
                    number=1000)
          for n in ns]
    plt.plot(ns, ts, 'or')

    
    coeffs = np.polyfit(ns, ts, degree)
    p = np.poly1d(coeffs)
    plt.title("Comparación de órdenes")
    plt.plot(ns, [p(n) for n in ns], '-g', label = "queHace1")
    
    ts = [timeit.timeit('queHace2(lst)',
                    setup='lst=list(range({})); random.shuffle(lst)'.format(n),
                    globals=globals(),
                    number=1000)
          for n in ns]
    plt.plot(ns, ts, 'or')

    coeffs = np.polyfit(ns, ts, degree)
    p = np.poly1d(coeffs)
    plt.plot(ns, [p(n) for n in ns], '-y', label = "queHace2")
    
    """
    
    ts = [timeit.timeit('queHace3(lst)',
                    setup='lst=list(range({})); random.shuffle(lst)'.format(n),
                    globals=globals(),
                    number=1000)
          for n in ns]
    plt.plot(ns, ts, 'or')

    coeffs = np.polyfit(ns, ts, degree)
    p = np.poly1d(coeffs)
    plt.plot(ns, [p(n) for n in ns], '-b', label = "queHace3")
    
    plt.legend(loc = "upper left")
    
    


