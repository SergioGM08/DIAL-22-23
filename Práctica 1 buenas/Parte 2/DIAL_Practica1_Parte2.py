#!/usr/bin/env python3
# -*- coding: utf-8 -*-



'''

    PRÁCTICA 1 (PARTE 2): ANÁLISIS DE LA EFICIENCIA DE ALGORITMOS DE 
                          ORDENACIÓN Y DE BÚSQUEDA EN PYTHON

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



# ALGORITMOS DE ORDENACION (SELECCIÓN E INSERCIÓN)



'''

EJERCICIO 1: Programa en Python los algoritmos de ordenación por selección y
ordenación por inserción estudiados en las clases de teoría. Usa el código 
visto en las sesiones de laboratorio para visualizar los tiempos de ejecución
de estos dos programas, para determinar cuál es más eficiente en la práctica, 
así como para visualizar la función de coste que define, para cada algoritmo, 
su orden de complejidad.

'''



def ord_seleccion(v): # Ordenación por selección (visto en clase)
    N = len(v);
    for i in range(0, N-1):
        pmin = i;
        for j in range(i+1, N):
            if (v[j] < v[pmin]): 
                pmin = j;
        k = v[i];
        v[i] = v[pmin];
        v[pmin] = k;



def ord_insercion(v): # Ordenación por inserción (visto en clase)
    N = len(v);
    for i in range(1, N):
        elem = v[i];
        j = i-1;
        while ((j>=0) and (elem < v[j])):
            v[j+1] = v[j];
            j = j-1;
        v[j+1] = elem;



def main1():
    
    MAX_LEN = 1000  # Maximum length of input list

    # Initialise results containers
    
    lengths_sort_sel  = []
    times_sort_sel    = []

    lengths_sort_ins  = []
    times_sort_ins    = []

    for length in range(0, MAX_LEN, 5) :
        
        # Generate random lists
        
        v  = [random.randint(-99, 99) for _ in range(length)]
        w = []
        for elem in v :
            w.append(elem)

        # Time execution (algoritmo de ordenacion por selección)
        
        start = time.perf_counter()
        ord_seleccion(v)
        end = time.perf_counter()

        # Store results
        
        lengths_sort_sel.append(length)
        times_sort_sel.append(end - start)

        # Time execution (algoritmo de ordenacion por inserción)
        
        start = time.perf_counter()
        ord_insercion(w)
        end = time.perf_counter()

        # Store results
        
        lengths_sort_ins.append(length)
        times_sort_ins.append(end - start)
        
        

    # Plot results
    
    plt.style.use("dark_background")
    plt.figure().canvas.manager.set_window_title("Algoritmos de ordenacion - Time Complexity")
    plt.xlabel("List Length")
    plt.ylabel("Execution Time (s)")
    plt.plot(lengths_sort_sel, times_sort_sel, label="ord_seleccion()")
    plt.plot(lengths_sort_ins, times_sort_ins, label="ord_insercion()")
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    """
    Se grafica sólo el método de ordenación por inserción, a priori más eficiente, 
    con el objetivo de visualizar mejor su orden de complejidad. Para ver el 
    método de ordenación por selección, cambiar las triples comillas.
    
    """
    #Polynomial fit
    
    degree = 5
    ns = np.linspace(1, 3000, 100, dtype = int)
    plt.title ("Orden del método")
    """
    ts = [timeit.timeit('ord_seleccion(lst)',
                    setup='lst=list(range({})); random.shuffle(lst)'.format(n),
                    globals=globals(),
                    number=100)
          for n in ns]

    plt.plot(ns, ts, 'or')

    
    coeffs = np.polyfit(ns, ts, degree)
    p = np.poly1d(coeffs)
    plt.plot(ns, [p(n) for n in ns], '-g', label = "ord_sel")
    """
    
    ts = [timeit.timeit('ord_insercion(lst)',
                    setup='lst=list(range({})); random.shuffle(lst)'.format(n),
                    globals=globals(),
                    number=100)
          for n in ns]
    
    plt.plot(ns, ts, 'or')

    coeffs = np.polyfit(ns, ts, degree)
    p = np.poly1d(coeffs)
    plt.plot(ns, [p(n) for n in ns], '-b', label = "ord_ins")
    #"""
    
    plt.legend(loc = "upper left")


# ALGORITMOS DE ORDENACION (QUICKSORT Y MERGESORT)


    
'''

