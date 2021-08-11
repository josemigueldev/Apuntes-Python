# METODOS DE ELEMINACION ======================================================
# Vaciar un diccionario
diccionario = {"color": "azul", "talla": "XL", "precio": 174.75}
# diccionario.clear()

# METODOS DE AGREGACION Y CREACION ============================================
# Copiar un diccionario
camiseta = diccionario.copy()

# Crear un nuevo diccionario desde las claves de una secuencia
secuencia = ["color", "talla", "precio"]
camiseta2 = dict.fromkeys(secuencia)
# {'color': None, 'talla': None, 'precio': None}

camiseta3 = dict.fromkeys(secuencia, "valor")
# {'color': "valor", 'talla': "valor", 'precio': "valor"}

# Concatenar diccionarios
dic1 = {"color": "verde", "precio": 45}
dic2 = {"talla": "M", "marca": "lacoste"}
dic1.update(dic2)
# dic1 => {'color': 'verde', 'precio': 45, 'talla': 'M', 'marca': 'lacoste'}

# Establecer una clave y valor por defecto
# retorna el valor por defecto
remera = {"color": "rosa", "marca": "Zara"}
remera.setdefault("talla", "L")
# {'color': 'rosa', 'marca': 'Zara', 'talla': 'L'}
remera.setdefault("precio")
# {'color': 'rosa', 'marca': 'Zara', 'talla': 'L', 'precio': None}

# METODOS DE RETORNO ==========================================================
# Obtener el valor de una clave
remera.get("talla")  # "L"

# Saber si una clave existe en el diccionario
print("talla" in remera)  # True
print("empresa" in remera)  # False

# Obtener las clave y valores de un diccionario
for clave, valor in remera.items():
    print(clave, valor)

# Obtener las claves
remera.keys()

# Obtener los valores
remera.values()

# Longitud de un diccionario
print(len(remera))
