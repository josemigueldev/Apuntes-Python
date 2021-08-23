"""
Enumeradores
============
Un Enum o una Enumeracion es un conjunto de nombres simbolicos los cuales se
encuentran vinculados a un valor, ese valor sera unico y constante.
En pocas palabras un Enum es una lista de constantes
Por lo general contienen numeros pero tambien pueden contener otros tipos
"""
import enum

class Color(enum.Enum):
    rojo = "#FF0000"
    verde = "#008000"
    azul = "#0000FF"


print(Color.rojo.name)  # rojo
print(Color.rojo.value)  # #FF0000

print(Color["rojo"].name)  # rojo
print(Color["rojo"].value)  #FF0000

print(Color.rojo is Color["rojo"])  # True

# Iterar un Enum
for color in Color:
    print(color.name, "=>", color.value)
    """
    rojo => #FF0000
    verde => #008000
    azul => #0000FF
    """
