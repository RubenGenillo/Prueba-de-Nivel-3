from pila import Pila

class pedido:
    def __init__(self, solicitante, muliverso, descripción):
        self.solicitante = solicitante
        self.multiverso = muliverso
        self.descripción = descripción
        if (self.solicitante == "Gran Conquistador" or self.multiverso == 616 or ("El que permanece" in self.descripción)):
            self.prioridad = 3
        elif (self.solicitante == "Khan que todo lo sabe" or self.multiverso == 838 or ("Carnicero de Dioses" in self.descripción)):
            self.prioridad = 2
        else:
            self.prioridad = 1

class gestorKhan():
    def __init__(self):
        self.vector = []
        self.tamanio = 0
        self.bitacora = Pila()

    def agregar(heap, soliciante, muliverso, descripción):
        heap.atender()
        dato = pedido(soliciante, muliverso, descripción)
        heap.vector.append(dato)
        heap.flotar(heap.tamanio)
        heap.tamanio += 1

    def flotar(heap, indice):
        while(indice > 0):
            if(heap.vector[indice].prioridad > heap.vector[(indice - 1) // 2].prioridad):
                aux = heap.vector[indice]
                heap.vector.pop(indice)
                heap.vector.insert((indice - 1) // 2, aux)
                indice = (indice - 1) // 2
            else:
                break

    def quitar(heap, dato):
        valor = heap.vector[dato]
        heap.vector[dato] = heap.vector[-1]
        heap.vector.pop()
        if heap.tamanio > 1:
            gestorKhan.hundir(heap, dato)
        return valor
    
    def hundir(heap, indice):
        hijo_izq = (indice * 2) + 1
        control = True
        while(control and hijo_izq < heap.tamanio-1):
            hijo_der = hijo_izq + 1
            aux = hijo_izq
            if(hijo_der < heap.tamanio-1):
                if(heap.vector[hijo_der].prioridad > heap.vector[hijo_izq].prioridad):
                    aux = hijo_der
            if(heap.vector[indice].prioridad < heap.vector[aux].prioridad):
                naux = heap.vector[indice]
                heap.vector[indice] = heap.vector[aux]
                heap.vector[aux] = naux                
                indice = aux
                hijo_izq = (indice * 2) + 1
            else:
                control = False

    def almacenar(heap):
        heap.bitacora.apilar(heap.quitar(0))

    def atender(heap):
        if not heap.bitacora.estaVacia():
            heap.bitacora.desapilar()