"""
DECORADORES
===============================================================================
Son funciones que a su vez añaden funcionalidades a otras funciones.
Estructura de un decorador:
- 3 funciones(A, B, C) donde A recibe como parámetro B para devolver C
- Un decorador devuelve una funcion

def funcion_decorador(funcion):
    def funcion_interna():
        # codigo funcion interna
    return funcion_interna
"""
def funcion_decoradora(funcion):
    def funcion_interna(*args, **kwargs):
        print("Comienzo")
        funcion(*args, **kwargs)
        print("Final")
    return funcion_interna

@funcion_decoradora
def suma(a, b):
    print(a + b)

@funcion_decoradora
def resta(a, b):
    print(a - b)

@funcion_decoradora
def potencia(base, exponente):
    print(pow(base, exponente))

suma(10, 5)
resta(15, 30)
potencia(exponente=5, base=2)
