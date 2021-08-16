# Programacion Funcional
# =============================================================================
from functools import reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cuadrados = list(map(lambda num: num * num, numeros))
pares = list(filter(lambda num: num % 2 == 0, numeros))
suma = reduce(lambda x, y: x + y, numeros)
multiplicacion = reduce(lambda x, y: x * y, numeros)


print(cuadrados)
print(pares)
print(suma)
print(multiplicacion)
