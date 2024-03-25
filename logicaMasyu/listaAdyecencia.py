from logicaMasyu import constantes

def matriz_a_lista_de_adyacencia(matriz):
    lista_adyacencia = {}
    filas = len(matriz)
    columnas = len(matriz[0])

    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] != 0:  # Si hay una conexión entre los nodos i y j
                nodo = (i, j)  # Nodo en la posición (i, j) de la matriz
                vecinos = []
                # Agregar los vecinos en la fila superior, inferior, izquierda y derecha
                if i > 0 and matriz[i - 1][j] != 0:
                    vecinos.append(((i - 1, j), matriz[i - 1][j]))
                if i < filas - 1 and matriz[i + 1][j] != 0:
                    vecinos.append(((i + 1, j), matriz[i + 1][j]))
                if j > 0 and matriz[i][j - 1] != 0:
                    vecinos.append(((i, j - 1), matriz[i][j - 1]))
                if j < columnas - 1 and matriz[i][j + 1] != 0:
                    vecinos.append(((i, j + 1), matriz[i][j + 1]))
                # Agregar los vecinos a la lista de adyacencia del nodo
                lista_adyacencia[nodo] = vecinos
    return lista_adyacencia


def lista_de_adyacencia_a_matriz(lista_adyacencia,matriz_og):
    # Obtener las coordenadas máximas para determinar el tamaño de la matriz
    max_fila = max(coord[0] for coord in lista_adyacencia.keys())
    max_columna = max(coord[1] for coord in lista_adyacencia.keys())

    # Inicializar la matriz con ceros
    matriz = [[0] * (max_columna + 1) for _ in range(max_fila + 1)]

    # Llenar la matriz con los valores de la lista de adyacencia
    for nodo, vecinos in lista_adyacencia.items():
        fila, columna = nodo
        matriz[fila][columna] = matriz_og[fila][columna]
        for vecino, valor in vecinos:
            fila_vecino, columna_vecino = vecino
            matriz[fila_vecino][columna_vecino] = valor

    return matriz

def asignar_valor_nodo(matriz, fila, columna, lista_adyacencia):
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
                tiene_vecino_horizontal = True
                contador_horizontal += 1
            if vecino[1] == columna:  # Vecino en la misma columna, es vertical
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
    elif tiene_vecino_horizontal and contador_horizontal >= 2:
     if not si_esquina:
        matriz[fila][columna] = constantes.Constantes.AL_LADO  # Vecino horizontal
     else:
        con_horizontal = False
    elif tiene_vecino_vertical and contador_vertical >= 2:
     if not si_esquina:
        matriz[fila][columna] = constantes.Constantes.VERTICAL  # Vecino vertical
     else:
        con_vertical = False

# Ajustar si el nodo debe ser AL_LADO o VERTICAL
    if si_esquina:
     if not con_vertical and con_horizontal:
        matriz[fila][columna] = constantes.Constantes.VERTICAL
     if not con_horizontal and not con_vertical:
        matriz[fila][columna] = constantes.Constantes.AL_LADO

def procesar_matriz(matriz):
    # Recorre cada fila y columna de la matriz

    lista_adyacencia = matriz_a_lista_de_adyacencia(matriz)
    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            if matriz[fila][columna] not in [0, 1, 2]:
            # Convierte la matriz en lista de adyacencia
             asignar_valor_nodo(matriz, fila, columna, lista_adyacencia)
            
    
    