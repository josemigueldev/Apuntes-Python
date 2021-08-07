"""
MANIPULACION DE CADENAS
===============================================================================
"""
# Inyeccion de variables
saludo1 = "Hola, {}!"
print(saludo1.format("jose"))

saludo2 = "Hola, {nombre} {apellido}"
print(saludo2.format(apellido="ruiz", nombre="luis"))

# Metodos de formato
print("bienvenidos a todos".capitalize())  # Bienvenidos a todos
print("bienvenidos a todos".upper())  # BIENVENIDOS A TODOS
print("BIENVENIDOS A TODOS".lower())  # bienvenidos a todos
print("hOlA".swapcase())  # HoLa
print("titulo de un blog".title())  # Titulo De Un Blog

# Centrar un texto (retorna una copia)
print("Bienvenido".center(30, "="))  # ==========Bienvenido==========

# Alinear texto a la izquierda (retorna una copia)
print("Bienvenido".ljust(30, "="))  # Bienvenido====================

# Alinear texto a la derecha (retorna una copia)
print("Bienvenido".rjust(30, "="))  # ====================Bienvenido

# Rellenar un texto anteponiendo ceros (retorna una copia)
numero_factura = str(1575)
print(numero_factura.zfill(12))  # 000000001575

# METODOS DE BUSQUEDA
# Contar cantidad de apariciones de un fragmento de texto (retorna un entero)
# retorna 0 si no encuentra apariciones
print("Bienvenido a mi aplicacion".count("a"))  # 3

# Buscar un fragmento de texto dentro de una cadena
# retorna un entero representando la posicion donde inicia la subcadena
# si no la encuentra retorna -1
print("Bienvenido a mi aplicacion".find("mi"))  # 13

# METODOS DE VALIDACION
# Saber si una cadena comienza con un fragmento de texto determinado
# retorna True o false
print("Bienvenido a mi aplicacion".startswith("Bienvenido"))  # True
print("Bienvenido a mi aplicacion".startswith("aplicacion", 16))  # True

# Saber si una cadena termina con un fragmento de texto determinado
# retorna True o false
print("Bienvenido a mi aplicacion".endswith("aplicacion"))  # True

# Saber si una cadena es alfanumerica (solo letras de alfabeto o numeros)
# retorna True o False
print("pepegrillo".isalnum())  # True
print("pepegrillo 75".isalnum())  # False
print("pepegrillo75".isalnum())  # True

# Saber si una cadena es alfabetica
# retorna True o False
print("pepegrillo".isalpha())  # True
print("pepegrillo75".isalpha())  # False

# Saber si una cadena es numerica
# retorna True o False
print("1075".isdigit())  # True
print("alt1075".isdigit())  # False
print("10.75".isdigit())  # False

# Saber si una cadena contiene solo minusculas
# retorna True o False
print("hola mundo".islower())  # True
print("Hola Mundo".islower())  # False

# Saber si una cadena contiene solo mayusculas
# retorna True o False
print("HOLA MUNDO".isupper())  # True
print("Hola Mundo".isupper())  # False

# Saber si una cadena solo contiene espacios en blanco
# retorna True o False
print("   ".isspace())  # True
print(" hola  ".isspace())  # False

# Saber si una cadena tiene formato tipo titulo
# retorna True o False
print("Esto Es Un Titulo".istitle())  # True
print("Esto es un Titulo".istitle())  # False

# METODOS DE SUSTITUCION
# Dar formato a una cadena
# retorna la cadena formateada
resultado = "Importe bruto: ${0} + IVA: ${1} = Importe neto: {2}"
print(resultado.format(100, 21, 121))

resultado2 = "Importe bruto: ${bruto} + IVA: ${iva} = Importe neto: {neto}"
print(resultado2.format(bruto=100, iva=21, neto=121))
print(resultado2.format(
    bruto=100,
    iva=100 * 21 / 100,
    neto=100 * 21 / 100 + 100
))

# Reemplazar texto en una cadena
# retorna la cadena reemplazada
buscar = "nombre apellido"
reemplazar = "Juan Perez"
print("Estimado Sr. nombre apellido:".replace(buscar, reemplazar))

# Eliminar caracteres a la izquierda y derecha de una cadena
# retorna la cadena sustituida
pagina_web = "   www.python.org   "
print(pagina_web.strip())  # "www.python.org"
print(pagina_web.strip(" "))  # "www.python.org"
print("zzzwww.python.orgzzz".strip("z"))  # "www.python.org"

# Eliminar caracteres a la izquierda de una cadena
print("www.python.org".lstrip("w"))  # ".python.org"

# Eliminar caracteres a la derecha de una cadena
print("www.python.org".rstrip(".org"))  # "www.python"

# METODOS DE UNION Y DIVISION
# Unir una cadena de forma iterativa
# retorna la cadena unida con el iterable
rellenos = ("N° 0000-0", "-0000 (ID: ", ")")
numero = "275"
numero_factura1 = numero.join(rellenos)
print(numero_factura1)  # N° 0000-0275-0000 (ID: 275)

# Partir una cadena en tres partes, utilizando un separador
# retorna una tupla de tres elementos donde el primero es el contenido previo
# al separador, el segundo, el separador mismo y el tercero, el contenido de la
# cadena posterior al separador
url = "https://www.google.com"
tupla = url.partition("www.")
print(tupla)
protocolo, separador, dominio = tupla
print("Protocolo: {0}\nDominio: {1}".format(protocolo, dominio))

# Partir una cadena en varias partes, utilizando un separador
# retorna una lista con todos los elementos econtrados al dividir la cadena
# por un separador
keywords = "python, guia, curso".split(", ")
print(keywords)  # ["python", "guia", "curso"]

# Partir una cadena en lineas
# retorna una lista donde cada elemento es una fraccion de la cadena dividida
# en lineas
texto1 = """Linea 1
Linea 2
Linea 3
Linea 4
"""
print(texto1.splitlines())  # ["Linea1", "Linea2", "Linea3", "Linea4"]

texto2 = "Linea1\nLinea2\nLinea3"
print(texto2.splitlines())  # ["Linea1", "Linea2", "Linea3"]
