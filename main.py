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
        return lore_main()
    
    elif opción == "3":
        return cómo_jugar_main()
    
    elif opción == "4":
        return creditos()
    
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
    
    print("1. Fascista a la Fuga. (Fox and Hounds)")
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
    
    print("1. Fascista a la Fuga (Fox and Hounds)")
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

def lore_main():

    print(r'''
           .--.                   .---.
       .---|__|           .-.     |~~~|
    .--|===|--|_          |_|     |~~~|--.
    |  |===|  |'\     .---!~|  .--|   |--|
    |%%|   |  |.'\    |===| |--|%%|   |  |
    |%%|   |  |\.'\   |   | |__|  |   |  |
    |  |   |  | \  \  |===| |==|  |   |  |
    |  |   |__|  \.'\ |   |_|__|  |~~~|__|
    |  |===|--|   \.'\|===|~|--|%%|~~~|--|
    ^--^---'--^    `-'`---^-^--^--^---'--' hjw
          ''')
    
    print(f"\nBienvenidx a la sección {Fore.CYAN}«Lore»{Fore.RESET}!\n")
    time.sleep(1)

    print("1. Continuar")

    print("\nq. Volver")

    print("\nADVERTENCIA: La siguiente sección contiene bastatnte texto, puedes tardar hasta 1 minuto!\n")
    opción = input("¿Deseas continuar?")

    if opción == "1":
        return lore()
    elif opción == "q" or  opción == "Q":
        return menu_principal()
    else:
        print("Ingresa una opción válida!")
        return lore_main()
    
# -------------------------- CRÉDITOS -------------------------

def creditos():

    print(r'''
    ___________.__                   __         
    \__    ___/|  |__ _____    ____ |  | __     
      |    |   |  |  \\__  \  /    \|  |/ /     
      |    |   |   Y  \/ __ \|   |  \    <      
      |____|   |___|  (____  /___|  /__|_ \     
                    \/     \/     \/     \/     
                         _____.___.             
                         \__  |   | ____  __ __ 
                          /   |   |/  _ \|  |  
                          \____   (  <_> )  |  /
                          / ______|\____/|____/ 
                          \/                    

          ''')

    print("Este Juego corresponde a la 3ª Progra de [IC1803] Taller de Programación")
    print("A Cargo del profe Aurelio Sanabria Rodriguez")
    print("Elaborado por Johannes Méndez Flores [j.mendez.4@estudiantec.cr]" \
          "y Daniel Solano Codero [	d.solano.1@estudiantec.cr]")
    print("Gracias Por Jugar!")
    time.sleep(5)

    print("")
    input("Presiona ↵ para volver al menú principal:")
    return menu_principal()




# ------------------------- CÓMO JUGAR ------------------------

def cj_caza():

    print(Fore.LIGHTRED_EX + "TEMATICA")
    print('''
          En este juego de tablero estrategico, un fascista (la liebre) intenta escapar mientras anarquistas
          (los perros) cooperan para impedir que logre huir. El jugador representa a el bando de los anarquistas,
          mientras que la computadora toma el rol del fascista agresivo.
          ''')
    print("")
    input("Presiona ↵ para continuar")

    print(Fore.LIGHTMAGENTA_EX + "OBJETIVO")
    print('''
          Fascista: Llegar al lado opuesto de donde inicia o evitar ser bloqueado durante todo el juego.
          Anarquistas: Acorralar al fascista hasta que no pueda moverse hacia ninguna direccion.
          ''')
    print("")
    input("Presiona ↵ para continuar")

    print(Fore.RED + "TABLERO")
    print('''
          Un tablero con forma de diamante en posicion horizontal, donde las casillas se intersecan con lineas verticales,
          horizontales y diagonales.
          Los anarquistan inician en la posicion mas a la izquierda de cada fila.
          El fascista incia en la posicion mas a la derecha de la fila central.
          ''')
    print("")
    input("Presiona ↵ para continuar")

    print(Fore.BLUE + "TURNOS Y MOVIMIENTO")
    print(''''
          Se juega por turnos alternos: primero los anarquistas y luego el fascista, asi sucesivamente.
          Fascista: Puede moverse hacia cualquier direccion dentro del tablero que este vacia.
          Anarquistas: Se mueve solo un anarquista por turno y solo puede avanzar verticalmente, en diagonal y hacia adelante.
          ''')
    print("")
    input("Presiona ↵ para continuar")

    print(Fore.GREEN + "REGLAS ESPECIALES")
    print('''
          - El fascista no puede saltar sobre anarquistas.
          - Los anarquistas no pueden retroceder, por lo que deben acorralar estrategicamente.
          - Si el fascista llega a la ultima columna del tablero, el fascista gana.
          - Si queda totalmente rodeado y sin movimientos legales, pierden los autoritarismos, digo, pierde el fascista.
          ''')
    print("")
    input("Presiona ↵ para regresar al menu principal")
    return menu_principal()

