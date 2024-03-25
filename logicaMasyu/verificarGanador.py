from logicaMasyu.constantes import Constantes
from logicaMasyu.constantes import Direcciones

NO_VECINOS = Constantes.NO_VECINOS #3
ESQUINA = Constantes.ESQUINA  #4
AL_LADO = Constantes.AL_LADO #5
VERTICAL = Constantes.VERTICAL #6

ARRIBA = Direcciones.ARRIBA
ABAJO = Direcciones.ABAJO
IZQUIERDA = Direcciones.IZQUIERDA
DERECHA = Direcciones.DERECHA

def verificar_vecinos_uno(matriz, fila, columna, lista_adyacencia):
    # Obtener el tamaño de la matriz
    num_filas = len(matriz)
    num_columnas = len(matriz[0])

    # Contadores para los vecinos en el rango correcto
    contador_vertical = 0
    contador_horizontal = 0

    # Verificar si el nodo actual es un valor de 1
    if matriz[fila][columna] == 1:
        # Verificar los vecinos en el rango correcto
        if (fila - 1, columna) in lista_adyacencia and matriz[fila - 1][columna] == 1:
            contador_vertical += 1
        if (fila + 1, columna) in lista_adyacencia and matriz[fila + 1][columna] == 1:
            contador_vertical += 1
        if (fila, columna - 1) in lista_adyacencia and matriz[fila][columna - 1] == 1:
            contador_horizontal += 1
        if (fila, columna + 1) in lista_adyacencia and matriz[fila][columna + 1] == 1:
            contador_horizontal += 1

    # Devolver True si tiene vecinos en horizontal y vertical
    return (contador_vertical >= 2 and contador_horizontal <= 0) or (contador_vertical <= 0 and contador_horizontal >= 2)

def verificar_vecinos_dos(matriz, fila, columna, lista_adyacencia):
    # Obtener el tamaño de la matriz
    num_filas = len(matriz)
    num_columnas = len(matriz[0])

    # Contadores para los vecinos en el rango correcto
    contador_horizontal = 0
    contador_vertical = 0

    # Verificar si el nodo actual está en el rango correcto
    if matriz[fila][columna] == 2:
        # Verificar los vecinos en el rango correcto
        if (fila - 1, columna) in lista_adyacencia and matriz[fila - 1][columna] in [3, 4, 5, 6]:
            contador_vertical += 1
        if (fila + 1, columna) in lista_adyacencia and matriz[fila + 1][columna] in [3, 4, 5, 6]:
            contador_vertical += 1
        if (fila, columna - 1) in lista_adyacencia and matriz[fila][columna - 1] in [3, 4, 5, 6]:
            contador_horizontal += 1
        if (fila, columna + 1) in lista_adyacencia and matriz[fila][columna + 1] in [3, 4, 5, 6]:
            contador_horizontal += 1

    # El nodo es una esquina si hay un vecino horizontal y un vecino vertical en el rango correcto
    return contador_horizontal >= 1 and contador_vertical >= 1

def obtener_nueva_direccion(peso, direccion_actual):
    return {
        ESQUINA: {
            DERECHA: ARRIBA,
            ABAJO: IZQUIERDA,
            IZQUIERDA: ABAJO,
            ARRIBA: DERECHA
        },
        AL_LADO: {DERECHA: DERECHA, IZQUIERDA: IZQUIERDA}.get(direccion_actual, DERECHA),
        VERTICAL: {ARRIBA: ARRIBA, ABAJO: ABAJO}.get(direccion_actual, ARRIBA)
    }.get(peso, direccion_actual)

