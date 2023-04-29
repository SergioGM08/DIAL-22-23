#!/usr/bin/env python3
# -*- coding: utf-8 -*-



'''

    PRÁCTICA 2 (PARTE 2): DISEÑO DE ALGORITMOS ITERATIVOS EFICIENTES EN PYTHON

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



def raiz_ent1(n):     # O(√n)
    r = 0

    while n >= (r+1)*(r+1):
        r += 1

    return r




def raiz_ent2(n):     # O(n)
    r = n

    while r * r > n:
        r -= 1

    return r




def raiz_ent3(n, a, b):     #(log(n))
    
    y = b + 1
    r = a

    while y != r + 1:
        h = (r + y) // 2

        if h * h <= n:
            r = h
        else:
            y = h

    return r
        


def raiz_ent4(n, a, b):     # O(log(n))
    r = 0

    if b == a + 1:
        r = a
    else:
        m = (a + b) // 2

        if m * m <= n:
            r = raiz_ent4(n, m, b)
        else:
            r = raiz_ent4(n, a, m)

    return r






def main1():
    
    MAX_LEN = 135  # Maximum length of input list.

    # Initialise results containers:
    
    lengths_raiz_ent1  = []
    times_raiz_ent1    = []

    lengths_raiz_ent2  = []
    times_raiz_ent2    = []
    
    lengths_raiz_ent3  = []
    times_raiz_ent3    = []
    
    lengths_raiz_ent4  = []
    times_raiz_ent4    = []
    

    for length in range(0, MAX_LEN, 1):
        
        # Generate random values:
        
        n = random.randint(length, 10*length)
            
        # Time execution (raiz_ent1)
    
        start = time.perf_counter()
        raiz_ent1(n)
        end = time.perf_counter()

        # Store results
    
        lengths_raiz_ent1.append(length)
        times_raiz_ent1.append(end - start)

        # Time execution (raiz_ent2)
    
        start = time.perf_counter()
        raiz_ent2(n)
        end = time.perf_counter()

        # Store results
    
        lengths_raiz_ent2.append(length)
        times_raiz_ent2.append(end - start)
        
        # Time execution (raiz_ent3)
    
        start = time.perf_counter()
        raiz_ent3(n, 0, n//2 + 1)
        end = time.perf_counter()

        # Store results
    
        lengths_raiz_ent3.append(length)
        times_raiz_ent3.append(end - start)
        
        # Time execution (raiz_ent4)
    
        start = time.perf_counter()
        raiz_ent4(n, 0, n//2 + 1)
        end = time.perf_counter()

        # Store results
    
        lengths_raiz_ent4.append(length)
        times_raiz_ent4.append(end - start)
        
    # Plot results
    
    plt.style.use("dark_background")
    plt.figure().canvas.manager.set_window_title("Algoritmos raiz cuadrada entera - Time Complexity")
    plt.xlabel("List Length")
    plt.ylabel("Execution Time (s)")
    plt.plot(lengths_raiz_ent1, times_raiz_ent1, label="raiz_ent1()")
    plt.plot(lengths_raiz_ent2, times_raiz_ent2, label="raiz_ent2()")
    plt.plot(lengths_raiz_ent3, times_raiz_ent3, label="raiz_ent3()")
    plt.plot(lengths_raiz_ent4, times_raiz_ent4, label="raiz_ent4()")
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    pass
    
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    print("\n")
    n = int(input("1.- raiz_ent1() | 2.- raiz_ent2() | 3.- raiz_ent3() | 4.- raiz_ent4() "))
    
    # Polynomial fit
    
    if n == 1 :
    
            ns = np.linspace(0, 1000, 100, dtype = int)
            ts = [timeit.timeit('raiz_ent1(lst[0])',
                    setup='lst=list(range({})); random.shuffle(lst)'.format(n),
                    globals=globals(),
                    number=1000)
                  for n in ns]

            plt.plot(ns, ts, 'or')

            degree = 5
            coeffs = np.polyfit(ns, ts, degree)
            p = np.poly1d(coeffs)
            plt.plot(ns, [p(n) for n in ns], '-b')
        
    elif n == 2 :
    
            ns = np.linspace(0, 1000, 100, dtype = int)
            ts = [timeit.timeit('raiz_ent2(lst[0])',
                    setup='lst=list(range({})); random.shuffle(lst)'.format(n),
                    globals=globals(),
                    number=1000)
                  for n in ns]

            plt.plot(ns, ts, 'or')

            degree = 5
            coeffs = np.polyfit(ns, ts, degree)
            p = np.poly1d(coeffs)
            plt.plot(ns, [p(n) for n in ns], '-b')
    
    elif n == 3 :
    
            ns = np.linspace(0, 1000, 100, dtype = int)
            ts = [timeit.timeit('raiz_ent3(lst[0])',
                    setup='lst=list(range({})); random.shuffle(lst)'.format(n),
                    globals=globals(),
                    number=1000)
                  for n in ns]

            plt.plot(ns, ts, 'or')

            degree = 5
            coeffs = np.polyfit(ns, ts, degree)
            p = np.poly1d(coeffs)
            plt.plot(ns, [p(n) for n in ns], '-b')
        
    elif n == 4 :
        
            ns = np.linspace(0, 1000, 100, dtype = int)
            ts = [timeit.timeit('raiz_ent4(lst[0])',
                    setup='lst=list(range({})); random.shuffle(lst)'.format(n),
                    globals=globals(),
                    number=1000)
                  for n in ns]

            plt.plot(ns, ts, 'or')

            degree = 5
            coeffs = np.polyfit(ns, ts, degree)
            p = np.poly1d(coeffs)
            plt.plot(ns, [p(n) for n in ns], '-b')




                
def potencia1(a, b):

    pass



def potencia2(a, b):
    
    pass





def main2():
    
    MAX_LEN = 1000  # Maximum length of input list.

    # Initialise results containers:
    
    lengths_potencia1  = []
    times_potencia1    = []
    
    lengths_potencia2  = []
    times_potencia2    = []

    for length in range(0, MAX_LEN, 10):
        
        # Generate values:
    
        a = 2
        b = length

        # Time execution (potencia1):
        
        start = time.perf_counter()
        potencia1(a, b)
        end = time.perf_counter()

        # Store results (potencia1):
        
        lengths_potencia1.append(length)
        times_potencia1.append(end - start)

        # Time execution (potencia2):
        
        start = time.perf_counter()
        potencia2(a, b)
        end = time.perf_counter()

        # Store results (potencia2):
        
        lengths_potencia2.append(length)
        times_potencia2.append(end - start)
        
    # Plot results
    
    plt.style.use("dark_background")
    plt.figure().canvas.manager.set_window_title("Algoritmos raiz cuadrada entera - Time Complexity")
    plt.xlabel("List Length")
    plt.ylabel("Execution Time (s)")
    plt.plot(lengths_potencia1, times_potencia1, label="potencia1()")
    plt.plot(lengths_potencia2, times_potencia2, label="potencia2()")
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    ns = np.linspace(0, 1000, 100, dtype = int)
    ts = [timeit.timeit('potencia2(2, len(lst))',
            setup='lst=list(range({})); random.shuffle(lst)'.format(n),
            globals=globals(),
            number=1000)
          for n in ns]

    plt.plot(ns, ts, 'or')

    degree = 5
    coeffs = np.polyfit(ns, ts, degree)
    p = np.poly1d(coeffs)
    plt.plot(ns, [p(n) for n in ns], '-b')





def log_ent(n, b):

    pass





def main3():
    
    MAX_LEN = 1300  # Maximum length of input list.

    # Initialise results containers:
    
    lengths_log_ent  = []
    times_log_ent    = []

    for length in range(0, MAX_LEN, 5):
        
        # Generate values:
    
        a = length
        b = 2

        # Time execution (log_ent):
        
        start = time.perf_counter()
        log_ent(a, b)
        end = time.perf_counter()

        # Store results (log_ent):
        
        lengths_log_ent.append(length)
        times_log_ent.append(end - start)
        
    # Plot results
    
    plt.style.use("dark_background")
    plt.figure().canvas.manager.set_window_title("Algoritmos raiz cuadrada entera - Time Complexity")
    plt.xlabel("List Length")
    plt.ylabel("Execution Time (s)")
    plt.plot(lengths_log_ent, times_log_ent, label="log_ent()")
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    ns = np.linspace(0, 10000, 100, dtype = int)
    ts = [timeit.timeit('log_ent(len(lst), 2)',
            setup='lst=list(range({})); random.shuffle(lst)'.format(n),
            globals=globals(),
            number=1000)
          for n in ns]

    plt.plot(ns, ts, 'or')

    degree = 5
    coeffs = np.polyfit(ns, ts, degree)
    p = np.poly1d(coeffs)
    plt.plot(ns, [p(n) for n in ns], '-b')