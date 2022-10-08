#En esta parte se indica de que archivois se estan importando funciones, clases, dibujo del ahorcado
from funciones import *
from dibujo import vidas
from listpalabras import Listado
# en esta primera parte se declara una lista vacia la cual contendra las palabras a adivinar
l=Listado()
#Se crea un bucle while que contendra el menú y bienvenida del programa, este bucle se repetira hasta que se ingrese la opción 4
while True:
    print(" ******************************************* ")
    print("BIENVENIDO AL JUEGO DEL AHORCADO")
    print("          Diviertete    =)           ")
    print(" *******************************************")
    print("Seleccionar opción deseada")
    print("1. Instrucciones")
    print("2. Ingresa Palabra")
    print("3. jugar")
    print("4. Salir")
    #se usa condición if,elif donde si la opción ingresada correponde con las opciones del menú ejecuta la acción correspondiente
    opcion=int(input())
    if opcion==1:
        instrucciones()
    elif opcion == 2:
        l.ingresaPalabra()
    elif opcion==3:
        letrasAdivinadas=set() #se hace uso de la función set para crear un conjunto vacío donde almacena las letras ingresadas, fácilita la búsqueda de las letras correctas e incorrectas
        intentosRestantes=6
        palabra=obtenPalabra(l.get_palabras()) # convierte la lista de la palabras a adivinar a cadena de caracteres.Proviene de la clase listado y se accede a ella por medio del metodo get
        print("La palabra tiene ", len(palabra), " letras.") #En esta linea se muestra cuantas letras tiene la palabra a adivinar
        while intentosRestantes > 0: # con el ciclo while se controla el número de inbtentos a adivinar la palabra mientras sea mayor a cero
            if palabraCompleta(palabra, letrasAdivinadas):
                print("¡Felicidades Ganaste el Juego!")
                break
            mostrar=proceso(palabra, letrasAdivinadas) # esta línea dibuja los guiones bajos que corresponden a cada una de las letras de la palabra a adivinar y la letra cuando es correcta
            print(mostrar)
            print(vidas(intentosRestantes))
            letra=leerLetra(letrasAdivinadas)
            letrasAdivinadas.add(letra) # lleva el registro de las letras correctas adivinadas, se agregan con la función add simila o parecido a append
            if letra not in palabra: # valida si la letra no esta en la palabra a adivinar y procede a ejecutras las acciones definidas
                intentosRestantes-=1 # decrementa los intentos
                print(vidas(intentosRestantes))
                print("¡Letra Incorrecta! Intentos restantes: ", intentosRestantes)
            else:
                print("¡Letra Correcta!")
    elif opcion==4:
        print("¡Adios, vuelve Pronto!")
        break
    else:
        print("Opción inválida")
