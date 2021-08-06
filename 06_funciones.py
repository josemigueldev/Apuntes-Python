"""
FUNCIONES
===============================================================================
Una funcion es una forma de agrupar expresiones y algoritmos de forma tal que
estos queden contenidos dentro de una capsula que solo puede ejecutarse cuando
el programador la invoque.
Una vez que una funcion es definida. puede ser invocada tantas veces como sea
necesario.
"""
# Parametros por omision (valores por defecto)
def calcular_neto(bruto, alicuota=21):
    iva = bruto * float(alicuota) / 100
    neto = bruto + iva
    return neto

print(calcular_neto(100))  # 121.0
print(calcular_neto(100, 10.5))  # 110.5

# Claves como argumentos
def area_triangulo(base, altura):
    area = base * altura / 2
    return area

print(area_triangulo(altura=4, base=8))

# Parametros arbitrarios (deben ir despues de los parametros fijos)
def imprimir_colores(*colores):
    for color in colores:
        print(color)

imprimir_colores("rojo", "verde", "azul")

def mostrar_usuario(**usuario):
    for clave in usuario:
        print(f"{clave}: {usuario[clave]}")

mostrar_usuario(nombre="miguel", edad=30, correo="miguel@dev.com")

# Desempaquetado de parametros
colores = ["magenta", "cyan", "indigo"]
imprimir_colores(*colores)

usuario1 = {"nombre": "vania", "edad": 21, "correo": "vania@design.com"}
usuario2 = dict(nombre="raquel", edad=18, correo="raquel@uni.com")
mostrar_usuario(**usuario1)
mostrar_usuario(**usuario2)

# Llamada recursiva (Una funcion que se llama asi misma)
def obtener_nombre():
    nombre = input("Ingresa tu nombre: ")
    if not nombre:
        obtener_nombre()
    else:
        print("Hola", nombre)

obtener_nombre()
