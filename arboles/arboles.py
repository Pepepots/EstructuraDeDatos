from NodosArbol import NodoArbolBinario, NodoArbolTernario

arbol1 = NodoArbolBinario('R')
arbol1.left = NodoArbolBinario('C')
arbol1.rigth = NodoArbolBinario('H')

arbol2 = NodoArbolTernario(4)
arbol2.left = NodoArbolTernario(3)
arbol2.rigth = NodoArbolTernario(5)
arbol2.left.left = NodoArbolTernario(5)
arbol2.left.center = NodoArbolTernario(5)
arbol2.left.rigth = NodoArbolTernario(2)
arbol2.left.left.left = NodoArbolTernario(2)

arbol3 = NodoArbolBinario('Santi')
arbol3.rigth = NodoArbolBinario('Jesus')
arbol3.rigth.left = NodoArbolBinario('Pedro')
arbol3.rigth.left.rigth = NodoArbolBinario('Pedro')
