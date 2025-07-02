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
        return cómo_jugar_main()
    
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
        return inicio_juego_caza()
    
    elif opción == "2":
        return menu_veintiuno()
    
    elif opción == "q" or opción == "Q":
        return menu_principal()
    
    else:
        print(f"\nEsa no es una opción valida! \n")
        time.sleep(3)
        return elegir_juego()
    
def cómo_jugar_main():

    print("\nElige uno de los juegos para saber cómo jugar:\n")
    time.sleep(1)
    
    print("1. Anarquistas y El Fascista (Fox and Hounds)")
    time.sleep(1)

    print("2. Lo que siguió (21)")
    time.sleep(1)

    print("\nq. Atrás")
    time.sleep(1)

    while True:

        opción = input(f"\nElige una {Fore.YELLOW}opción:{Fore.RESET}")

        if not es_numerico(opción) and opción != "q" and opción != "Q":
            print("\nIgresa una opción valida! \n")
            time.sleep(3)
            continue

        elif opción == "1":
            return cj_caza()
        
        elif opción == "2":
            return cj_veintiuno()
        
        elif opción == "q" or opción == "Q":
            return menu_principal()
        
        else:
            print(f"\nEsa no es una opción valida! \n")
            time.sleep(3)
            continue

# ------------------------- CÓMO JUGAR ------------------------

def cj_caza():

    return ''

def cj_veintiuno():

    return ''  

# ---------------------- LIEBRE Y PERROS ----------------------

def inicio_juego_caza():
    '''Funcion principal del juego'''
    print("")
    print("Bienvenido a la Liebre y los Perros de Caza.")
    print("")
    time.sleep(1)
    print("Te enfrentas a la computadora.")
    print("")

    tablero = crear_tablero_caza()
    turno = 0
    while turno != 2:

        if turno == 0:

            time.sleep(2)
            print("--Tablero de juego--")
            print("")

            mostrar_tablero_caza(tablero)
            print("")
            print("A1: Anarquista Max Striner \nA2: Anarquista Lysander Spooner \n" \
                    "A3: Anarquista Guillermo Godwin \nF: Facista agresivo")
            print("")
            
            time.sleep(1)
            eleccion = input("Que anarquista desea mover (1 - 2 - 3): ")
            while not verificar_existe_caza(eleccion):

                time.sleep(1)
                print("Seleccione un anarquista existente: ")
                eleccion = input("Que anarquista desea mover: ")
            
            anarquista = "(A" + eleccion +")"
            posibilidades = posibilidad_caza(anarquista, tablero)
            posicion = posicion_caza(anarquista, tablero)
            if posibilidades == "1":

                bloqueos = bloqueos_f1_caza(anarquista, tablero, posicion)

            elif posibilidades == "2":

                bloqueos = bloqueos_f3_caza(anarquista, tablero, posicion)

            else:

                bloqueos = bloqueos_f2_caza(anarquista, tablero, posicion)

            while bloqueos == []:

                print("No hay caminos disponibles.\
                    Seleccion otro Anarquista.")
                eleccion = input("Que anarquista desea mover (1 - 2 - 3): ")
                print("")
                while not verificar_existe_caza(eleccion):

                    print("Seleccione un anarquista existente: ")
                    eleccion = input("Que anarquista desea mover: ")
                
                anarquista = "(A" + eleccion +")"
                posibilidades = posibilidad_caza(anarquista, tablero)
                posicion = posicion_caza(anarquista, tablero)
                if posibilidades == "1":

                    bloqueos = bloqueos_f1_caza(anarquista, tablero, posicion)

                elif posibilidades == "2":

                    bloqueos = bloqueos_f3_caza(anarquista, tablero, posicion)

                else:

                    bloqueos = bloqueos_f2_caza(anarquista, tablero, posicion)

            time.sleep(1)
            camino = opciones_caza(bloqueos)
            tablero = modificar_tablero_caza(anarquista, posicion, tablero, camino)

            time.sleep(1)
            print("--Tablero de juego--")
            mostrar_tablero_caza(tablero)
            turno = 1

        if turno == 1:
            fascista = "(F)"
            posibilidades = posibilidad_caza(fascista, tablero)
            posicion = posicion_caza(fascista, tablero)
            if posicion[1] == 0:

                return print("El fascista agrasivo escapo.\n" + "Fin del juego.")  
            
            if posibilidades == "1":

                bloqueos = bloqueos_f1_fascista(tablero, posicion)

            elif posibilidades == "2":

                bloqueos = bloqueos_f3_fascista(tablero, posicion)

            else:

                bloqueos = bloqueos_f2_fascista(tablero, posicion)            
                
            if bloqueos == []:

                return print("El fascista ha sido capturado.\n" + "Los anarquistas ganan el juego.")
                
            else:
                camino = opciones_fascista(bloqueos)
                tablero = modificar_tablero_fascista(fascista, posicion, tablero, camino)

                time.sleep(1)
                print("")
                print("--Tablero de juego--")
                print("")
                mostrar_tablero_caza(tablero)
                print("")
                print("El fascista se mueve hacia: " + camino)
                print("")
                turno = 0

