# MANEJO DE ARCHIVOS
"""
io => manejo de entrada y salida de flujos de datos
lectura r
escritura w
agregado a
"""
from io import open

# Escribir archivo - si no existe lo crea
"""
archivo = open("archivo.txt", "w")
texto = "Miercoles\nEstupendo día para aprender Python!"
archivo.write(texto)  # escribimos el texto en el archivo
archivo.close()
"""

# Leer archivo
"""
archivo = open("archivo.txt", "r")
texto = archivo.read()
archivo.close()
print(texto)
"""

# Leer archivo linea por linea
"""
archivo = open("archivo.txt", "r")
lineas = archivo.readlines()
archivo.close()

for linea in lineas:
      print(linea.rstrip("\n"))  # eliminamos saltos de linea con rstrip

# nota: Tambien podemos leer una sola linea con readline()
"""

# Agregar texto al final
"""
archivo = open("archivo.txt", "a")
nuevo_texto = "\nsigue adelante!"
archivo.write(nuevo_texto)
archivo.close()
"""

# Mover el puntero de la lectura
"""
archivo = open("archivo.txt", "r")
archivo.seek(10)  # movemos el puntero 10 posiciones
print(archivo.read())  # lee a partir de la posicion 10
archivo.close()
"""

# Lectura y Escritura
archivo = open("archivo.txt", "r+")
cursor = len("".join(archivo.readlines()))
archivo.seek(cursor)  # ubicamos el cursor al final
archivo.write("\nNo te detengas!")
archivo.close()
