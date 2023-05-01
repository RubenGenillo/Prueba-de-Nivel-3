class Nodo(object):
    info,sig = None, None

class Cola(object):
    def __init__(self):
        self.tamanio = 0
        self.primero, self.ultimo = None, None

    def añadir(cola, info):
        nuevo = Nodo()
        nuevo.info = info
        if cola.primero is  None:
         cola.primero = nuevo        
        else:
         cola.ultimo.sig = nuevo
        cola.ultimo = nuevo
        cola.tamanio += 1

    def atender(cola):
        #que pasa si es none y no tiene info??
        dato = cola.primero.info
        cola.primero = cola.primero.sig
        if cola.primero is None:
            cola.ultimo = None
        cola.tamanio -= 1
        return dato

    def cola_vacia(cola):
        return cola.primero is None

    def mostrar_Primero(cola):
       return cola.primero.info
    
    def colaTamanio(cola):
        return cola.tamanio
    
    def mover_al_final(cola):
        dato = cola.atender()
        cola.añadir(dato)
        return dato

    def Barrido(cola):
        veces = cola.tamanio
        for i in range(veces):
           print(cola.mover_al_final())

