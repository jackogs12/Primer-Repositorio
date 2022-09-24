from automovil import Automovil
from autobus import Autobus
def main():
    #print("Hola Mundo") Impresion para saber que se ejecuta el constructor
    # ceando objeto
    a1 = Automovil("Toyota", 80, 300,4)
    a2 = Automovil("Volvo",100,200,3)
    a3 = Automovil("Kia",250, 400,6) 
    
    b1 = Autobus("Caterpilla", 60, 80,4)
    

    #print(f"Hola soy {a1.nombre}, velocidad maxima {a1.velocidad_max}, Kilometraje {a1.kilometraje}")
    #Metodo es un comportamiento de un objeto
    print(a1.tarifa())
    print(b1.tarifa())
    #print(a1.capacidad_pasajeros())
    #print(b1.capacidad_pasajeros())
    a1.en_marcha(100)
    a1.saludar()
    a2.en_marcha(30)
    a2.saludar()
    a3.en_marcha(300)
    a3.saludar()
    a1.set_nombre("vw")
    print(a1.get_nombre())

if __name__=="__main__":
    main()