def cj_veintiuno():

    print(f"{Fore.YELLOW}LAS CARTAS\n")

    print(f'''

          En esta modalidad, El maso de cartas es {Fore.YELLOW}infinito{Fore.RESET}.
          Esto significa todas las cartas son posibles cada que sloicitas tomar una nueva carta.
          En este juego, los palos de las cartas no importan, salvo en un caso especial que se denotará más adelante.
          Todas las cartas de valor tienen su mismo valor. Las cartas de figura tienen un valor de 10.
          Si tienes un AS en tu mano, este puede tener un valor de 1 u 11, el cual puedes elegir al sumar tus cartas.

          ''')
    input("Presiona ↵ para continuar")

    
    print(f"{Fore.YELLOW}EL FLUJO DE JUEGO\n")


    print(f'''

          Al comenzar el juego (y tras elegir la modlidad), a cada jugador se le entregan 2 cartas aleatorias del maso.
          Comienza juganto {Fore.LIGHTRED_EX}LA COM{Fore.RESET} o {Fore.GREEN}J1{Fore.RESET}, dependiendo de la modalidad.
          Si juega {Fore.LIGHTRED_EX}LA COM{Fore.RESET}, esta jugará de manera automática obedeciendo a un dado perfil, asignado al comenzar la partida.
          Si juega {Fore.GREEN}J1{Fore.RESET}, se sumarán sus cartas y se mostrará la suma en pantalla.
          Mientras Juege {Fore.GREEN}J1{Fore.RESET}, la persona que juege como {Fore.MAGENTA}LA CASA{Fore.RESET} no debe mirar la sumatoria de las cartas de {Fore.GREEN}J1{Fore.RESET}.
          Durante su turno, {Fore.GREEN}J1{Fore.RESET} podrá decidir si solicitar una carta o pasar su turno.
          Luego de que {Fore.GREEN}J1{Fore.RESET} o {Fore.LIGHTRED_EX}LA COM{Fore.RESET} pase su turno, jugará {Fore.MAGENTA}LA CASA{Fore.RESET}.
          Durante el turno de {Fore.MAGENTA}LA CASA{Fore.RESET}, se sumarán sus cartas y se mostrará el resultado en pantalla.
          {Fore.MAGENTA}LA CASA{Fore.RESET} podrá decidir si tomar una carta o pasar su turno.
          Una ves que {Fore.MAGENTA}LA CASA{Fore.RESET} pasa su turno, se determina el ganador.
    
          ''')
    input("Presiona ↵ para continuar")

    
    print(f"{Fore.YELLOW}¿CÓMO GANAR?\n")

    print(f'''

          Para ganar, la suma de tus cartas deberá ser lo más cercano a 21 como sea posible, pero nunca debe exceder 21.
          Salvo en casos especiales (que de detalla más adelante), el ganador se determina al finalizar el turno de {Fore.MAGENTA}LA CASA{Fore.RESET}.
          Si antes del turno de {Fore.MAGENTA}LA CASA{Fore.RESET}, la suma de las cartas de {Fore.LIGHTRED_EX}LA COM{Fore.RESET} o de {Fore.GREEN}J1{Fore.RESET} excede 21, ganará {Fore.MAGENTA}LA CASA{Fore.RESET} automáticamente.
          Si durante el turno de {Fore.MAGENTA}LA CASA{Fore.RESET}, la suma de sus cartas excede 21, ganará {Fore.LIGHTRED_EX}LA COM{Fore.RESET} o {Fore.GREEN}J1{Fore.RESET}, según la modalidad.
          Si al finalizar el turno de {Fore.MAGENTA}LA CASA{Fore.RESET}, ambos Jugadores siguen en pie, ganará el bando con el puntaje mayor.

          ''')
    input("Presiona ↵ para continuar")

    
    print(f"{Fore.YELLOW}CASOS ESPECIALES\n")

    print(f'''

          Hay varias más maneras de ganar: los casos especiales.
          Si alguno de los dos bandos tiene en total 5 cartas sin figuras y su sumatoria es menor o igual a 21, gana automáticamente.
          Por otro lado, si la primera carta otorgada a un jugador es un 5 de rombos, gana automáticamente (reglas de {Fore.MAGENTA}LA CASA{Fore.RESET}, sorry not sorry).
          Si un jugador obtiene dos ASes de cualquier palo, también ganará automáticamente.
          Por último, si un jugador obtiene tres 7 en una sola mano, ganará automáticamente por sobre cualquier otro caso especial (Jackpot 🤑).

          ''')
    input("Presiona ↵ para continuar")

    
    print('''

          Ya sabés Jugar 21! Andá jugá o leételo otra ves, mae.

          ''')
    
    input("Presiona ↵ para regresar al menu principal")
    return menu_principal()





