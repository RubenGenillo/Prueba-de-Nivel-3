import random
import math

def leer_numero(ini, fin, mensaje):
    while True:
        try :
            numero = int(input(mensaje))
        except: pass
        
        else:
            if numero >= ini and numero <= fin:
                return numero

def generador():
    numeros = leer_numero(1,20,"¿Cuantos números quieres generar? [1-20]: ")
    modo = leer_numero(1,3,"¿Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal: ")
    lista = []
    for i in range(numeros):
        numero = random.uniform(0,100)
        if modo == 1:
            nAct = math.ceil(numero)
        elif modo == 2:
            nAct = int(numero)
        elif modo == 3:
            nAct = round(numero)
        print(f"Número normal: {numero} Número redondeado: {nAct}")
        lista.append(nAct)
    return lista

