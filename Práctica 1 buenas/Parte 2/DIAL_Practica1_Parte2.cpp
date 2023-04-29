#include <iostream>
#include <stdio.h>
#include <time.h>


using namespace std ;


/*

    PRÁCTICA 1 (PARTE 2): ANÁLISIS DE LA EFICIENCIA DE ALGORITMOS DE
                          ORDENACIÓN Y DE BÚSQUEDA EN C/C++

    ASIGNATURA: DISEÑO DE ALGORITMOS
    CURSO:      2022-2023
    SUBGRUPO:   U1 / U2

    APELLIDOS: González Montero
    NOMBRE:	   Sergio

 
*/



/* ALGORITMOS DE ORDENACIÓN (SELECCIÓN E INSERCIÓN) */



/*
 
 EJERCICIO 1: Escribe el código en C++ de los algoritmos
 de ordenación por selección y de ordenación por inserción.
 (OPCIONAL) Escribe también el código en C++ de los algoritmos
 de ordenación quicksort y mergesort.
 
 */

void selectionSort(int v[], int N){
	int aux;

	for (int i = 0; i < N-1; i++){
		int pmin = i;
		
		for (int j = i+1; j < N; j++){
			
			if (v[j] < v[pmin]) pmin = j;
		}
		aux = v[i];
		v[i] = v[pmin];
		v[pmin] = aux;
	}
}

void insertionSort(int v[], int N){
	
	for (int i = 1; i < N; i++){
		
		int elem = v[i];
		int j = i-1;
		
		while (j >= 0 and elem < v[j]){
			v[j+1] = v[j];
			j = j-1;
		}
		v[j+1] = elem;
	}
}


int main1(){

	/* EJECUCIÓN DE LOS PROGRAMAS */
    
    const int DIM = 50 ;
    int v[DIM] ;
    int N ;
    
    cout << "Introduce la longitud del vector: " ;
    cin >> N ;
    cout << endl ;
    
    cout << "Introduce las " << N << " componentes del vector: \n" ;
    for (int i = 0 ; i < N ; i++) cin >> v[i] ;
    cout << endl ;

    cout << "Vector = " ;
    for (int i = 0 ; i < N ; i++) cout << v[i] << " " ;
    cout << endl ;
    
    int w[DIM] ;
    for (int i = 0 ; i < N ; i++) w[i] = v[i] ;
    
    cout << "Resultado de la funcion 'selectionSort': " ;
        selectionSort(w, N) ;
        for (int i = 0 ; i < N ; i++) cout << w[i] << " " ;
        cout << endl << endl ;
    cout << endl ;
    
    cout << "Resultado de la funcion 'insertionSort': " ;
        insertionSort(w, N) ;
        for (int i = 0 ; i < N ; i++) cout << w[i] << " " ;
        cout << endl << endl ;
    cout << endl ;
	
	    
    /* MEDIDAS DEL TIEMPO DE EJECUCION DE LOS PROGRAMAS */
  
    int repeticiones ;
    int tamanyos[DIM] ;
    double tiempos[DIM] ;
    clock_t t1, t2 ;
    
    cout << "Introduce el numero de repeticiones: " ;
    cin >> repeticiones ;
    cout << endl ;

    for (int i = 0 ; i < N ; i++) tamanyos[i] = i + 1 ;
  	
  	/* MEDIDA DE TIEMPO PARA selectionSort */
  	/*Clonar vector v en w*/
  	
    cout << "Medidas del tiempo de ejecucion del programa 'selectionSort': \n" << endl ;

    for (int k = 0 ; k < N ; k++){
        
       t1 = clock();
       
       for (int i = 0 ; i < repeticiones ; i++){
           
          selectionSort(v, tamanyos[k]) ;
          
       }
       
       t2 = clock() ;
       
       tiempos[k] = (double(t2 - t1) / CLOCKS_PER_SEC) / repeticiones ;
       
    }
    
    for (int k = 0 ; k < N ; k++)
         cout << "Longitud = " << tamanyos[k] << "; Tiempo = " << tiempos[k] << endl ;
    
    cout << endl ;
    
    /* MEDIDA DEL TIEMPO DE EJECUCIÓN PARA insertionSort */
    
    /*Clonar vector v en w*/
    
    cout << "Medidas del tiempo de ejecucion del programa 'insertionSort': \n" << endl ;

    for (int k = 0 ; k < N ; k++){
        
       t1 = clock();
       
       for (int i = 0 ; i < repeticiones ; i++){
           
          insertionSort(v, tamanyos[k]) ;
          
       }
       
       t2 = clock() ;
       
       tiempos[k] = (double(t2 - t1) / CLOCKS_PER_SEC) / repeticiones ;
       
    }
    
    for (int k = 0 ; k < N ; k++)
         cout << "Longitud = " << tamanyos[k] << "; Tiempo = " << tiempos[k] << endl ;
    
    cout << endl ;
}