def crear_tablero_caza():
    '''Crea el tablero de 5x3'''
    fila = []
    for i in range(5):
        
        if i == 1:
            columna = [r"   /  | \ | / | \ "]
            fila += [columna]

        elif i == 3:
            columna = [r"   \  | / | \ | / "]
            fila += [columna]

        else:
            columna = []
            for x in range(9):
                
                if x == 0 or x == 2 or\
                      x == 4 or x == 6 or\
                        x == 8:

                    if i == 0 and x == 2:

                        columna += ["(A1)"]

                    elif i == 2 and x == 0:

                        columna += ["(A2)"]
                    
                    elif i == 4 and x == 2:

                        columna += ["(A3)"]

                    elif i == 2 and x == 8:

                        columna += ["(F)"]

                    else:

                        columna += ["( )"]
                
                else:

                    if i == 2 and x == 1 or\
                        i == 2 and x == 7:
                        
                        columna += ["-"] 

                    elif x == 3 or x == 5:
                        
                        columna += ["-"] 

                    else:

                        columna += [""]                  

            fila += [columna]

    return fila

def mostrar_tablero_caza(tablero):
    '''Hace print del tablero'''
    for fila in range(len(tablero)):

        for columna in range(len(tablero[fila])):
            
            if fila == 0 and columna == 0 or\
                fila == 0 and columna == 8:

                print("    ", end="")
            
            elif fila == 4 and columna == 0 or\
                fila == 4 and columna == 8:

                print("    ", end="")
            
            else:
                print(tablero[fila][columna], end="")

        print()

def verificar_existe_caza(eleccion):
    '''Verifica que la seleccion del anarquista exista'''
    if eleccion == "1" or eleccion == "2" or eleccion == "3":

        return True
    
    else:

        return False
    
def posibilidad_caza(objeto, tablero):
    '''busca las opciones del anarquista al anarquista'''
    for fila in range(len(tablero)):

        for columna in range(len(tablero[fila])):
            
            if fila == 0 and tablero[fila][columna] == objeto:

                return "1"
            
            if fila == 4 and tablero[fila][columna] == objeto:

                return "2"

            if fila == 2 and tablero[fila][columna] == objeto:

                return "3"

def posicion_caza(objeto, tablero):
    '''Devuelve la posicion del anarquista seleccionado'''
    for fila in range(len(tablero)):

        for columna in range(len(tablero[fila])):
            
            if tablero[fila][columna] == objeto:

                return [fila, columna]
            
