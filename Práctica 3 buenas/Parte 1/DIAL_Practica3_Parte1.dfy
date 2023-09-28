/*


    PRÁCTICA 3 (PARTE 1): DISEÑO DE ALGORITMOS RECURSIVOS EN DAFNY

    ASIGNATURA: DISEÑO DE ALGORITMOS
    CURSO:      2022-2023
    SUBGRUPO:   U1 / U2

    APELLIDOS: González Montero
    NOMBRE:    Sergio


*/



/*


	EJERCICIO 5.3: SUMA DE UN VECTOR

	Considera la siguiente especificación de un algoritmo para sumar todos
	los elementos de un vector de enteros dado:


	     { P : N >= 0 }

	     fun suma_vector(v[0..N) de ent) dev s : int 

	     { Q : s = ( Sumatorio i : 0 <= i < N : v[i] ) }	


	a) Diseña un algoritmo recursivo lineal no final planteando una INMERSIÓN 
	   NO FINAL.

	b) Diseña un algoritmo recursivo lineal final planteando una INMERSIÓN 
	   FINAL.


*/



// FUNCIÓN AUXILIAR PARA ESPECIFICAR LA SUMA DE UN VECTOR



function sum_vector(v : array?<int>, n : nat) : int

	requires  v != null && 0 <= n <= v.Length

	decreases n

	reads v

{

	if n == 0 then 0
	else sum_vector(v, n - 1) + v[n - 1]

}



// INMERSIÓN NO FINAL



method suma_vector1(v : array?<int>) returns (s : int)     // O(v.Length)

	requires v != null
	ensures  s == sum_vector(v, v.Length)

{

	s := gsuma_vector(v, v.Length) ;

}



method gsuma_vector(v : array?<int>, n : nat) returns (s : int)     // O(n)

	requires  v != null && 0 <= n <= v.Length
	ensures   s == sum_vector(v, n)

	decreases n

{

	if n == 0 {

		s := 0 ;

	} else {

		var s1 : int ;

		s1 := gsuma_vector(v, n - 1) ;

		s := s1 + v[n - 1] ;

	}

}



// INMERSIÓN FINAL



method suma_vector2(v : array?<int>) returns (s : int)     // O(v.Length)

	requires v != null
	ensures  s == sum_vector(v, v.Length)

{

	s := gfsuma_vector(v, 0, 0) ;

}



method gfsuma_vector(v : array?<int>, n : nat, w : int) returns (s : int)     // O(N - n)

	requires  v != null && 0 <= n <= v.Length && w == sum_vector(v, n)
	ensures   s == sum_vector(v, v.Length)

	decreases v.Length - n

{

	if n == v.Length {

		s := w ;

	} else {

		s := gfsuma_vector(v, n + 1, w + v[n]) ;

	}

}





/*



	EJERCICIO 5.7: PRODUCTO ESCALAR DE DOS VECTORES

	Diseña algoritmos recursivos para calcular el producto escalar de dos 
	vectores de enteros dados de igual longitud, planteando, primero, una 
	inmersión no final, y después, una inmersión final.



*/

// FUNCIÓN AUXILIAR PARA CALCULAR EL PRODUCTO ESCALAR DE VECTORES DE IGUAL LONGITUD
function prod_escalar(v : array?<int>, w : array? <int>, n : nat) : int

    requires v != null && 0 <= n <= v.Length
    requires w != null && 0 <= n <= w.Length
    requires v.Length == w.Length

    decreases v.Length - n

    reads v
    reads w
//prod_escalar(v, w, n) = (SUM i : n <= i <= N : v[i] * w[i])
//                     prod_escalar(v, w, n+1) + v[n] * w[n] si n < N
//                     prod_escalar(v, w, n) = 0 si n = N
{
    if n == v.Length then 0
    else prod_escalar(v, w, n+1) + (v[n] * w[n])
}

// INMERSIÓN NO FINAL
method producto_escalar( v : array?<int>, w : array?<int>) returns (s : int) // {O(v.Length)}

    requires v != null
    requires w != null
    requires v.Length == w.Length
    ensures s == prod_escalar(v, w, 0)

{
    s := gproducto_escalar(v, w, 0) ; 
}

// Función inmersora
method gproducto_escalar( v : array?<int>, w : array?<int>, n : nat) returns (s : int) //{O(v.Length - n)}

    requires v != null && 0 <= n <= v.Length
    requires w != null && 0 <= n <= w.Length
    requires v.Length == w.Length
    ensures s == prod_escalar(v, w, n)

    decreases v.Length - n

    {
        if n == v.Length {
                    s := 0 ;
        } else {
            var s1: int ;
            s1 := gproducto_escalar(v, w, n+1) ;
            s := s1 + (v[n] * w[n]) ;
        }

    }

// INMERSIÓN FINAL
method producto_escalar2( v : array?<int>, w : array?<int>) returns (s : int) // {O(v.Length)}

    requires v != null
    requires w != null
    requires v.Length == w.Length
    ensures s == prod_escalar(v, w, 0)

{
    s := gfproducto_escalar(v, w, v.Length, 0) ;
}

//Añadimos un acumulador
method gfproducto_escalar( v : array?<int>, w : array?<int>, n : nat, ac : int) returns (s : int) // {O(n)}

    requires v != null && 0 <= n <= v.Length
    requires w != null && 0 <= n <= w.Length
    requires v.Length == w.Length
    requires ac == prod_escalar(v, w, n)
    ensures s == prod_escalar(v, w, 0)

    decreases n

{
    if n == 0 {
        s := ac ;
    } else {
        s := gfproducto_escalar(v, w, n-1, ac + (v[n-1] * w[n-1])) ;
    }
}


// PROGRAMA PRINCIPAL PARA PROBAR LOS ALGORITMOS RECURSIVOS DISEÑADOS

method Main()
{

	var v := new int[] [-1, 2, 5, -5, 8] ;
	var w := new int[] [ 1, 0, 5,  5, 8] ;
	var s1 := suma_vector1(v) ;
	var s2 := suma_vector1(w) ;

	print("\n") ;
	print("La suma del primer vector es: ") ;
	print(s1) ;
	print("\n") ;
	print("La suma del segundo vector es: ") ;
	print(s2) ;
	print("\n\n") ;
	
}

method Main1()
{
    var v := new int[] [-1, 2, 5, -5, 8] ;
    var w := new int[] [ 1, 0, 5,  5, 8] ;
    var s := producto_escalar(v,w) ;
    
    print("El producto escalar de los dos vectores es: ") ;
    print (s) ;
    print("\n") ;
}