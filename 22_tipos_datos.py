# Manejo de Tipos de Datos
# =============================================================================
# Obtener el tipo de dato de una variable
print(type("cadena"))  # <class 'str'>
print(type(10.5))  # <class 'float'>

# Comprobar si un dato es una instancia de ...
print(isinstance("cadena", str))  # True
print(isinstance(10.5, int))  # False

# Obtener el nombre del tipo de dato de una variable
print(type("cadena").__name__)  # str
print(type(10.5).__name__)  # float

# Obtener el tipo y el nombre con __class__
class Persona():
    def __init__(self, nombre):
        self.nombre = nombre


miguel = Persona("miguel")
print(miguel.__class__)  # <class '__main__.Persona'>
print(miguel.__class__.__name__)  # Persona

print("cadena".__class__)  # <class 'str'>
print("cadena".__class__.__name__)  # str
