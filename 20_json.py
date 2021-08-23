import json

# convertimos un string_json en un diccionario
json_str = '{"nombre": "miguel", "edad": 21, "pais": "perú"}'

diccionario = json.loads(json_str)
print(diccionario)
print(type(diccionario))  # <class 'dict'>

# convertimos un diccionario en un string_json
datos = {
    "nombre": "vania",
    "edad": 22,
    "pais": "perú",
    "cursos": ["python", "ruby", "javascript"]
}

json_datos = json.dumps(datos)
print(json_datos)
print(type(json_datos))  # <class 'str'>

"""
Equivalencias entre Python y Json
=================================
dict  => Object
list  => Array
tuple => Array
str   => String
int   => Number
float => Number
True  => true
False => false
None  => ull
"""

# formatear salida del string_json
usuario = {
    "nombre": "kira",
    "edad": 19,
    "email": "kira19@gmail.com",
    "lenguajes": ["python", "rust", "go"]
}

usuario_str = json.dumps(usuario, indent=4, separators=(", ", ": "), sort_keys=True)
print(usuario_str)

# Encodificar y Decodificar JSON
# convertimos diccionario en un json_string
encodificar = json.JSONEncoder().encode({"lenguajes": ["haskell", "elixir"]})
print(type(encodificar))  # <class 'str'>

# convertimos json_string en un diccionario
decodificar = json.JSONDecoder().decode(encodificar)
print(type(decodificar))  # <class 'dict'>

# Convertir un objeto en un string_json
# =====================================
class Curso:
    def __init__(self, codigo, nombre, creditos):
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos


mi_curso = Curso("9717", "lenguaje", 5)
objeto_json_string = json.dumps(mi_curso.__dict__)
print(objeto_json_string)
print(type(objeto_json_string))  # <class 'str'>

# convertimos el objeto_json_string en un diccionario
objeto_json_diccionario = json.loads(objeto_json_string)
print(objeto_json_diccionario)
print(type(objeto_json_diccionario))  # <class 'dict'>
