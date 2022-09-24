from ast import Return


class Automovil:
    color ="Blanco"
    def __init__(self, nombre, velocidad_max, kilometraje,capacidad):
        self.__nombre = nombre # Ejemplo de atributo privado
        self.__velocidad_max = velocidad_max
        self.__kilometraje = kilometraje
        self.capacidad = capacidad
        
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,nombre):
        self.__nombre = nombre
        #print(f"Hola soy {nombre}")
        
    def saludar (self):
        print(f"Hola soy {self.__nombre}, VM: {self.__velocidad_max}, KM: {self.__kilometraje}")
        
    def en_marcha (self, km):
        self.__kilometraje += km
        return self.__kilometraje
    # Ejemplo de herencia la capacidfad se hereda en clase autobus
    def capacidad_pasajeros(self):
        return f"La capacidad de {self.__nombre} es de {self.capacidad} pasajeros"
    
    def tarifa(self):
        return self.capacidad * 100