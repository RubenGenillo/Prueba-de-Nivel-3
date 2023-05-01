import random

from cola import Cola

class nodoArbol():
    def __init__(self, info):
        self.info = info
        self.izq = None
        self.der = None
        self.altura = 0
 
    def insertar_nodo(raiz, dato):
        if raiz is None:
            raiz = nodoArbol(dato)
        elif dato < raiz.info:
            raiz.izq = nodoArbol.insertar_nodo(raiz.izq, dato)
        else:
            raiz.der = nodoArbol.insertar_nodo(raiz.der, dato)
        nodoArbol.actualizaraltura(raiz)
        return raiz
    
    def eliminar_nodo(raiz, clave):
        x = None
        if(raiz is not None):
            if(clave < raiz.info):
                raiz.izq, x = nodoArbol.eliminar_nodo(raiz.izq, clave)
            elif(clave > raiz.info):
                raiz.der, x = nodoArbol.eliminar_nodo(raiz.der, clave)
            else:
                x = raiz.info
                if(raiz.izq is None):
                    raiz = raiz.der
                elif(raiz.der is None):
                    raiz = raiz.izq
                else:
                    raiz.izq, aux = nodoArbol.remplazar(raiz.izq)
                    raiz.info = aux.info
        nodoArbol.actualizaraltura(raiz)
        return raiz, x
    
    def arbol_vacio(raiz):
        return raiz == None

    def remplazar(raiz):
        aux = None
        if(raiz.der is None):
            aux = raiz
            raiz = raiz.izq
        else:
            raiz.der, aux = nodoArbol.remplazar(raiz.der)
        return raiz, aux    

    def por_nivel(raiz):
        pendientes = Cola()
        pendientes.añadir(raiz)
        while not pendientes.cola_vacia():
            nodo = pendientes.atender()
            print(nodo.info)
            if nodo.izq is not None:
                pendientes.añadir(nodo.izq)
            if nodo.der is not None:
                pendientes.añadir(nodo.der)

    def buscar(raiz, clave):
        pos = None
        if (raiz.info is not None):
            if(raiz.info == clave):
                pos = raiz
            elif(clave < raiz.info):
                pos = nodoArbol.buscar(raiz.izq, clave)
            else:
                pos = nodoArbol.buscar(raiz.der, clave)
        return pos
    
    def inorden(raiz):
        if raiz is not None:
            nodoArbol.inorden(raiz.izq)
            print(raiz.info)
            nodoArbol.inorden(raiz.der)

    def preorden(raiz):
        if raiz is not None:
            print(raiz.info)
            nodoArbol.preorden(raiz.izq)
            nodoArbol.preorden(raiz.der)

    def postorden(raiz):
        if raiz is not None:
            nodoArbol.postorden(raiz.der)
            print(raiz.info)
            nodoArbol.postorden(raiz.izq)

    def altura(raiz):
        if(raiz is None):
            return -1
        else:
            return raiz.altura

    def actualizaraltura(raiz):
        if raiz is not None:
            alt_izq = nodoArbol.altura(raiz.izq)
            alt_der = nodoArbol.altura(raiz.der)
            raiz.altura = (alt_izq if alt_izq > alt_der else alt_der) + 1
 
    def ocurrencia(raiz, clave):
        cant = 0
        if raiz is not None:
            if(raiz.info == clave):
                cant += 1
            cant += nodoArbol.ocurrencia(raiz.izq, clave)
            cant += nodoArbol.ocurrencia(raiz.der, clave)
        return cant
    
    def par_e_impar(raiz, par):
        cant = 0
        if raiz is not None:
            if par:
                if raiz.info % 2 == 0:
                    cant += 1
            else:
                if raiz.info % 2 != 0:
                    cant += 1
            cant += nodoArbol.par_e_impar(raiz.izq, par)
            cant += nodoArbol.par_e_impar(raiz.der, par)
        return cant



def algoritmo():
    arbol = nodoArbol(random.randint(0, 100))
    for i in range(1000):
        arbol.insertar_nodo(random.randint(0, 100))
    arbol.preorden()
    arbol.inorden()
    arbol.postorden()
    arbol.por_nivel()
    print(arbol.buscar(random.randint(0, 100)))
    arbol.eliminar_nodo(random.randint(0, 100))
    arbol.eliminar_nodo(random.randint(0, 100))
    arbol.eliminar_nodo(random.randint(0, 100))
    print(arbol.izq.altura)
    print(arbol.der.altura)
    print(arbol.ocurrencia(random.randint(0, 100)))
    print(arbol.par_e_impar(True))
    print(arbol.par_e_impar(False))


if __name__ == "__main__":
    algoritmo()