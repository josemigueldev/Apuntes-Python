"""
CONJUNTOS - SETS
===============================================================================
- Concepto equivalente al de conjunto en matematica
- Elementos sin orden (no hay indice)
- Los elementos no pueden repetirse
- Elementos heterogeneos, pero solo de tipos inmutables
- No admiten rebanadas (no tienen indice)
- Mutables (pueden agregarse o eliminarse elementos)

Creacion
conjunto_vacio = set()
conjunto_con_elementos = {104, "hola", 0.8, True}
conjunto_desde_string = set("palabra")
conjunto_desde_rango = set(range(5))
conjunto_desde_lista = set([10, 20, 30])
conjunto_desde_tupla = set(("a", "b", "c"))

Iterar
for elemento in conjunto:
    print(elemento)

longitud: len(conjunto)
pertenencia: elemento in conjunto => True | False
agregar elemento:
    conjunto.add(elemento)
    conjunto.update(contenedor) => contenedor = lista | tupla
eliminar elemento:
    conjunto.remove(elemento) => Lanza un error si no encuentra el elemento
    conjunto.discard(elemento) => No lanza un error
vaciar conjunto: conjunto.clear()

iguldad: conjunto1 == conjunto2

inclusion: conjunto1 < conjunto2, conjunto1 > conjunto2
"""
conjunto1 = {10, 20, 30}
conjunto1.add(40)
conjunto2 = {10, 20, 30, 50}
conjunto3 = conjunto1 | conjunto2  # union de conjuntos

print(conjunto1)
print(conjunto1 == conjunto2)  # False
print(conjunto3)

a = {1, 2, 3}
b = {1, 2, 3, 4, 5, 6}
c = {1, 2, 3, 4, 5, 6, 7, 8, 9}

print(a < b)  # a esta incluido en b => True
print(c > b)  # b esta incluido en c => True

d = {10, 50, 60, 80}
e = {10, 70, 90, 50}

print(d - e)  # diferencia: a "d" le quito "e" => {80, 60}
print(e - d)  # diferencia: a "e" le quito "d" => {90, 70}
print(d ^ e)  # diferencia simetrica => {70, 80, 90, 60}
"""
La diferencia simetrica son la partes no comunes entre conjuntos, mejor dicho
todo menos la interseccion
"""

# Interseccion de Conjuntos
print(d & e)  # {10, 50}
