class Personaje:
    # variables de clase
    def __init__(self, nombre, genero):
        # variables de instancia
        self.nombre = nombre.capitalize()
        self.genero = genero

    def obtener_nombre(self):
        return self.nombre

    def atacar(self):
        return f"{self.nombre} golpea con el puño"

    def __str__(self):  # un metodo para mostrar objetos en forma de cadena
        return "Soy un personaje"


class Guerrero(Personaje):  # Herencia
    def __init__(self, nombre, genero, raza):
        super().__init__(nombre, genero)  # constructor padre
        self.raza = raza

    def atacar(self):  # polimorfismo
        return f"{self.nombre} corta con la espada"

    def __str__(self):  # un metodo para mostrar objetos en forma de cadena
        return "Soy un guerrero/a"


class Cazador(Personaje):  # Herencia
    def __init__(self, nombre, genero, raza):
        super().__init__(nombre, genero)  # constructor padre
        self.raza = raza

    def atacar(self):  # polimorfismo
        return f"{self.nombre} lanza una flecha"

    def __str__(self):  # un metodo para mostrar objetos en forma de cadena
        return "Soy un cazador/a"


varian = Guerrero("varian", "masculino", "humano")
tyrande = Cazador("tyrande", "femenino", "elfo")

print(varian.atacar())
print(tyrande.atacar())

# Comprobar que un objeto es instancia de una clase
print(isinstance(varian, Guerrero))  # True
print(isinstance(tyrande, Guerrero))  # False
print(isinstance(tyrande, Personaje))  # True

print(varian)  # Soy un guerrero/a
print(tyrande)  # Soy un cazador/a