def bloqueos_f1_caza(anarquista, tablero, posicion):
    '''Determina que caminos estan bloqueados'''
    caminos = []
    if posicion[1] == 2:

        for i in range(3):

            if i == 0:

                if tablero[posicion[0]][posicion[1] + 2] == "( )":

                    caminos += ["Derecha"]

            elif i == 1:

                if tablero[posicion[0] + 2][posicion[1] + 2] == "( )":

                    caminos += ["Diagonal Abajo"]

            else:

                if tablero[posicion[0] + 2][posicion[1]] == "( )":

                    caminos += ["Abajo"]

        return caminos
    
    elif posicion[1] == 4:

        for i in range(2):

            if i == 0:

                if tablero[posicion[0]][posicion[1] + 2] == "( )":

                    caminos += ["Derecha"]

            else:

                if tablero[posicion[0] + 2][posicion[1]] == "( )":

                    caminos += ["Abajo"]

        return caminos
    
    else:

        for i in range(2):

            if i == 0:

                if tablero[posicion[0] + 2][posicion[1] + 2] == "( )":

                    caminos += ["Diagonal Abajo"]

            else:

                if tablero[posicion[0] + 2][posicion[1]] == "( )":

                    caminos += ["Abajo"]

        return caminos
    
def bloqueos_f2_caza(anarquista, tablero, posicion):
    '''Determina que caminos estan bloqueados'''
    caminos = []
    if posicion[1] == 0:

        for i in range(3):

            if i == 0:

                if tablero[posicion[0] - 2][posicion[1] + 2] == "( )":

                    caminos += ["Diagonal Arriba"]

            elif i == 1:

                if tablero[posicion[0]][posicion[1] + 2] == "( )":

                    caminos += ["Derecha"]

            else:

                if tablero[posicion[0] + 2][posicion[1] + 2] == "( )":

                    caminos += ["Diagonal Abajo"]

        return caminos

    elif posicion[1] == 2 or posicion[1] == 6:
        
        for i in range(3):

            if i == 0:

                if tablero[posicion[0] - 2][posicion[1]] == "( )":

                    caminos += ["Arriba"]

            elif i == 1:

                if tablero[posicion[0]][posicion[1] + 2] == "( )":

                    caminos += ["Derecha"]

            else:

                if tablero[posicion[0] + 2][posicion[1]] == "( )":

                    caminos += ["Abajo"]

        return caminos
    
    else:
        
        for i in range(5):

            if i == 0:

                if tablero[posicion[0] - 2][posicion[1]] == "( )":

                    caminos += ["Arriba"]

            elif i == 1:

                if tablero[posicion[0] - 2][posicion[1] + 2] == "( )":

                    caminos += ["Diagonal Arriba"]

            elif i == 2:

                if tablero[posicion[0]][posicion[1] + 2] == "( )":

                    caminos += ["Derecha"]

            elif i == 3:

                if tablero[posicion[0] + 2][posicion[1] + 2] == "( )":

                    caminos += ["Diagonal Abajo"]

            else:

                if tablero[posicion[0] + 2][posicion[1]] == "( )":

                    caminos += ["Abajo"]

        return caminos

def bloqueos_f3_caza(anarquista, tablero, posicion):
    '''Determina que caminos estan bloqueados'''
    caminos = []
    if posicion[1] == 2:

        for i in range(3):

            if i == 0:

                if tablero[posicion[0] - 2][posicion[1]] == "( )":

                    caminos += ["Arriba"]

            elif i == 1:

                if tablero[posicion[0] - 2][posicion[1] + 2] == "( )":

                    caminos += ["Diagonal Arriba"]

            else:

                if tablero[posicion[0]][posicion[1] + 2] == "( )":

                    caminos += ["Derecha"]

        return caminos
    
    elif posicion[1] == 4:

        for i in range(2):

            if i == 0:

                if tablero[posicion[0] - 2][posicion[1]] == "( )":

                    caminos += ["Arriba"]

            else:

                if tablero[posicion[0]][posicion[1] + 2] == "( )":

                    caminos += ["Derecha"]

        return caminos
    
    else:

        for i in range(2):

            if i == 0:

                if tablero[posicion[0] - 2][posicion[1]] == "( )":

                    caminos += ["Arriba"]

            else:

                if tablero[posicion[0] - 2][posicion[1] + 2] == "( )":

                    caminos += ["Diagonal Arriba"]

        return caminos
    
