'''
Progra 3 de Taller

Consiste de dos juegos; un juego de cartas estilo "21" o "Ron",
y otro que imita al juego cásico de "Fox and Houds" o "El zorro y los Sabuesos"
'''

import random
import time
from colorama import Fore, init
init(autoreset=True)

# ----------------- FUNCIONES AUXILIARES -----------------

def es_numerico(string):
    '''
    Verfifica si un string contiene solo caracteres numericos

    E: Un string
    S: Un booleano que indica si el string es numerico
    R: string debe ser un string, de lo contrario retorna False.
    '''

    if type(string) != str:
        return False
    
    for elem in range(len(string)):

        if string[elem] != "0" and string[elem] != "1" and string[elem] != "2" and \
            string[elem] != "3" and string[elem] != "4" and string[elem] != "5" and \
            string[elem] != "6" and string[elem] != "7" and string[elem] != "8" and \
            string[elem] != "9":
            return False
        
    return True


# ----------------- FUNCIONES DEL JUEGO -----------------

def menu_principal():
    '''
    Muestra el menú principal del juego y permite al usuario elegir una opción

    E: Un numero del 1 al 4
    S: Llama a la función encargada de la opción elegida por el usuario.
    R: Se debe ingresar un número del 1 al 4.
    '''

    print(r'''

##############################################################################
#                                                                            #
#                                                                            #
#      __  __              __    ____       _            _             _     #
#     |  \/  | ___ _ __  _/_/_  |  _ \ _ __(_)_ __   ___(_)_ __   __ _| |    #
#     | |\/| |/ _ \ '_ \| | | | | |_) | '__| | '_ \ / __| | '_ \ / _` | |    #
#     | |  | |  __/ | | | |_| | |  __/| |  | | | | | (__| | |_) | (_| | |    #
#     |_|  |_|\___|_| |_|\__,_| |_|   |_|  |_|_| |_|\___|_| .__/ \__,_|_|    #
#                                                         |_|                #
#                                                                            #
#                                                                            #
##############################################################################

            ''')
    time.sleep(1)

    print("1. Jugar") # -> Jugar
    time.sleep(1)
    print("2. Lore") # -> Lore
    time.sleep(1)
    print("3. Cómo jugar") # -> Instrucciones
    time.sleep(1)
    print("4. Créditos") # -> EasterEgg
    time.sleep(1)
    print("\nq. Salir") # -> Salir
    time.sleep(1)

    opción = input(f"\nElige una {Fore.YELLOW}opción:{Fore.RESET}")

    if not es_numerico(opción) and opción != "q" and opción != "Q":
        print("\nNo es una opción valida! \n")
        time.sleep(3)
        return menu_principal()
    
    elif opción == "1":
        return elegir_juego()
    
    elif opción == "2":
        return ""
    
    elif opción == "3":
        return ""
    
    elif opción == "4":
        return ""
    
    elif opción == "q" or opción == "Q":
        print("\nVuelve Pronto!")
        time.sleep(3)
        return ""
    
    else:
        print(f"\nEsa no es una opción valida! \n")
        time.sleep(3)
        return menu_principal()

def elegir_juego():

    print("\nElige uno de los juegos para comenzar la partida:\n")
    time.sleep(1)
    
    print("1. La encuadrillada (Fox and Hounds)")
    time.sleep(1)

    print("2. La Disputa (21)")
    time.sleep(1)

    print("\nq. Atrás")
    time.sleep(1)

    opción = input(f"\nElige una {Fore.YELLOW}opción:{Fore.RESET}")

    if not es_numerico(opción) and opción != "q" and opción != "Q":
        print("\nIgresa una opción valida! \n")
        time.sleep(3)
        return elegir_juego()
    
    elif opción == "1":
        return "JUEGO 1"
    
    elif opción == "2":
        return iniciar_veintiuno()
    
    elif opción == "q" or opción == "Q":
        return menu_principal()
    
    else:
        print(f"\nEsa no es una opción valida! \n")
        time.sleep(3)
        return elegir_juego()
    
# ---------------------- LIEBRE Y PERROS ----------------------

def inicio_liebre_y_perros ():
    tablero = lyp_crear_tablero([])
    mostrar_tablero(tablero)

def lyp_crear_tablero(tablero):
    '''
    Funcion que crea el tablero para el juego de liebres y los perros de caza

    E: Nada
    S: Una matriz que representa el tablero del juego
    R: Ninguna
    '''
    fila = []
    for i in range(2):

        columna = []
        for i2 in range(4):
            columna += ["y"]
        fila += columna
        tablero += [fila]

    print(tablero)
    return tablero

def mostrar_tablero(tablero):
    for fila in tablero:
        
        for elemento in fila:
            print(elemento, end=" ")
        print()


# ---------------------- VEINTIUNO ----------------------

def iniciar_veintiuno():

    print("\nBienvenidx al Juego de 21!\n")
    time.sleep(1)

    print("Elige un Modo de Juego:\n")
    time.sleep(1)

    print("1. Un Jugador (V.S. COM.)")
    time.sleep(1)

    print("2. Dos Jugadores")
    time.sleep(1)

    print("\nq. Atrás")
    time.sleep(1)

    opción = input(f"\nElige una {Fore.YELLOW}opción:{Fore.RESET}")

    if not es_numerico(opción) or opción != "q" or opción != "Q":
        print("\nIgresa una opción valida! \n")
        time.sleep(3)
        return iniciar_veintiuno()
    
    elif opción == "1":
        return ""
    
    elif opción == "2":
        return ""
    
    elif opción == "q" or opción == "Q":
        return elegir_juego()
    
    else:
        print(f"\nEsa no es una opción valida! \n")
        time.sleep(3)
        return iniciar_veintiuno()
# ---------------------- EXPERIMENTAL ----------------------


res = menu_principal()
print(res)

