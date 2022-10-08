import random

def obtenPalabra(listadoPalabras):  
    return listadoPalabras[random.randint(0, len(listadoPalabras)-1)] 

#crea un string, por cada letra de la palabra verifica si esa letra ya fue adivinada en otro caso, pone "_".
def proceso(palabra, letrasAdivinadas):
    adivinado=""
    for letra in palabra:
        if letra in letrasAdivinadas:
            adivinado+=letra
        else:
            adivinado+="_"
    return adivinado

#solicita al usuario ingresar una letra para adivinar.Convierte letra a mayúscula.Si la letra ya había sido ingresada anteriormente, se informa y vuelve a pedir una letra.

def leerLetra(letrasAdivinadas):
    while (True):
        letra=input("Adivinar letra: ").upper().strip()
        if len(letra)==1:
            if letra in letrasAdivinadas:
                print("Ya elegiste esa letra")
            else:
                break
    return letra

#retorna False si encuentra una letra que está en la palabra a adivinar.En otro caso retorna True porque el jugador ya adivinó la palabra correcta.
def palabraCompleta(palabra, letrasAdivinadas):
    for letra in palabra:
        if letra not in letrasAdivinadas:
            return False
    return True
#únicamente imprime las reglas del juego
def instrucciones():
    print("""
INSTRUCCIONES
Este juego consiste en ir descubriendo las palabras mediante la acción "adivinar" de cada una de las letras que conforman la palabra a ser adivinada.
1. Se debe Ingresar la Palabra a adivinar.
2. El jugador inicia el juego con 6 vidas.
3. El jugador debe ingresar una letra que crea forma parte de la palabra a adivinar.""")