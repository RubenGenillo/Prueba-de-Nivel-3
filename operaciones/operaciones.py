def suma(a,b):
   try:
    return float(a)+float(b)
   except TypeError:
    raise TypeError("Tipo de dato no válido")  
def resta(a,b):
   try:
    return float(a)-float(b)
   except ValueError:
    raise TypeError("Tipo de dato no válido")
def producto(a,b):
   try:
    return float(a)*float(b)
   except TypeError:
    raise TypeError("Tipo de dato no válido")
def division(a,b):
   try: 
    return float(a)/float(b)
   except ZeroDivisionError:
       raise ZeroDivisionError("No es posible dividir entre cero")
   except TypeError:
       raise TypeError("Tipo de dato no válido")