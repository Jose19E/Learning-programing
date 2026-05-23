import random

# Cantidad de jugadores
jugadores = int(input("Ingrese cantidad de jugadores (2-4): "))

while jugadores < 2 or jugadores > 4:
    jugadores = int(input("Ingrese cantidad válida (2-4): "))

# Menú
print("1. Básico - 20 posiciones")
print("2. Intermedio - 30 posiciones")
print("3. Avanzado - 50 posiciones")
print("4. Experto - 100 posiciones")

nivel = int(input("Seleccione nivel: "))

# Meta según nivel
if nivel == 1:
    meta = 20
elif nivel == 2:
    meta = 30
elif nivel == 3:
    meta = 50
else:
    meta = 100

# Posiciones
j1 = 0
j2 = 0
j3 = 0
j4 = 0

# Dobles consecutivos
d1 = 0
d2 = 0
d3 = 0
d4 = 0

ganador = False

while ganador == False:

    # JUGADOR 1
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)

    print("\nJugador 1")
    print("Dados:", dado1, dado2)

    j1 = j1 + dado1 + dado2
    print("Posición:", j1)

    if dado1 == dado2:
        d1 = d1 + 1
    else:
        d1 = 0

    if d1 == 3:
        print("Jugador 1 gana por 3 dobles")
        ganador = True

    if j1 >= meta:
        print("Jugador 1 ganó")
        ganador = True

    # JUGADOR 2
    if ganador == False:

        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)

        print("\nJugador 2")
        print("Dados:", dado1, dado2)

        j2 = j2 + dado1 + dado2
        print("Posición:", j2)

        if dado1 == dado2:
            d2 = d2 + 1
        else:
            d2 = 0

        if d2 == 3:
            print("Jugador 2 gana por 3 dobles")
            ganador = True

        if j2 >= meta:
            print("Jugador 2 ganó")
            ganador = True

    # JUGADOR 3
    if jugadores >= 3 and ganador == False:

        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)

        print("\nJugador 3")
        print("Dados:", dado1, dado2)

        j3 = j3 + dado1 + dado2
        print("Posición:", j3)

        if dado1 == dado2:
            d3 = d3 + 1
        else:
            d3 = 0

        if d3 == 3:
            print("Jugador 3 gana por 3 dobles")
            ganador = True

        if j3 >= meta:
            print("Jugador 3 ganó")
            ganador = True

    # JUGADOR 4
    if jugadores == 4 and ganador == False:

        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)

        print("\nJugador 4")
        print("Dados:", dado1, dado2)

        j4 = j4 + dado1 + dado2
        print("Posición:", j4)

        if dado1 == dado2:
            d4 = d4 + 1
        else:
            d4 = 0

        if d4 == 3:
            print("Jugador 4 gana por 3 dobles")
            ganador = True

        if j4 >= meta:
            print("Jugador 4 ganó")
            ganador = True
        