# --------------------------- LORE ----------------------------

def lore():

    print('''

        Esta historia se remonta a años antes de los eventos transcurridos en el juego ‘carrera al futuro’ 
        y los eventos aquí descritos tienen lugar alrededor del año 202X.

          ''')
    
    input("Presiona ↵")

    print('''

        En un lugar cerca de Washington DC, varias protestas surgen ante la candidatura de un cierto político infame que, 
        tras años de gobernar los estados unidos y esparcir su desdén por la libertad colectiva y las minorías, 
        decide poner en marcha nuevamente su plan. Varios concordaban ciegamente con sus ideologías, 
        pero tras 4 años de gobierno, no cabía duda de sus verdaderas intenciones: hacerse con el dinero del pueblo 
        e incentivar un sistema que perpetuara su estadía en el poder, pasando por alto (o condenando como ‘inconstitucional’) 
        cualquier mecanismo estatal, activista, moción o demás, que le impidiera enraizar en lo profundo de la política estadounidense.

          ''')

    input("Presiona ↵")

    print('''

        En dicha protesta, un grupo de protestantes pacíficos de alianza Anarquista, liderados por 3 personas bajo los seudónimos de Max Striner, 
        Lysander Spooner y Guillermo Godwin (en honor a las figuras históricas homónimas), notan que, mientras transitaban pacíficamente 
        por la plaza donde se da la manifestación, un violento individuo comienza a atacar a los protestantes, gritando en defesa del infame político.

          ''')
    
    input("Presiona ↵")

    print('''

        Ante tal conmoción, los 3 líderes se lanzan a la defensa de las masas y deciden acorralar al violento individuo e informar a las autoridades correspondientes.
        [Acá se lleva a cabo el juego ‘Los Anarquistas y el Fascista’]

          ''')
    
    input("Presiona ↵")

    print('''

          Habiendo acorralado al fascista y tras su arresto por parte de las autoridades, la manifestación puede seguir con normalidad. 
          La manifestación es transmitida por todos los medios nacionales e incluso llega a ser noticia internacional y consiguen eliminar 
          al infame político de la lista de candidatos, ganando las elecciones una aclamada dama que promueve la diversidad, la cultura 
          y los derechos de todxs. Meses después, el día de la marcha es nombrado como el ‘Día de la resistencia’ por la ONU 
          y se convierte en un día conmemorado internacionalmente como un día para luchar en contra de la opresión y en pro de la libertad 
          y los derechos humanos universales.

          ''')
    
    input("Presiona ↵")

    print('''

          Satisfechos con sus logros, deciden rentar un casino para jugar a las cartas con sus amigos, mas, un día, una misteriosa dama 
          conocida bajo el seudónimo de ‘{Fore.LIGHTRED_EX}LA COM{Fore.RESET}’ los reta a todos a un juego de blackjack, y promete hacer una generosa donación 
          si consiguen derrotarla a ella en 4 juegos seguidos.
          [Acá se lleva a cabo el juego ‘Lo que siguió’]

          ''')
    
    input("Presiona ↵")

    print('''

          Tras varias victorias consecutivas, consiguen salir victoriosos y reciben la donación. 
          Esa tarde, todos fueron a la nave.

          ''')
    
    input("Presiona ↵")

    print('El Fin', end='')
    time.sleep(1)
    print('.', end='')
    time.sleep(1)
    print('.', end='')
    time.sleep(1)
    print('.', end='')
    time.sleep(1)
    print('?')
    time.sleep(1)

    print('Volverás al Menú principal')
    time.sleep(3)

    return menu_principal()