def bloqueos_f1_fascista(tablero, posicion):
    '''Determina que caminos estan bloqueados de la primera linea'''
    caminos = []
    if posicion[1] == 6:

        for i in range(4):

            if i == 0:

                if tablero[posicion[0]][posicion[1] - 2] == "( )":

                    caminos += ["Izquierda"]

            elif i == 1:

                if tablero[posicion[0] + 2][posicion[1] - 2] == "( )":

                    caminos += ["Diagonal Abajo Izquierda"]

            elif i == 2:

                if tablero[posicion[0] + 2][posicion[1]] == "( )":

                    caminos += ["Abajo"]

            else:

                if tablero[posicion[0] + 2][posicion[1] + 2] == "( )":

                    caminos += ["Diagonal Abajo Derecha"]

        return caminos
    
    elif posicion[1] == 4:

        for i in range(3):

            if i == 0:

                if tablero[posicion[0]][posicion[1] - 2] == "( )":

                    caminos += ["Izquierda"]

            elif i == 1:

                if tablero[posicion[0] + 2][posicion[1]] == "( )":

                    caminos += ["Abajo"]

            else:

                if tablero[posicion[0]][posicion[1] + 2] == "( )":

                    caminos += ["Derecha"]

        return caminos
    
    else:

        for i in range(4):

            if i == 0:

                if tablero[posicion[0] + 2][posicion[1] - 2] == "( )":

                    caminos += ["Diagonal Abajo Izquierda"]

            elif i == 1:

                if tablero[posicion[0] + 2][posicion[1]] == "( )":

                    caminos += ["Abajo"]

            elif i == 2: 

                if tablero[posicion[0] + 2][posicion[1] + 2] == "( )":

                    caminos += ["Diagonal Abajo Derecha"]

            else:

                if tablero[posicion[0]][posicion[1] + 2] == "( )":

                    caminos += ["Derecha"]

        return caminos
    
def bloqueos_f2_fascista(tablero, posicion):
    '''Determina que caminos estan bloqueados'''
    caminos = []
    if posicion[1] == 8:

        for i in range(3):

            if i == 0:

                if tablero[posicion[0] - 2][posicion[1] - 2] == "( )":

                    caminos += ["Diagonal Arriba Izquierda"]

            elif i == 1:

                if tablero[posicion[0]][posicion[1] - 2] == "( )":

                    caminos += ["Izquierda"]

            else:

                if tablero[posicion[0] + 2][posicion[1] - 2] == "( )":

                    caminos += ["Diagonal Abajo Izquierda"]

        return caminos

    elif posicion[1] == 2 or posicion[1] == 6:
        
        for i in range(4):

            if i == 0:

                if tablero[posicion[0] - 2][posicion[1]] == "( )":

                    caminos += ["Arriba"]

            elif i == 1:

                if tablero[posicion[0]][posicion[1] - 2] == "( )":

                    caminos += ["Izquierda"]

            elif i == 2:

                if tablero[posicion[0] + 2][posicion[1]] == "( )":

                    caminos += ["Abajo"]
            
            else:

                if tablero[posicion[0]][posicion[1] + 2] == "( )":

                    caminos += ["Derecha"]

        return caminos
    
    elif posicion[1] == 4:
        
        for i in range(8):

            if i == 0:

                if tablero[posicion[0] - 2][posicion[1]] == "( )":

                    caminos += ["Arriba"]

            elif i == 1:

                if tablero[posicion[0] - 2][posicion[1] - 2] == "( )":

                    caminos += ["Diagonal Arriba Izquierda"]

            elif i == 2:

                if tablero[posicion[0]][posicion[1] - 2] == "( )":

                    caminos += ["Izquierda"]

            elif i == 3:

                if tablero[posicion[0] + 2][posicion[1] - 2] == "( )":

                    caminos += ["Diagonal Abajo Izquierda"]

            elif i == 4:

                if tablero[posicion[0] + 2][posicion[1]] == "( )":

                    caminos += ["Abajo"]
            
            elif i == 5:

                if tablero[posicion[0] + 2][posicion[1] + 2] == "( )":

                    caminos += ["Diagonal Abajo Derecha"]

            elif i == 6: 
                
                if tablero[posicion[0]][posicion[1] + 2] == "( )":

                    caminos += ["Derecha"]
            
            else:

                if tablero[posicion[0] - 2][posicion[1] + 2] == "( )":

                    caminos += ["Diagonal Arriba Derecha"]
        else:

            caminos += ["Fin"]

        return caminos

