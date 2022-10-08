'''
dibujar vidas
'''
# Se crea una lista con nombre AHORCADO, de tamaño 6 que correspondera a cada una de las vidas para el jugador y por cada vida va dibujando una parte del ahorcado.
AHORCADO = ['''
                  +---+
                  |   |
                      |
                      |
                      |
                      |
                =========''', '''
                  +---+
                  |   |
                  O   |
                      |
                      |
                      |
                =========''', '''
                  +---+
                  |   |
                  O   |
                  |   |
                      |
                      |
                =========''', '''
                  +---+
                  |   |
                  O   |
                 /|   |
                      |
                      |
                =========''', '''
                  +---+
                  |   |
                  O   |
                 /|\  |
                      |
                      |
                =========''', '''
                  +---+
                  |   |
                  O   |
                 /|\  |
                 /    |
                      |
                =========''', '''
                  +---+
                  |   |
                  O   |
                 /|\  |
                 / \  |
                      |
                =========''']
# Define función vidas, la cual regresa la lista AHORCADO
def vidas(vidas):
      """_dibuja vidas_

      Args:
          vidas (_str_): _ letra_

      Returns:
          _str_: _ dibujo del ahorcado con guiones _
      """
      return AHORCADO[len(AHORCADO)-vidas-1]