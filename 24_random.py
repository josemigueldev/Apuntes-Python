import random

# NUMEROS ALEATORIOS
# =============================================================================
# Flotante aleatorio entre 0 y 1 (puede generar 0, pero no 1)
print(random.random())

# Flotante aleatorio entre 1 y 5
# puede generar 1 y debido a la forma de redondear de Python,
# puede que genere 5 o no)
print(random.uniform(1, 5))

# Entero aleatorio de 0 a 9, 10 excluido
print(random.randrange(10))

# Entero aleatorio de 1 a 10
print(random.randrange(1, 11))

# Entero aleatorio de 0 a 10, cada dos numeros (multiplos de 2)
print(random.randrange(0, 11, 2))

# Entero aleatorio de 0 a 50, cada cinco numeros (multiplos de 5)
print(random.randrange(0, 51, 5))

# Entero aleatorio de 1 a 5
print(random.randint(1, 5))

# MUESTRAS
# =============================================================================
# Letra aleatoria
print(random.choice("Hola Mundo!"))  # a

# Elemento aleatorio
print(random.choice([1, 2, 3, 4, 5]))  # 5

# Dos elementos aleatorios
print(random.sample([1, 2, 3, 4, 5], 2))  # [1, 4]

# MEZCLAR COLECCIONES
# =============================================================================
lista = [1, 2, 3, 4, 5]
random.shuffle(lista)

print(lista)  # [2, 3, 4, 1, 5]
