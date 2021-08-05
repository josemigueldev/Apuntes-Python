"""
ESTRUCTURAS DE CONTROL DE FLUJO
===============================================================================
Una estructura de control es un bloque de codigo fuente que permite agrupar
instrucciones de forma controlada.

Estructuras de control condicionales (if, elif, else)
=====================================================
Controlan el flujo de los datos a partir de condiciones.

Estructuras de control iterativas (while, for)
==============================================
Controlan el flujo de los datos, ejecutando una misma accion de forma repetida.

Para describir la evaluacion a realizar sobre una condicion, se utilizar opera-
dores relacionales o de comparacion:
==, !=, <, >, <=, >=

Para evaluar mas de una condicion simultaneamente, se usan operadores logicos:
and(y) devuelve True si los dos elementos evaluan a True
or(o) devuelve True si uno de los elementos evalua a True
^ (o excluyente) devuelve True si uno de los elementos evalua distinto al otro
"""
gasto = 150

if gasto <= 100:
    print("Pagar con efectivo")
elif gasto > 100 and gasto < 300:
    print("Pagar con debito")
else:
    print("Pagar con cretido")

year = 2015

while year <= 2021:
    print("Informes de", year)
    year += 1

while True:
    numero = int(input("Ingrese un numero mayor que 100: "))
    if numero > 100:
        print("El numero es:", numero)
        break

colores = ["rojo", "verde", "azul"]

for color in colores:
    print(color)

# imprimir informes con for
for year in range(2015, 2022):
    print("Informes de", year)
