"""
Python posee ademas de los tipos ya vistos, 3 tipos mas complejos, que admiten
una coleccion de datos. Estos tipos son:
Tuplas
Listas
Diccionarios
Estos tres tipos, pueden almacenar colecciones de datos de diversos tipos y se
diferencian por su sintaxis y por la forma en la cual los datos pueden ser
manipulados.
"""
# TUPLAS
# Es una variable que permite almacenar varios datos inmutables y estos datos
# pueden ser de tipos diferentes
mi_tupla = ("cadena de texto",  15, 2.8, "otro dato", True)

print(mi_tupla[1])  # 15
print(mi_tupla[1:4])  # (15, 2.8, "otro dato")
print(mi_tupla[3:])  # ("otro dato", True)
print(mi_tupla[:2])  # ("cadena de texto", 15)
print(mi_tupla[-1])  # True
print(mi_tupla[-2])  # "otro dato"

# LISTAS
# Igual que una tupla con la diferencia que sus elementos si pueden ser
# modificados, se acceden igual que una tupla por su numero de indice
mi_lista = ["cadena de texto", 15, 2.8, "otro dato", True]
mi_lista[2] = 3.8  # el tercer elemento ahora es 3.8

# ademas las lista permiten agregar nuevos elementos
mi_lista.append("nuevo dato")
print(mi_lista[-1])

# DICCIONARIOS
# A diferencia de las tuplas y listas los valores de un diccionario se asocian
# a un nombre de clave.

mi_diccionario = {
    "usuario": "kira",
    "edad": 21,
    "correo": "kira.dev@gmail.com"
}

print(mi_diccionario["edad"])  # 21

# Un diccionario permite eliminar cualquier entrada
del(mi_diccionario["correo"])
print(mi_diccionario)

# Tambien podemos modificar valores
mi_diccionario["edad"] = 31
print(mi_diccionario)

# Y tambien podemos agregar nuevos elementos
mi_diccionario["pais"] = "japon"
print(mi_diccionario)