EJERCICIO 2: Programa en Python los algoritmos de ordenación "quicksort" 
y "mergesort", y compara su eficiencia con los algoritmos de ordenación 
anteriores.

'''   


def quickSort(v): # Ordenación por el método quicksort
    N = len(v);
    if N <= 1:
        return v
    else:
        part_pos = 0;
        for i in range(1, N):
            if v[i] <= v[0]:
                part_pos += 1;
                permute = v[i];
                v[i] = v[part_pos];
                v[part_pos] = permute;
                
    permute = v[0];
    v[0] = v[part_pos];
    v[part_pos] = permute;
    
    l = quickSort(v[0:part_pos]);
    r = quickSort(v[part_pos+1:N]);
    
    v = l + [v[part_pos]] + r;
    return v
       

def mergeSort(myList): # Ordenación por el método mergesort
    N = len(myList);
    
    if (N > 1): #Cambiado de != 1 a N > 1 para abordar caso base correctamente
        m = N//2;
        (iz, dr) = (myList[:m], myList [m:]);
        mergeSort(iz);
        mergeSort(dr);
        (I, D) = (len(iz), len(dr)); 
        i = 0; j = 0; k = 0;
        
        while (i < I and j < D):
            if (iz[i] <= dr[j]):
                myList[k] = iz[i];
                i += 1
            else:
                myList[k] = dr[j];
                j += 1;
            k += 1;
        while (i < I):
            myList[k] = iz[i];
            i += 1;
            k += 1;
        while (j < D):
            myList[k] = dr[j];
            j += 1;
            k += 1;


def main2():
    
    MAX_LEN = 1000  # Maximum length of input list
    
    # Initialise results containers
    
    lengths_sort_sel = []
    times_sort_sel   = []

    lengths_sort_ins = []
    times_sort_ins   = []
    
    lengths_quick = []
    times_quick   = []
    
    lengths_merge = []
    times_merge   = []

    for length in range(0, MAX_LEN, 100) :
        
        # Generate random list
        
        v = [random.randint(-99, 99) for _ in range(length)] # Lista aleatoria
        v1 = []
        v2 = []
        v3 = []
        for elem in v :
            v1.append(elem)
            v2.append(elem)
            v3.append(elem)
        
        # Time execution (algoritmo de ordenacion por selección)
        
        start = time.perf_counter()
        ord_seleccion(v)
        end = time.perf_counter()

        # Store results
        
        lengths_sort_sel.append(length)
        times_sort_sel.append(end - start)

        # Time execution (algoritmo de ordenacion por inserción)
        
        start = time.perf_counter()
        ord_insercion(v1)
        end = time.perf_counter()

        # Store results
        
        lengths_sort_ins.append(length)
        times_sort_ins.append(end - start)
        
        # Time execution (algoritmo de ordenacion quicksort)

        start = time.perf_counter()
        quickSort(v2)
        end = time.perf_counter()
        
        # Store results
        
        lengths_quick.append(length)
        times_quick.append(end - start)
        
        # Time execution (algoritmo de ordenacion mergesort)

        start = time.perf_counter()
        mergeSort(v3)
        end = time.perf_counter()
        
        # Store results
        
        lengths_merge.append(length)
        times_merge.append(end - start)

        

    # Plot results
    
    plt.style.use("dark_background")
    plt.figure().canvas.manager.set_window_title("Algoritmos de ordenacion - Time Complexity")
    plt.xlabel("List Length")
    plt.ylabel("Execution Time (s)")
    plt.plot(lengths_sort_sel, times_sort_sel, label="ord_seleccion()")
    plt.plot(lengths_sort_ins, times_sort_ins, label="ord_insercion()")
    plt.plot(lengths_merge, times_merge, label="mergeSort()")
    plt.plot(lengths_quick, times_quick, label="quickSort()")
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    """
    Gracias a que mergeSort y quickSort se comportan de forma parecida,
    son apreciables en la misma gráfica sin verse perjudicada la observación.
    Aun así, he comentado mergeSort para que de base sólo grafique quickSort.
    
    """
    # Polynomial fit
    
    degree = 5
    ns = np.linspace(1, 3000, 100, dtype = int)
    plt.title("Orden del método")
    
    """
    ts = [timeit.timeit('mergeSort(lst)',
                    setup='lst=list(range({})); random.shuffle(lst)'.format(n),
                    globals=globals(),
                    number=1000)
          for n in ns]
    plt.plot(ns, ts, 'or')

    coeffs = np.polyfit(ns, ts, degree)
    p = np.poly1d(coeffs)
    plt.plot(ns, [p(n) for n in ns], '-b', label = "Merge")
    
    """
    
    ts = [timeit.timeit('quickSort(lst)',
                    setup='lst=list(range({})); random.shuffle(lst)'.format(n),
                    globals=globals(),
                    number=1000)
          for n in ns]
    plt.plot(ns, ts, 'or')
    
    coeffs = np.polyfit(ns, ts, degree)
    p = np.poly1d(coeffs)
    plt.plot(ns, [p(n) for n in ns], '-g', label = "Quick")
    #"""
    
    plt.legend(loc = "upper left")



# ALGORITMOS DE BÚSQUEDA (SECUENCIAL Y BINARIA)

'''