def bloqueos_f3_fascista(tablero, posicion):
    '''Determina que caminos estan bloqueados'''
    caminos = []
    if posicion[1] == 6:

        for i in range(4):

            if i == 0:
                
                if tablero[posicion[0] - 2][posicion[1] + 2] == "( )":

                    caminos += ["Diagonal Arriba Derecha"]

            elif i == 1:

                if tablero[posicion[0] - 2][posicion[1]] == "( )":

                    caminos += ["Arriba"]

            elif i == 2:

                if tablero[posicion[0] - 2][posicion[1] - 2] == "( )":

                    caminos += ["Diagonal Arriba Izquierda"]

            else:

                if tablero[posicion[0]][posicion[1] - 2] == "( )":

                    caminos += ["Izquierda"]

        return caminos
    
    elif posicion[1] == 4:

        for i in range(3):

            if i == 0:

                if tablero[posicion[0]][posicion[1] + 2] == "( )":

                    caminos += ["Derecha"]

            elif i == 1:

                if tablero[posicion[0] - 2][posicion[1]] == "( )":

                    caminos += ["Arriba"]

            else:

                if tablero[posicion[0]][posicion[1] - 2] == "( )":

                    caminos += ["Izquierda"]

        return caminos
    
    else:

        for i in range(4):

            if i == 0:

                if tablero[posicion[0]][posicion[1] + 2] == "( )":

                    caminos += ["Derecha"]

            elif i == 1:

                if tablero[posicion[0] - 2][posicion[1] + 2] == "( )":

                    caminos += ["Diagonal Arriba Derecha"]

            elif i == 2:

                if tablero[posicion[0] - 2][posicion[1]] == "( )":

                    caminos += ["Arriba"]

            else:

                if tablero[posicion[0] - 2][posicion[1] - 2] == "( )":

                    caminos += ["Diagonal Arriba Izquierda"]

        return caminos

def opciones_caza(bloqueos):
    '''Deja al jugador seleccionar el camino que desea tomar'''
    num = 1
    opciones = []
    for i in range(len(bloqueos)):

        print(str(num) + ". " + bloqueos[i])
        opciones += [str(num)]
        num += 1

    time.sleep(1)
    print("")
    seleccion = input("Seleccione el camino deseado: ")
    while seleccion != 0:

        for i in opciones:

            if i == seleccion:

                return bloqueos[int(i)-1]
        
        time.sleep(1)
        print("")
        seleccion = input("Seleccione un camino existente: ")

def opciones_fascista(bloqueos):
    '''Selecciona el camino que la maquina va a tomar'''
    num = 1
    opciones = []
    for i in range(len(bloqueos)):

        opciones += [num]
        num += 1

    seleccion = random.randint(1,len(bloqueos))
    while seleccion != 0:

        for i in opciones:

            if i == seleccion:

                return bloqueos[i-1]
            
