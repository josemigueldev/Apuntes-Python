# Listas por comprension (List Comprehension)
# =============================================================================
# Crear una lista del 1 al 10
lista = [numero for numero in range(1, 11)]
print(lista)

# Crear una lista de numero pares del 1 al 10
pares = [numero for numero in range(1, 11) if numero % 2 == 0]
print(pares)

# Tambien podemos crear diccionarios por comprension
palabra = "dicci"
cantidad_letras = {letra: palabra.count(letra) for letra in palabra}
print(cantidad_letras)  # {'d': 1, 'i': 2, 'c': 2}