# ---------------------- LIEBRE Y PERROS ----------------------

def inicio_juego_caza():
    '''Funcion principal del juego'''
    print("")
    print("Bienvenido a la Liebre y los Perros de Caza.")
    time.sleep(1)
    print("En este juego tu objetivo es atrapar al fascista en fuga.")
    print("")
    time.sleep(1)
    print("Te enfrentas al fascista. (compuradora)")
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
    '''Reparte num cantidad de cartas (retorna un valor o AS)'''

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
    '''Menú principal del juego de 21'''

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
    '''inicializa el juego de 21'''

    cartas = [[],[]]

    while True:

        index = 0

        while index < 2:

            print(f"\n===== {Fore.CYAN}REPARTIENDO CARTAS A {modalidad[index]} =====\n")

            cartas[index] += [repartir_cartas(2)]
            time.sleep(2)
            print('Done!')
            time.sleep(1)

            if index == 1 and cartas[index][0] == 5:

                coin = random.randint(0, 3)
                if coin == 0:
                    return fin_21(pierde=modalidad[index], motivo=2)

            index += 1

        if modalidad[0] == 'LA COM':
            return veintiuno_com(cartas)
        else:
            return veintiuno_vs(cartas)

def veintiuno_com(cartas):
    '''determina el ciclo de juego de LA COM'''

    sumatoria = [0, 0]
    perfil = random.randint(1, 4)

    print(f"\n===== PERFIL DE {Fore.LIGHTRED_EX}LA COM{Fore.RESET}: {perfil} =====\n")

    while True:

        if cartas[0][-1] == None:
            break
        if len(cartas) >= 5:
            return fin_21(pierde='LA CASA', motivo=3)

        sumatoria[0] = suma_cartas(cartas[0], 'LA COM')

        if sumatoria[0] > 21:

            print(f"\n===== SUMATORIA DE {Fore.LIGHTRED_EX}LA COM{Fore.RESET} =====")
            print(f"{Fore.YELLOW}-> {sumatoria[0]}{Fore.RESET}\n")

            return fin_21(pierde='LA COM', motivo=0)

        cartas[0] += [jugar_com(perfil, sumatoria[0])]

        if cartas[0][-1] != None:

            print(f"{Fore.LIGHTRED_EX}LA COM{Fore.RESET} ha solicitado una carta\n")
            time.sleep(1)
            print("...\n")
            time.sleep(1)
            print(f"{Fore.LIGHTRED_EX}LA COM{Fore.RESET} ha obtenido una carta con un valor de {cartas[0][-1]}\n")
            time.sleep(3)

        else:
            print(f"LA COM ha pasado el turno\n")
            time.sleep(3)

    return jugar_casa(cartas, modalidad='LA COM')


def jugar_com(perfil, sumatoria):
    '''Determina cómo juega LA COM segun su perfil'''

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
    '''Presenta el ciclo de juego al J1 y le deja tomar acciones'''

    print(f"\n===== JUEGA {Fore.GREEN}J1{Fore.RESET} =====\n")
    time.sleep(3)

    while True:

        sumatoria = suma_cartas(cartas[0], 'J1')

        if sumatoria > 21:

            print(f"\n===== SUMATORIA DE {Fore.GREEN}J1{Fore.RESET} =====")
            print(f"{Fore.YELLOW}-> {sumatoria}{Fore.RESET}\n")
            time.sleep(1)

            return fin_21(pierde='J1', motivo=0)
        
        if len(cartas) >= 5:
            return fin_21(pierde='LA CASA', motivo=3)

        print(f"\n===== SUMATORIA DE {Fore.GREEN}J1{Fore.RESET} =====")
        print(f"{Fore.YELLOW}-> {sumatoria}{Fore.RESET}\n")

        print("Elige una acción:\n")
        time.sleep(1)
        print("1. Tomar una Carta")
        time.sleep(1)
        print("2. Pasar el Turno")

        acción = input(f"\n{Fore.YELLOW}¿Qué deseas hacer? : {Fore.RESET}")

        if acción == "1":
            cartas[0] += [repartir_cartas(1)]

            print(f"{Fore.GREEN}J1{Fore.RESET} ha solicitado una carta\n")
            time.sleep(1)
            print("...\n")
            time.sleep(1)
            print(f"{Fore.GREEN}J1{Fore.RESET} ha obtenido una carta con un valor de {cartas[0][-1]}\n")
            time.sleep(3)


        elif acción == "2":
            break

        else:
            print("Debes escoger una opción valida!\n")
            continue

    return jugar_casa(cartas, modalidad='J1')

    