def modificar_tablero_caza(anarquista, posicion, tablero, camino):
    '''Modifica el tablero con el movimiento seleccionado'''
    if camino == "Arriba":

        tablero[posicion[0]][posicion[1]] = "( )"
        tablero[posicion[0] - 2][posicion[1]] = anarquista
        return tablero

    if camino == "Diagonal Arriba":

        tablero[posicion[0]][posicion[1]] = "( )"
        tablero[posicion[0] - 2][posicion[1] + 2] = anarquista
        return tablero
    
    if camino == "Derecha":

        tablero[posicion[0]][posicion[1]] = "( )"
        tablero[posicion[0]][posicion[1] + 2] = anarquista
        return tablero
    if camino == "Diagonal Abajo":

        tablero[posicion[0]][posicion[1]] = "( )"
        tablero[posicion[0] + 2][posicion[1] + 2] = anarquista
        return tablero
    if camino == "Abajo":

        tablero[posicion[0]][posicion[1]] = "( )"
        tablero[posicion[0] + 2][posicion[1]] = anarquista
        return tablero
    
def modificar_tablero_fascista(fascista, posicion, tablero, camino):
    '''Modifica el tablero con el movimiento seleccionado'''
    if camino == "Arriba":

        tablero[posicion[0]][posicion[1]] = "( )"
        tablero[posicion[0] - 2][posicion[1]] = fascista
        return tablero

    elif camino == "Diagonal Arriba Izquierda":

        tablero[posicion[0]][posicion[1]] = "( )"
        tablero[posicion[0] - 2][posicion[1] - 2] = fascista
        return tablero
    
    elif camino == "Izquierda":

        tablero[posicion[0]][posicion[1]] = "( )"
        tablero[posicion[0]][posicion[1] - 2] = fascista
        return tablero
    
    elif camino == "Diagonal Abajo Izquierda":

        tablero[posicion[0]][posicion[1]] = "( )"
        tablero[posicion[0] + 2][posicion[1] - 2] = fascista
        return tablero
    
    elif camino == "Abajo":

        tablero[posicion[0]][posicion[1]] = "( )"
        tablero[posicion[0] + 2][posicion[1]] = fascista
        return tablero
    
    elif camino == "Diagonal Abajo Derecha":

        tablero[posicion[0]][posicion[1]] = "( )"
        tablero[posicion[0] + 2][posicion[1] + 2] = fascista
        return tablero
    
    elif camino == "Derecha":

        tablero[posicion[0]][posicion[1]] = "( )"
        tablero[posicion[0]][posicion[1] + 2] = fascista
        return tablero
    
    elif camino == "Diagonal Arriba Derecha":

        tablero[posicion[0]][posicion[1]] = "( )"
        tablero[posicion[0] - 2][posicion[1] + 2] = fascista
        return tablero
# ---------------------- VEINTIUNO ----------------------

def repartir_cartas(num):

    for i in range(num):

        carta = random.randint(1, 52)

        if carta < 1 or carta > 52:
            print("\nError: El número de carta debe estar entre 1 y 52.")

        if carta in range(1, 5):
            carta = 2

        elif carta in range(5, 9):
            carta = 3

        elif carta in range(9, 13):
            carta = 4
        
        elif carta in range(13, 17):
            carta = 5

        elif carta in range(17, 21):
            carta = 6

        elif carta in range(21, 25):
            carta = 7

        elif carta in range(25, 29):
            carta = 8

        elif carta in range(29, 33):
            carta = 9

        elif carta in range(33, 49):
            carta = 10

        else:
            carta = 'AS'

        return carta


def menu_veintiuno():

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

    if not es_numerico(opción) and opción != "q" and opción != "Q":
        print("\nIgresa una opción valida! \n")
        time.sleep(3)
        return menu_veintiuno()
    
    elif opción == "1":
        return veintiuno_main(["LA COM", "LA CASA"])
    
    elif opción == "2":
        return veintiuno_main(["J1", "LA CASA"])
    
    elif opción == "q" or opción == "Q":
        return elegir_juego()
    
    else:
        print(f"\nEsa no es una opción valida! \n")
        time.sleep(3)
        return menu_veintiuno()
    


