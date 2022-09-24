
from automovil import Automovil
class Autobus(Automovil):
#se sobre escribe la herencia capacidad de automovil a autobus
    def capacidad_pasajeros(self):
        return f"La capacidad de {self.__nombre} es de {self.capacidad} pasajeros"
    def tarifa(self):
        monto = super().tarifa()
        monto += monto*10/100
        return monto