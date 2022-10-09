import random

def obtenPalabra(listadoPalabras):  
    """_ ontiene palabra_

    Args:
        listadoPalabras (_str_): _cadena de caracteres_

    Returns:
        _str_: _lista de palabras_
    """
    return listadoPalabras[random.randint(0, len(listadoPalabras)-1)] 

#crea un string, por cada letra de la palabra verifica si esa letra ya fue adivinada en otro caso, pone "_".
def proceso(palabra:str, letrasAdivinadas:str)->str:
    """_proceso_

    Args:
        palabra (str): _recibe una letra_
        letrasAdivinadas (str): _se crea string por letra y valida si ya fue ingresada

    Returns:
        str: _coloca la letra adivinada y encaso de no ser la letra esperada dibuja nuevamente un guion_
    """
    adivinado=""
    for letra in palabra:
        if letra in letrasAdivinadas:
            adivinado+=letra
        else:
            adivinado+="_"
    return adivinado

#solicita al usuario ingresar una letra para adivinar.Convierte letra a mayúscula.Si la letra ya había sido ingresada anteriormente, se informa y vuelve a pedir una letra.

def leerLetra(letrasAdivinadas):
    """_lee letra_

    Args:
        letrasAdivinadas (_char_): _letras ingresada en mayúscula y valida si ya habia sido ingresada e informa_

    Returns:
        _char_: _letra adivida correcta_
    """
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
    """_palabra completa_

    Args:
        palabra (_str_): _letra a ser adivinada_
        letrasAdivinadas (_str_): _verifica si no esta la letra en las letras adivinadas _

    Returns:
        _bool_: _falso o verdadero_
    """
    for letra in palabra:
        if letra not in letrasAdivinadas:
            return False
    return True
#únicamente imprime las reglas del juego
def instrucciones():
    """
    imprime las instrucciones del juego
    """
    print("""
INSTRUCCIONES
Este juego consiste en ir descubriendo las palabras mediante la acción "adivinar" de cada una de las letras que conforman la palabra a ser adivinada.
1. Se debe Ingresar la Palabra a adivinar.
2. El jugador inicia el juego con 6 vidas.
3. El jugador debe ingresar una letra que crea forma parte de la palabra a adivinar.""")