def veintiuno_main(modalidad):

    cartas = [[],[]]

    while True:

        index = 0

        while index < 2:

            print(f"\n===== REPARTIENDO CARTAS A {modalidad[index]} =====\n")

            cartas[index] += [repartir_cartas(2)]
            time.sleep(2)
            print('Done!')
            time.sleep(1)

            if index == 1 and modalidad[index] == 'LA COM' or 'J1' and cartas[index][0] == 5:

                coin = random.randint(0, 3)
                if coin == 0:
                    return fin_21(pierde='LA CASA', motivo=2)

            index += 1

        if modalidad[0] == 'LA COM':
            return veintiuno_com(cartas)
        else:
            return veintiuno_vs(cartas)

def veintiuno_com(cartas):

    sumatoria = [0, 0]
    perfil = random.randint(1, 4)

    print(f"\n===== PERFIL DE LA COM: {perfil} =====\n")

    while True:

        if cartas[0][-1] == None:
            break

        sumatoria[0] = suma_cartas(cartas[0], 'LA COM')

        if sumatoria[0] > 21:

            print(f"\n===== SUMATORIA DE LA COM =====")
            print(f"{Fore.YELLOW}-> {sumatoria[0]}{Fore.RESET}\n")

            return fin_21(pierde='LA COM', motivo=0)

        cartas[0] += [jugar_com(perfil, sumatoria[0])]

        if cartas[0][-1] != None:

            print(f"LA COM ha solicitado una carta\n")
            time.sleep(1)
            print("...\n")
            time.sleep(1)
            print(f"LA COM ha obtenido una carta con un valor de {cartas[0][-1]}\n")
            time.sleep(3)

        else:
            print(f"LA COM ha pasado el turno\n")
            time.sleep(3)

    return jugar_casa(cartas, modalidad='LA COM')


def jugar_com(perfil, sumatoria):

    if perfil == 1:

        if sumatoria in range(0, 19):
            return repartir_cartas(1)
        
        elif sumatoria in range(19, 21):

            coin = random.randint(0, 1)

            if coin == 1:
                return repartir_cartas(1)
            
        return None

    elif perfil == 2:

        if sumatoria in range(0, 16):
            return repartir_cartas(1)
                    
        return None

    elif perfil == 3:

        if sumatoria in range(0, 16):
            return repartir_cartas(1)
        
        elif sumatoria in range(16, 20):

            coin = random.randint(0, 1)

            if coin == 1:
                return repartir_cartas(1)
            
        return None

    else: #perfil == 4:

        return repartir_cartas(1)
    
def veintiuno_vs(cartas):

    print(f"\n===== JUEGA J1 =====\n")
    time.sleep(3)

    while True:

        sumatoria = suma_cartas(cartas[0], 'J1')

        if sumatoria > 21:

            print(f"\n===== SUMATORIA DE J1 =====")
            print(f"{Fore.YELLOW}-> {sumatoria}{Fore.RESET}\n")
            time.sleep(1)

            return fin_21(pierde='J1', motivo=0)

        print(f"\n===== SUMATORIA DE J1 =====")
        print(f"{Fore.YELLOW}-> {sumatoria}{Fore.RESET}\n")

        print("Elige una acción:\n")
        time.sleep(1)
        print("1. Tomar una Carta")
        time.sleep(1)
        print("2. Pasar el Turno")

        acción = input(f"\n{Fore.YELLOW}¿Qué deseas hacer? : {Fore.RESET}")

        if acción == "1":
            cartas[0] += [repartir_cartas(1)]

            print(f"J1 ha solicitado una carta\n")
            time.sleep(1)
            print("...\n")
            time.sleep(1)
            print(f"J1 ha obtenido una carta con un valor de {cartas[0][-1]}\n")
            time.sleep(3)


        elif acción == "2":
            break

        else:
            print("Debes escoger una opción valida!\n")
            continue

    return jugar_casa(cartas, modalidad='J1')

    

