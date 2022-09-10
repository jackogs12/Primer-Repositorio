''' importar todas las funciones de funciones'''
#from funciones import *
''' importar todo el archivo y darle un alias'''
import funciones as f
#import random as r

def main():
    print("Hola mundo")
    #n = suma_n_numeros(1,2,3,4,5,6)
    #print(n)
    suma = f.suma_n_numeros(1,5)
   # ran = r.randint()
    
    #maxi,mini = f.maximo_minimo(1,2,3)
    #print(f"maximo = {maxi} , minimo = {mini}")
    
if __name__ == "__main__":
    main()