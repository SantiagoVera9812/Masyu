from logicaMasyu import constantes
from collections import OrderedDict
from logicaMasyu import listaAdyecencia

def asignar_valor_nodo(matriz, fila, columna, lista_adyacencia, lista_nodo):
    tiene_vecino_vertical = False
    tiene_vecino_horizontal = False

    # Contadores para revisar si hay mas de un vecino horizontales o verticales
    contador_horizontal = 0
    contador_vertical = 0

    # Verificar si el nodo tiene vecinos
    if (fila, columna) in lista_adyacencia:
        vecinos = lista_adyacencia[(fila, columna)]
        
        # Verificar si tiene vecinos verticales u horizontales
        print("Vecinos:", vecinos)  # Imprimir los vecinos para depuración
        for vecino, _ in vecinos:
            if vecino[0] == fila:  # Vecino en la misma fila, es horizontal
                if vecino not in lista_nodo: 
                 print("No esta en lista nodo") # Verificar si el vecino está en lista_nodo
                 tiene_vecino_horizontal = True
                 contador_horizontal += 1
            if vecino[1] == columna: 
                print("No esta en lista nodo")  # Vecino en la misma columna, es vertical
                if vecino not in lista_nodo:
                 print("No esta en lista nodo")   # Verificar si el vecino está en lista_nodo
                 tiene_vecino_vertical = True
                 contador_vertical += 1
    
    # Imprimir los valores de los índices para depuración
    print("Fila:", fila)
    print("Columna:", columna)

    si_esquina = False
    con_vertical = True
    con_horizontal = True

# Verificar si el nodo es una esquina
    if tiene_vecino_horizontal and tiene_vecino_vertical:
     si_esquina = True

# Asignar el valor correspondiente basado en los vecinos
    if tiene_vecino_horizontal and tiene_vecino_vertical and contador_horizontal <= 1 and contador_vertical <= 1:
     matriz[fila][columna] = constantes.Constantes.ESQUINA  # Vecino vertical y horizontal
    elif tiene_vecino_horizontal and contador_horizontal >= 1:
     if not si_esquina:
        matriz[fila][columna] = constantes.Constantes.AL_LADO  # Vecino horizontal
     else:
        con_horizontal = False
    elif tiene_vecino_vertical and contador_vertical >= 1:
     if not si_esquina:
        matriz[fila][columna] = constantes.Constantes.VERTICAL  # Vecino vertical
     else:
        con_vertical = False

# Ajustar si el nodo debe ser AL_LADO o VERTICAL
    if si_esquina:
     if not con_vertical:
        matriz[fila][columna] = constantes.Constantes.AL_LADO
     if not con_horizontal:
        matriz[fila][columna] = constantes.Constantes.VERTICAL
    
    if (fila,columna) not in lista_nodo and matriz[fila][columna] == 4:
     print("ver en esquina")
     es_esquina(matriz,fila,columna,lista_adyacencia,lista_nodo)

def es_esquina(matriz, fila, columna, lista_adyacencia, lista_nodo):
    # Obtener el tamaño de la matriz
    num_filas = len(matriz)
    num_columnas = len(matriz[0])

    # Contadores para los vecinos en el rango correcto
    contador_horizontal = 0
    contador_vertical = 0

    # Verificar si el nodo actual está en el rango correcto
    if matriz[fila][columna] in [3, 4, 5, 6]:
        # Verificar los vecinos en el rango correcto
        if (fila - 1, columna) in lista_adyacencia and (fila - 1, columna) not in lista_nodo:
            print("ver en esquina 1")
            matriz[fila][columna] = constantes.Constantes.UP_RIGHT
            contador_vertical += 1
        if (fila + 1, columna) in lista_adyacencia and matriz[fila + 1][columna] in [3, 5, 6] and (fila + 1, columna) not in lista_nodo:
            matriz[fila][columna] = constantes.Constantes.RIGHT_DOWN
            print("ver en esquina 2")
            contador_vertical += 1
        if (fila, columna - 1) in lista_adyacencia and matriz[fila][columna - 1] in [3, 5, 6]  and (fila, columna - 1) not in lista_nodo:
            matriz[fila][columna] = constantes.Constantes.DOWN_LEFT
            print("ver en esquina 3")
            contador_horizontal += 1
        if (fila, columna + 1) in lista_adyacencia and matriz[fila][columna + 1] in [3, 5, 6] and (fila, columna + 1) not in lista_nodo:
            matriz[fila][columna] = constantes.Constantes.LEFT_UP
            print("ver en esquina 4") 
            contador_horizontal += 1

    # El nodo es una esquina si hay un vecino horizontal y un vecino vertical en el rango correcto
    if(contador_horizontal >= 1 and contador_vertical >= 1):
       print("el nodo es una esquina") 
       

def procesar_matriz(matriz,lista_nodo):
    # Recorre cada fila y columna de la matriz
    print("procesando matriz")
    lista_adyacencia = listaAdyecencia.matriz_a_lista_de_adyacencia(matriz)
    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            if matriz[fila][columna] not in [0, 1, 2] and matriz[fila][columna] not in lista_nodo:
            # Convierte la matriz en lista de adyacencia
             asignar_valor_nodo(matriz, fila, columna)