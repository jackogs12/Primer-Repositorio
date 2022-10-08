from ast import Return
import random

class Listado: #se contruye la clase listado, se crea su constructor y sus metodos get y set

    def __init__(self):
        self.palabras = []

    def get_palabras(self):
        """_encapsula palabra_

        Returns:
            _str_: _atributo privado_
        """
        return self.palabras

    def set_palabras(self,palabra):
        """_recupera atributo_

        Args:
            palabra (_str_): _recupera valor de atributo_
        """
        self.palabras.append(palabra)
# solicita ingresar las palabras y las va agregando a la lista.La palabra se pasa a mayúsculas antes de insertarse en la lista..
    def ingresaPalabra(self):
        """_ingresa palabra a ser adivinada_
        """
        palabra=input("Ingresar palabra a advivinar ó letra \"F\" para finalizar:").upper().strip() 
        #strip elimina los espacios en blanco
        while palabra!="F":
            self.set_palabras(palabra)
            palabra=input("Ingresar palabra a advivinar ó letra \"F\" para finalizar:").upper().strip()
    

