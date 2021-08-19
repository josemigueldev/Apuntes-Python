"""
EXCEPCIONES
===============================================================================
Las excepciones son errores que ocurren durante la ejecucion del programa.
La sintaxis del codigo es correcta pero durante la ejecucion ocurre algo
inesperado.
"""
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    try:
        return float(a) / float(b)
    except ZeroDivisionError:
        return "No se puede dividir entre 0"
    except ValueError as mensaje:
        return f"Ingrese un numero | {mensaje}"
    # finally:
        # print("Esto siempre se ejecutara")


num1 = input("Igrese el primer numero: ")
num2 = input("Igrese el segundo numero: ")

# Probamos con dividir
operacion = input("""Ingrese la operacion a realizar:
1. Sumar
2. Restar
3. Multiplicar
4. Dividir
>> """)

if operacion == "1":
    print(sumar(num1, num2))
elif operacion == "2":
    print(restar(num1, num2))
elif operacion == "3":
    print(multiplicar(num1, num2))
elif operacion == "4":
    print(dividir(num1, num2))
else:
    print("Ingrese una opcion del 1 - 4")

print("Fin del programa.\n")

# Lanzar excepciones personalizadas
import math
# Forma 01
# def raiz_cuadrada(numero):
#     if numero < 0:
#         raise ValueError("El numero no puede ser negativo")
#     else:
#         return math.sqrt(numero)

# numero = int(input("Ingrese un numero: "))

# try:
#     print(raiz_cuadrada(numero))
# except ValueError as ErrorNumeroNegativo:
#     print(ErrorNumeroNegativo)

# Forma 02
class ErrorNumeroNegativo(Exception):
    pass

def raiz_cuadrada(numero):
    if numero < 0:
        raise ErrorNumeroNegativo("El numero no puede ser negativo")
    else:
        return math.sqrt(numero)

numero = int(input("Ingrese un numero: "))

try:
    print(raiz_cuadrada(numero))
except ErrorNumeroNegativo as mensaje:
    print(mensaje)

try:
    print(10 / 0)
# except:
    # print("Ocurrio una excepcion")
except Exception as error:
    # mostrando el nombre de la excepcion
    print("Nombre de excepcion:", type(error).__name__)
    # mostrando el mensaje de la excepcion
    print(error)
