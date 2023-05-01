import random
from pila import Pila

def generarCartas(pila, x,y):
    if x <= y:
        pila.apilar(str(x)+"E")
        pila.apilar(str(x)+"B")
        pila.apilar(str(x)+"C")
        pila.apilar(str(x)+"O")
        generarCartas(pila, x+1, y)    

def cartasAleatorias(pila):
    pilaAux1 = Pila()
    pilaAux2 = Pila()
    generarCartas(pilaAux1, 1, 12)
    for i in reversed(range(1,48+1)):        
        for j in range(random.randint(1,i)):            
            pilaAux2.apilar(pilaAux1.desapilar())
        pila.apilar(pilaAux2.desapilar())
        while(not pilaAux2.estaVacia()):
            pilaAux1.apilar(pilaAux2.desapilar())

def separar(pila):
    espadas = Pila()
    bastos = Pila()
    copas = Pila()
    oros = Pila()
    while(not pila.estaVacia()):
        carta = pila.desapilar()
        if carta[-1] == "E":
            espadas.apilar(carta)
        elif carta[-1] == "B":
            bastos.apilar(carta)
        elif carta[-1] == "C":
            copas.apilar(carta)
        else:
            oros.apilar(carta)
    return espadas, bastos, copas, oros

def ordenar(pila):
    pilaAux = Pila()
    pilaFinal = Pila()
    while(not pila.estaVacia()):
        carta = str(pila.mostrarTamaño())
        while str(pila.mostrarTope())[:-1] != carta:
            pilaAux.apilar(pila.desapilar())
        pilaFinal.apilar(pila.desapilar())
        while(not pilaAux.estaVacia()):
            pila.apilar(pilaAux.desapilar())
    return pilaFinal

def main():
    pilaCartas = Pila()
    cartasAleatorias(pilaCartas)
    pilaCartas.barrido()
    espadas, bastos, copas, oros = separar(pilaCartas)   
    espadasOrdenadas = ordenar(espadas)
    espadasOrdenadas.barrido()

if __name__ == "__main__":
    main()