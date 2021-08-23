import math

numero = 3.5789
print(round(numero))  # 4 redondeo total
print(round(numero, 1))  # 3.6 redondeo a un decimal

print(math.ceil(numero))  # 4 redondeo hacia arriba
print(math.floor(numero))  # 3 redondeo hacia abajo

print(math.trunc(numero))  # 3 retorna la parte entera

numeros = [1, 2, 3, 4, 5]
print(math.fsum(numeros))  # 15.0 suma un iterable

print(math.fabs(-7))  # 7.0 valor absoluto

print(math.fmod(17, 6))  # 5.0 residuo/modulo

print(math.exp(2))  # 7.38905609893065 epsilon elevado al cuadrado

print(math.pi)  # 3.14159...

print(math.pow(5, 2))  # 25.0 cinco elevado al cuadrado

print(math.sqrt(16))  # 4.0 raiz cuadrada de 16

# convertir 45 grados sexagesimales a radianes
print(math.radians(45))  # 0.7853981633974483

# calcular la hipotenusa de los catetos de 8 y 9
print(math.hypot(8, 9))  # 12.041594578792296
