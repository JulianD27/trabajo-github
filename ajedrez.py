import random

# Definición de las piezas
PIEZAS = ("P", "T", "A", "C", "D", "R", "K")
VALORES = {"P": 1, "T": 3, "A": 3, "C": 5, "D": 9, "R": 0, "K": 0}

# Definición del tablero
TABLERO = [[0 for i in range(8)] for j in range(8)]

# Función para colocar las piezas en el tablero inicial
def colocar_piezas():
  for i in range(8):
    TABLERO[1][i] = PIEZAS[0]
    TABLERO[6][i] = PIEZAS[0]
  TABLERO[0][0] = TABLERO[0][7] = PIEZAS[1]
  TABLERO[7][0] = TABLERO[7][7] = PIEZAS[1]
  TABLERO[0][1] = TABLERO[0][6] = PIEZAS[2]
  TABLERO[7][1] = TABLERO[7][6] = PIEZAS[2]
  TABLERO[0][2] = TABLERO[0][5] = PIEZAS[3]
  TABLERO[7][2] = TABLERO[7][5] = PIEZAS[3]
  TABLERO[0][3] = PIEZAS[4]
  TABLERO[7][4] = PIEZAS[4]
  TABLERO[0][4] = PIEZAS[5]
  TABLERO[7][4] = PIEZAS[6]

# Función para imprimir el tablero
def imprimir_tablero():
  for i in range(8):
    for j in range(8):
      print(TABLERO[i][j], end=" ")
    print()

# Función para mover una pieza
def mover_pieza(origen, destino):
  if TABLERO[destino[0]][destino[1]] != 0:
    return False
  TABLERO[destino[0]][destino[1]] = TABLERO[origen[0]][origen[1]]
  TABLERO[origen[0]][origen[1]] = 0
  return True

# Función para jugar una partida
def jugar_partida():
  colocar_piezas()
  while True:
    # Obtener el movimiento del jugador
    origen = input("Ingrese la posición de la pieza a mover (fila, columna): ")
    destino = input("Ingrese la posición de destino (fila, columna): ")
    origen = (int(origen[0]) - 1, int(origen[2]) - 1)
    destino = (int(destino[0]) - 1, int(destino[2]) - 1)

    # Validar el movimiento
    if not mover_pieza(origen, destino):
      print("Movimiento inválido.")
      continue

    # Chequear si el jugador ha ganado
    if TABLERO[destino[0]][destino[1]] == PIEZAS[6] and destino[0] == 0:
      print("¡Felicidades! Has ganado.")
      break

    # Generar un movimiento aleatorio para la computadora
    while True:
      origen = (random.randint(0, 7), random.randint(0, 7))
      destino = (random.randint(0, 7), random.randint(0, 7))
      if mover_pieza(origen, destino):
        break

    # Chequear si la computadora ha ganado
    if TABLERO[destino[0]][destino[1]] == PIEZAS[6] and destino[0] == 7:
      print("Lo siento, has perdido.")
      break

    # Imprimir el tablero
    imprimir_tablero()

# Iniciar la partida
jugar_partida()