void quickSort(int v[],int inicio,int fin){
    int m, i, j, piv;
    m = (inicio + fin)/2;
    piv = v[m];
    i = inicio;
    j = fin;
	while (v[i] < piv) i++;
    while (v[j] > piv) j--;
    if(i <= j){
        int aux;
        aux = v[i];
        v[i] = v[j]; /*intercambia v[i] con v[j] */
        v[j] = aux;
		i++;
        j--;
    }
    while (i <= j);
    if (inicio < j) quickSort(v,inicio,j); /*mismo proceso con sublista izquierda*/
    if (i < fin) quickSort(v,i,fin); /*mismo proceso con sublista derecha*/
}
/* Función auxiliar para la mezcla: merge*/

void merge (int v[], int inicio, int medio, int fin){
	int i, j, k;
	int izelem = medio - inicio +1 ;
	int drelem = fin - medio;
	int iz[izelem];
	int dr[drelem];
	
	/* Creación de parte izquierda y derecha */
	
	for (int i = 0; i < izelem; i++){
		iz[i] = v[inicio + i];
	}
	for (int j = 0; j < drelem; j++){
		dr[j] = v[medio + 1 + j];
	}
	i = 0, j = 0, k = inicio;
	
	while (i < izelem and j < drelem){
		if (iz[i] <= dr[j]){
			v[k] = iz[i];
			i++;
		}else{
			v[k] = dr[j];
			j++;
		}
		k++;
	}
	while (i < izelem){
		v[k] = iz[i];
		i++;
		k++;
	}
	while (j < drelem){
		v[k] = dr[j];
		j++;
		k++;
	}
	
}

void mergeSort(int v[], int inicio, int fin){
	int medio ;
    if (inicio < fin){
        medio = (inicio + fin)/2;
        mergeSort(v, inicio, medio);
        mergeSort(v, medio + 1, fin);
        merge(v,inicio, medio, fin);
    }
}


/* ALGORITMOS DE BÚSQUEDA (SECUENCIAL Y BINARIA) */



/*
 
 EJERCICIO 2: Escribe el código en C++ de los algoritmos
 de búsqueda secuencias y de búsqueda binaria.
 
 */



int busquedaSecuencial(int v[], int longitud, int item){
	int i;
	i = 0;
	while (i < longitud and v[i] != item){
		i++;
	}
	if (i == longitud)
		return -1 ;
	else
		return (0 <= i && i < longitud);
	
}


int busquedaBinaria(int v[], int item, int s1, int s2){
	
    while (s1 <= s2){
    	
        int m = (s1 + s2) / 2;
        
        if (item == v[m])
            return m;
        else if (item < v[m])
            s2 = m - 1;
        else
            s1 = m + 1;
    }
    return -1;
}


