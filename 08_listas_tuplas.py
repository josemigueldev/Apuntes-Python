# METODOS DE AGREGADO (listas) ================================================
# Agregar un elemento al final de la lista
nombres_masculinos = ["Alvaro", "Daniel", "Rodrigo"]
nombres_masculinos.append("Jose")

# Agregar varios elementos al final de la lista
nombres_masculinos.extend(["Eduardo", "Miguel"])

# Agregar un elemento en una posicion determinada
nombres_masculinos.insert(1, "Ricky")

# Eliminar el ultimo elemento de la lista
# retorna el elemento eliminado
nombres_masculinos.pop()

# Eliminar un elemento por indice
# retorna el elemento eliminado
nombres_masculinos.pop(1)

# Eliminar un elemento por su valor
nombres_masculinos.remove("Rodrigo")

# METODOS DE ORDEN ============================================================
# Ordenar una lista en reversa
colores = ["rojo", "verde", "azul"]
colores.reverse()

# Ordenar una lista en forma ascendente (alfabetica)
colores.sort()

# Ordenar una lista en forma descendente
colores.sort(reverse=True)

# METODOS DE BUSQUEDA =========================================================
# Contar cantidad de apariciones de elementos
nombres = ["vania", "jose", "gabriela", "jose", "pamela"]
apariciones = nombres.count("jose")  # 2

numeros = [10, 15, 10, 20, 30, 10]
cantidad = numeros.count(10)  # 3

# Obtener numero de indice
print(nombres.index("jose"))  # 1

# Obtener numero de indice a partir de una pocision
print(nombres.index("jose", 2))  # 3

# Preguntar esta en la lista?
print("pamela" in nombres)  # True
print("raquel" in nombres)  # False

# LISTAS Y TUPLAS =============================================================
# Conversion de tuplas a listas y viceversa (list(tupla) tuple(lista))
mi_tupla = (1, 2, 3, 4)
mi_lista = list(mi_tupla)  # [1, 2, 3, 4]

# Concatenacion de colecciones
print([10, 20, 30] + [40, 50, 60])  # [10, 20, 30, 40, 50, 60]
print((1, 2, 3) + (4, 5, 6))  # [1, 2, 3, 4, 5, 6]

# Valor maximo y minimo
print(max([15, 5, 30]))  # 30
print(min([15, 5, 30]))  # 5

# Contar elementos
print(len([10, 15, 20]))  # 3
print(len("hola mundo"))  # 4
