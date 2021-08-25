"""
Cortocircuito en Python
===============================================================================
OR
Cuando el valor de la izquierda siempre pueda validar a True es el que se
cargara por defecto de lo contrario se cargara el otro valor.

AND
Cuando el valor de la izquierda siempre pueda validar a False es el que se
cargara por defecto de lo contrario se cargara el otro valor.

Valores Falsy
None, 0, "", [], (), {}, Todos los demas valores son considerados Truthy
"""

print("" or 20)  # 20
print("hola" or 20)  # hola
print(False or True)  # True
print(False or -1)  # -1
print(0 or 10)  # 10

print("" and 20)  # ""
print("hola" and 20)  # 20
print(False and True)  # False
print([] and -1)  # []
print(0 and 10)  # 0