int main()
{
    
    
    /* DATOS DE ENTRADA */
    
    
    const int DIM = 50 ;
    int v[DIM] ;
    int N ;
   
    cout << "Introduce la longitud del vector: " ;
    cin >> N ;
    cout << endl ;
    
    cout << "Introduce las " << N << " componentes del vector: \n" ;
    for (int i = 0 ; i < N ; i++) cin >> v[i] ;
    cout << endl ;
    
    
    /* ALGORITMOS DE ORDENACIÓN (SELECCIÓN E INSERCIÓN) */
    
    
    int w[DIM] ;
    for (int i = 0 ; i < N ; i++) w[i] = v[i] ;
    
    cout << "Ordenar el vector (1.- Seleccion | 2.- Insercion): " ;
    int opcion ;
    cin >> opcion ;
    cout << endl ;
    
    if (opcion == 1) {
        
        cout << "Resultado de la funcion 'selectionSort': " ;
        selectionSort(w, N) ;
        for (int i = 0 ; i < N ; i++) cout << w[i] << " " ;
        cout << endl << endl ;
        
    }
        
    if (opcion == 2) {
        
        cout << "Resultado de la funcion 'insertionSort': " ;
        insertionSort(w, N) ;
        for (int i = 0 ; i < N ; i++) cout << w[i] << " " ;
        cout << endl << endl ;
        
    }
    
    
    /* ALGORITMOS DE BÚSQUEDA (SECUENCIAL Y BINARIA) */
        
    
    cout << "Introduce el elemento a buscar en el vector ordenado: " ;
    int item ;
    cin >> item ;
    cout << endl ;
    
    if (busquedaSecuencial(w, N, item) != -1) cout << "SI encontrado (busqueda secuencial)" << endl ;
    else cout << "NO encontrado (busqueda secuencial)" << endl ;
    cout << endl ;
    
    if (busquedaBinaria(w, item, 0, N) != -1) cout << "SI encontrado (busqueda binaria)" << endl ;
    else cout << "NO encontrado (busqueda binaria)" << endl ;
    cout << endl ;
        
    
    /* MEDIDAS DEL TIEMPO DE EJECUCION DE LOS PROGRAMAS */
  
    
    int repeticiones ;
    int tamanyos[DIM] ;
    double tiempos[DIM] ;
    clock_t t1, t2 ;
    
    cout << "Introduce el numero de repeticiones: " ;
    cin >> repeticiones ;
    cout << endl ;

    for (int i = 0 ; i < N ; i++) tamanyos[i] = i + 1 ;
    
    
    /* TIEMPOS DE EJECUCIÓN DE LOS ALGORITMOS DE ORDENACIÓN (SELECCIÓN E INSERCIÓN) */
    
    
    for (int i = 0 ; i < N ; i++) w[i] = v[i] ;
  
    cout << "Medidas del tiempo de ejecucion del programa 'selectionSort': \n" << endl ;

    for (int k = 0 ; k < N ; k++){
        
       t1 = clock();
       
       for (int i = 0 ; i < repeticiones ; i++){
           
          selectionSort(w, tamanyos[k]) ;
          
       }
       
       t2 = clock() ;
       
       tiempos[k] = (double(t2 - t1) / CLOCKS_PER_SEC) / repeticiones ;
       
    }
    
    for (int k = 0 ; k < N ; k++)
         cout << "Longitud = " << tamanyos[k] << "; Tiempo = " << tiempos[k] << endl ;
    
    cout << endl ;
    
    
    for (int i = 0 ; i < N ; i++) w[i] = v[i] ;
    
    cout << "Medidas del tiempo de ejecucion del programa 'insertionSort': \n" << endl ;

    for (int k = 0 ; k < N ; k++){
        
       t1 = clock();
       
       for (int i = 0 ; i < repeticiones ; i++){
           
          insertionSort(w, tamanyos[k]) ;
          
       }
       
       t2 = clock() ;
       
       tiempos[k] = (double(t2 - t1) / CLOCKS_PER_SEC) / repeticiones ;
       
    }
    
    for (int k = 0 ; k < N ; k++)
         cout << "Longitud = " << tamanyos[k] << "; Tiempo = " << tiempos[k] << endl ;
    
    cout << endl ;

    
    /* (OPCIONAL) TIEMPOS DE EJECUCIÓN DE LOS ALGORITMOS DE ORDENACIÓN (MERGESORT Y QUICKSORT) */
    
    cout << "Medidas del tiempo de ejecucion del programa 'mergeSort': \n" << endl ;

    for (int k = 0 ; k < N ; k++){
        
       t1 = clock();
       
       for (int i = 0 ; i < repeticiones ; i++){
           
          mergeSort(w, tamanyos[k], tamanyos[0]) ;
          
       }
       
       t2 = clock() ;
       
       tiempos[k] = (double(t2 - t1) / CLOCKS_PER_SEC) / repeticiones ;
       
    }
    
    for (int k = 0 ; k < N ; k++)
         cout << "Longitud = " << tamanyos[k] << "; Tiempo = " << tiempos[k] << endl ;
    
    cout << endl ;
    
    
    for (int i = 0 ; i < N ; i++) w[i] = v[i] ;
    
    cout << "Medidas del tiempo de ejecucion del programa 'quickSort': \n" << endl ;

    for (int k = 0 ; k < N ; k++){
        
       t1 = clock();
       
       for (int i = 0 ; i < repeticiones ; i++){
           
          quickSort(w, tamanyos[k], tamanyos[0]) ;
          
       }
       
       t2 = clock() ;
       
       tiempos[k] = (double(t2 - t1) / CLOCKS_PER_SEC) / repeticiones ;
       
    }
    
    for (int k = 0 ; k < N ; k++)
         cout << "Longitud = " << tamanyos[k] << "; Tiempo = " << tiempos[k] << endl ;
    
    cout << endl ;
    
    /* TIEMPOS DE EJECUCIÓN DE LOS ALGORITMOS DE BÚSQUEDA (SECUENCIAL Y BINARIA) */
    
    
    cout << "Medidas del tiempo de ejecucion del programa 'busquedaSecuencial': \n" << endl ;

    for (int k = 0 ; k < N ; k++){
        
       t1 = clock();
       
       for (int i = 0 ; i < repeticiones ; i++){
           
          busquedaSecuencial(v, tamanyos[k], tamanyos[0]) ;
          
       }
       
       t2 = clock() ;
       
       tiempos[k] = (double(t2 - t1) / CLOCKS_PER_SEC) / repeticiones ;
       
    }
    
    for (int k = 0 ; k < N ; k++)
         cout << "Longitud = " << tamanyos[k] << "; Tiempo = " << tiempos[k] << endl ;
    
    cout << endl ;
    
    
    cout << "Medidas del tiempo de ejecucion del programa 'busquedaBinaria': \n" << endl ;

    for (int k = 0 ; k < N ; k++){
        
       t1 = clock();
       
       for (int i = 0 ; i < repeticiones ; i++){
           
          busquedaBinaria(v, 0, tamanyos[k], tamanyos[0]) ;
          
       }
       
       t2 = clock() ;
       
       tiempos[k] = (double(t2 - t1) / CLOCKS_PER_SEC) / repeticiones ;
       
    }
    
    for (int k = 0 ; k < N ; k++)
         cout << "Longitud = " << tamanyos[k] << "; Tiempo = " << tiempos[k] << endl ;
    
    cout << endl ;
    
    
}