def jugar_casa(cartas, modalidad):
    
    print(f"\n===== JUEGA LA CASA =====\n")
    time.sleep(3)

    while True:

        sumatoria = suma_cartas(cartas[1], 'LA CASA')

        if sumatoria > 21:

            print(f"\n===== SUMATORIA DE LA CASA =====")
            print(f"{Fore.YELLOW}-> {sumatoria}{Fore.RESET}\n")
            time.sleep(1)

            return fin_21(pierde='LA CASA', motivo=0)

        print(f"\n===== SUMATORIA DE LA CASA =====")
        print(f"{Fore.YELLOW}-> {sumatoria}{Fore.RESET}\n")

        print("Elige una acción:\n")
        time.sleep(1)
        print("1. Tomar una Carta")
        time.sleep(1)
        print("2. Pasar el Turno")

        acción = input(f"\n{Fore.YELLOW}¿Qué deseas hacer? : {Fore.RESET}")

        if acción == "1":
            cartas[1] += [repartir_cartas(1)]

            print(f"LA CASA ha tomado una carta\n")
            time.sleep(1)
            print("...\n")
            time.sleep(1)
            print(f"LA CASA ha obtenido una carta con un valor de {cartas[1][-1]}\n")
            time.sleep(3)


        elif acción == "2":
            break

        else:
            print("Debes escoger una opción valida!\n")
            continue

    return determinar_ganador(cartas, modalidad)


def determinar_ganador(cartas, modalidad):

    sumatoria = [0 ,0]
    sumatoria[0] += suma_cartas(cartas[0], 'LA CASA')
    sumatoria[1] += suma_cartas(cartas[1], 'NO LA CASA')

    if sumatoria[0] > sumatoria[1]:
        return fin_21(pierde='LA CASA', motivo=1, cartas=cartas)
    else:
        return fin_21(pierde=modalidad, motivo=1, cartas=cartas)

    

def fin_21(pierde, motivo, cartas):

    if motivo == 0:
        motivo = "La suma de sus cartas excede 21"
    elif motivo == 1:
        motivo = "La suma de sus cartas es menor"
    elif motivo == 2:
        motivo = "La primera carta de LA COM fué un 5 de rombos :P"

    print(f"\n¡Ha perdido {pierde}! {motivo}")

    while True:

        acción = input("\n¿Deseas Jugar otra vez? (s/n)")

        if acción == 'S' or 's':

            print("\n1. Un Jugador (V.S. COM.)")
            time.sleep(1)
            print("2. Dos Jugadores")
            time.sleep(1)
            acción = input("\nElige una Modalidad:")

            if acción == '1':
                return veintiuno_main(["LA COM", "LA CASA"])
            
        elif acción == 'N' or 'n':

            print("\nVolverás al Menú Principal")
            time.sleep(3)
            return menu_principal



def suma_cartas(cartas, modalidad):

    sumatoria = [0, 0]

    if modalidad == 'LA COM':
        index = 0
    else:
        index = 1

            
    for i in range(len(cartas)):

        if cartas[i] == None:
            break
        elif cartas[i] == 'AS' and index != 0:

            j = 0    
            while j == 0:
                    
                respuesta = input("\nHay un As! Quieres contarlo como 1 o como 11? (1/11): ")

                if respuesta == "1":
                    cartas[i] = 1
                    j +=  1
                elif respuesta == "11":
                    cartas[i] = 11
                    j += 1
                else:
                    print("Respuesta no válida. Por favor, ingresa 1 o 11.")

        elif cartas[i] == 'AS' and index == 0:

            coin = random.randint(0, 1)

            if coin == 0:
                cartas[i] = 1
            else:
                cartas[i] = 11
                


        sumatoria[index] += cartas[i]

    return sumatoria[index]







# ---------------------- EXPERIMENTAL ----------------------


menu_principal()

