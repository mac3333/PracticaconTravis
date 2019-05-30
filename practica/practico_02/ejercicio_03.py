# Implementar la clase Persona que cumpla las siguientes condiciones:
# Atributos:
# - nombre.
# - edad.
# - sexo (H hombre, M mujer).
# - peso.
# - altura.
# Métodos:
# - es_mayor_edad(): indica si es mayor de edad, devuelve un booleano.
# - print_data(): imprime por pantalla toda la información del objeto.
# - generar_dni(): genera un número aleatorio de 8 cifras y lo guarda dentro del atributo dni.


class Persona:
    last_dni = 0

    def __init__(self, nombre, edad, sexo, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
        self.dni = self.__generar_dni()

    def es_mayor_edad(self):
        return self.edad >= 18

    # llamarlo desde __init__
    @classmethod
    def __generar_dni(cls):
        cls.last_dni += 1
        return str(cls.last_dni).zfill(8)
        
    def print_data(self):
        print(f"Información Personal de {self.nombre}")
        print(f"DNI: {self.dni}")
        print(f"Edad: {self.edad}")
        print(f"Sexo: {self.sexo}")
        print(f"Peso: {self.peso}")
        print(f"Altura: {self.altura}")
