from ast import Return
import random

class Listado: #se contruye la clase listado, se crea su constructor y sus metodos get y set

    def __init__(self):
        self.palabras = []

    def get_palabras(self):
        return self.palabras

    def set_palabras(self,palabra):
        self.palabras.append(palabra)
# solicita ingresar las palabras y las va agregando a la lista.La palabra se pasa a mayúsculas antes de insertarse en la lista..
    def ingresaPalabra(self):
        """_ingresaPalabra_
        """
        palabra=input("Ingresar palabra a advivinar ó letra \"F\" para finalizar:").upper().strip() 
        #strip elimina los espacios en blanco
        while palabra!="F":
            self.set_palabras(palabra)
            palabra=input("Ingresar palabra a advivinar ó letra \"F\" para finalizar:").upper().strip()
    

