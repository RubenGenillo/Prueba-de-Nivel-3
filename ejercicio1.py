from cola import Cola

class nodoArbol():
    def __init__(self, info):
        self.info = info
        self.izq = None
        self.der = None
    
    def insertar_nodo(raiz, dato, pos):
        if pos:
            if raiz.izq is None:
             raiz.izq = nodoArbol(dato)
            else:
                nodoArbol.insertar_nodo(raiz.der, dato, pos)
        else:
            if raiz.der is None:
              raiz.der = nodoArbol(dato)
            else:
                nodoArbol.insertar_nodo(raiz.der, dato, pos)

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

    def determinar_superheroe(self, pregunta):
        if self.izq is not None:
            if pregunta == self.info:
                return self.izq.info
            else:
                return nodoArbol.determinar_superheroe(self.der, pregunta)


def main():
    decision = nodoArbol("Para misiones intergalácticas en equipo")
    decision.insertar_nodo("Khan", True)
    decision.insertar_nodo("Para misiones de recuperación donde sea necesario no ser detectado", False)
    decision.insertar_nodo("AntMan", True)
    decision.insertar_nodo("Para misiones de destrucción", False)
    decision.insertar_nodo("Hulk", True)
    decision.insertar_nodo("Para comandar misiones de defensa y de recuperación", False)
    decision.insertar_nodo("Capitan America", True)
    decision.insertar_nodo("Muy poderosa y que viaje por distintas galaxias", False)
    decision.insertar_nodo("Capitana Marvel", True)
    decision.insertar_nodo("Muy hábil y útil para varias misiones", False)
    decision.insertar_nodo("Khan", True)
    decision.insertar_nodo("Para misiones de recuperación donde requiera infiltrarse con personas del lugar", False)
    decision.insertar_nodo("The Winter Soldier", True)
    decision.insertar_nodo("Para planear misiones de defensa", False)
    decision.insertar_nodo("Iron Man", True)
    decision.insertar_nodo("Cuando se requiere elegir cuál será la próxima acción para tomar y moverse rápidamente de un lugar a otro", False)
    decision.insertar_nodo("Nick Fury", True)
    decision.insertar_nodo("Para destruir ejércitos completos", False)
    decision.insertar_nodo("Thor", True)

    
if __name__ == "__main__":
    main()