def jugar_casa(cartas, modalidad):
    '''Presenta el ciclo de juego a LA CASA y le deja tomar acciones'''
    
    print(f"\n===== JUEGA {Fore.MAGENTA}LA CASA{Fore.RESET} =====\n")
    time.sleep(3)

    while True:

        sumatoria = suma_cartas(cartas[1], 'LA CASA')

        if sumatoria > 21:

            print(f"\n===== SUMATORIA DE {Fore.MAGENTA}LA CASA{Fore.RESET} =====")
            print(f"{Fore.YELLOW}-> {sumatoria}{Fore.RESET}\n")
            time.sleep(1)

            return fin_21(pierde='LA CASA', motivo=0)
        
        
        if len(cartas) >= 5:
            return fin_21(pierde='LA CASA', motivo=3)


        print(f"\n===== SUMATORIA DE {Fore.MAGENTA}LA CASA{Fore.RESET} =====")
        print(f"{Fore.YELLOW}-> {sumatoria}{Fore.RESET}\n")

        print("Elige una acción:\n")
        time.sleep(1)
        print("1. Tomar una Carta")
        time.sleep(1)
        print("2. Pasar el Turno")

        acción = input(f"\n{Fore.YELLOW}¿Qué deseas hacer? : {Fore.RESET}")

        if acción == "1":
            cartas[1] += [repartir_cartas(1)]

            print(f"{Fore.MAGENTA}LA CASA{Fore.RESET} ha tomado una carta\n")
            time.sleep(1)
            print("...\n")
            time.sleep(1)
            print(f"{Fore.MAGENTA}LA CASA{Fore.RESET} ha obtenido una carta con un valor de {cartas[1][-1]}\n")
            time.sleep(3)


        elif acción == "2":
            break

        else:
            print("Debes escoger una opción valida!\n")
            continue

    return determinar_ganador(cartas, modalidad)


def determinar_ganador(cartas, modalidad):
    '''Determina un ganador tras finalizar el turno de La CASA'''

    sumatoria = [0 ,0]
    sumatoria[0] += suma_cartas(cartas[0], 'LA CASA')
    sumatoria[1] += suma_cartas(cartas[1], 'NO LA CASA')

    if sumatoria[0] > sumatoria[1]:
        return fin_21(pierde='LA CASA', motivo=1, cartas=cartas)
    else:
        return fin_21(pierde=modalidad, motivo=1, cartas=cartas)

    

def fin_21(pierde, motivo):
    '''finaliza el juego de 21 imprimiendo el perdedor y su causa'''

    if motivo == 0:
        motivo = "La suma de sus cartas excede 21"
    elif motivo == 1:
        motivo = "La suma de sus cartas es menor que la de su oponente"
    elif motivo == 2:
        motivo = "La primera carta de su oponente fué un 5 de rombos :P"
    elif motivo == 3:
        motivo = "Su oponente obtuvo 5 cartas y su suma es 21 o menos :P"
    elif motivo == 4:
        motivo = "Su oponente obtuvo dos ASes"
    elif motivo == 5:
        motivo = "Su oponente obtuvo tres 7 🤑"

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
            elif acción == '2':
                return veintiuno_main(["J1", "LA CASA"])
            
        elif acción == 'N' or 'n':

            print("\nVolverás al Menú Principal")
            time.sleep(3)
            return menu_principal



def suma_cartas(cartas, modalidad):
    '''suma las cartas en la mano del jugador'''

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







# ---------------------- FUNCIONAL ----------------------


menu_principal()

