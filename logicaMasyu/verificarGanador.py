from logicaMasyu.constantes import Constantes
from logicaMasyu.constantes import Direcciones
from leerYPresentarInformacion import utilidades
from logicaMasyu import listaAdyecencia

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


def atravesar_matriz(matriz, lista_adyacencia):
      # Obtener la posición inicial y el peso inicial
    print(lista_adyacencia)
    utilidades.mostrar_matriz(matriz)
    lista_adyacencia = listaAdyecencia.matriz_a_lista_de_adyacencia(matriz)
    posicion_inicial, peso_inicial = utilidades.obtener_primera_ficha(matriz, lista_adyacencia)

    # Obtener el tamaño de la matriz
    num_filas = len(matriz)
    num_columnas = len(matriz[0])

    # Definir la posición inicial y la dirección inicial
    fila_actual, columna_actual = posicion_inicial
    direccion_actual = "izquierda"

       # Conjunto de posiciones visitadas
    posiciones_visitadas = set()

    while 0 <= fila_actual < num_filas and 0 <= columna_actual < num_columnas:
        # Obtener el valor y peso del nodo actual
        valor_actual = matriz[fila_actual][columna_actual]

        if (fila_actual, columna_actual) in posiciones_visitadas:
            print("Se ha encontrado un bucle. Terminando la ejecución.")
            break

        print(fila_actual,columna_actual)
          # Agregar la posición actual al conjunto de posiciones visitadas
        posiciones_visitadas.add((fila_actual, columna_actual))
        
        # Determinar la nueva dirección basada en el valor actual del nodo
        if valor_actual == 3:  # No existen vecinos
            print(valor_actual)
            nueva_direccion = "No hay dirección"
            print(nueva_direccion)
            fila_actual = -1
            columna_actual = -1
        elif valor_actual == 4:  # Cambio de dirección
            print(valor_actual)
            nueva_direccion = obtener_nueva_direccion(valor_actual, direccion_actual)
            print(nueva_direccion)
        elif valor_actual == 5:
            print(valor_actual)  # Mantener la dirección horizontal
            nueva_direccion = direccion_actual
            print(nueva_direccion)
        elif valor_actual == 6:  
            print(valor_actual)# Mantener la dirección vertical
            nueva_direccion = direccion_actual
            print(nueva_direccion)
        elif valor_actual == 1:
            print(valor_actual)
            if (verificar_vecinos_uno):
                nueva_direccion = direccion_actual
                print(nueva_direccion)
        elif valor_actual == 2:
            print(valor_actual)
            if(verificar_vecinos_dos):
                nueva_direccion = obtener_nueva_direccion(valor_actual, direccion_actual)
                print(nueva_direccion)
        else:
            print("valor no valido")

    # Moverse en la nueva dirección
        fila_actual, columna_actual = moverse_en_direccion(fila_actual, columna_actual, nueva_direccion)

def moverse_en_direccion(fila_actual, columna_actual, direccion_actual):
    # Moverse en la dirección actual
    if direccion_actual == DERECHA:
        columna_actual += 1
    elif direccion_actual == IZQUIERDA:
        columna_actual -= 1
    elif direccion_actual == ARRIBA:
        fila_actual -= 1
    elif direccion_actual == ABAJO:
        fila_actual += 1
    else:
        print("No se puede continuar")

    # Devolver la nueva posición
    return fila_actual, columna_actual