EJERCICIO 3: Programa en Python los algoritmos de búsqueda secuencial y 
búsqueda binaria, y compara su eficiencia. Visualiza sus ordenes de 
complejidad.

'''  

       
def busq_sec(lst, x): # Búsqueda secuencial
    N = len(lst); i = 0;
    while i < N and lst[i] != x:
        i += 1;
    return (0 <= i < N)


def busq_bin(lst, x): # Búsqueda binaria (o dicotómica)
    N = len(lst); l = 0; u = N-1;
    while l <= u:
        m = (l + u)//2;
        if x < lst[m]:
            u = m-1;
        elif x > lst[m]:
            l = m+1;
        else:
            return True
    else:
        return False


def main3():
    
    MAX_LEN = 1000  # Maximum length of input list
    
    # Initialise results containers
    
    lengths_busq_sec = []
    times_busq_sec   = []

    lengths_busq_bin = []
    times_busq_bin   = []

    for length in range(0, MAX_LEN, 10) :
        
        # Generate random list
        
        v = [random.randint(-99, 99) for _ in range(length)]
        x = random.randint(-99, 99)
        
        # Sort the list
        
        ord_insercion(v)

        # Time execution (algoritmo de búsqueda secuencial)
        
        start = time.perf_counter()
        busq_sec(v, x)
        end = time.perf_counter()

        # Store results
        
        lengths_busq_sec.append(length)
        times_busq_sec.append(end - start)

        # Time execution (algoritmo de búsqueda binaria)
        
        start = time.perf_counter()
        busq_bin(v, x)
        end = time.perf_counter()

        # Store results
        
        lengths_busq_bin.append(length)
        times_busq_bin.append(end - start)



    # Plot results
    
    plt.style.use("dark_background")
    plt.figure().canvas.manager.set_window_title("Algoritmos de búsqueda - Time Complexity")
    plt.xlabel("List Length")
    plt.ylabel("Execution Time (s)")
    plt.plot(lengths_busq_sec, times_busq_sec, label="busq_sec()")
    plt.plot(lengths_busq_bin, times_busq_bin, label="busq_bin()")
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    """
    Se grafica sólo el método de búsqueda binaria, más eficiente, 
    con el objetivo de visualizar mejor su orden de complejidad. Para ver el 
    método de búsqueda secuencial, cambiar las triples comillas.
    
    """
    # Polynomial fit
    
    degree = 10
    ns = np.linspace(1, 10000, 100, dtype = int)
    plt.title("Orden del método")
    
    """
    ts = [timeit.timeit('busq_sec(lst, random.randint(lst[0], lst[len(lst)-1]))',
                    setup='lst=list(range({}))'.format(n),
                    globals=globals(),
                    number=1000)
          for n in ns]
    
    plt.plot(ns, ts, 'or')


    coeffs = np.polyfit(ns, ts, degree)
    p = np.poly1d(coeffs)
    plt.plot(ns, [p(n) for n in ns], '-g', label = "busq_sec")
    
    """
    
    ts = [timeit.timeit('busq_bin(lst, random.randint(lst[0], lst[len(lst)-1]))',
                    setup='lst=list(range({}))'.format(n),
                    globals=globals(),
                    number=1000)
          for n in ns]
    
    plt.plot(ns, ts, 'or')


    coeffs = np.polyfit(ns, ts, degree)
    p = np.poly1d(coeffs)
    plt.plot(ns, [p(n) for n in ns], '-b', label = "busc_bin")
    #"""
    
    plt.legend(loc = "upper left")
    
