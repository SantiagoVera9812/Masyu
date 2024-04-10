from logicaMasyu import constantes
from collections import OrderedDict



left_dir = {8, 9, 5, 1, 2}  # Constantes.RIGHT_DOWN, Constantes.DOWN_LEFT, Constantes.AL_LADO
right_dir = {7, 10, 5, 1, 2}  # Constantes.UP_RIGHT, Constantes.LEFT_UP, Constantes.AL_LADO
up_dir = {9, 10, 6, 1, 2}  # Constantes.DOWN_LEFT, Constantes.LEFT_UP, Constantes.VERTICAL
down_dir = {7, 8, 6, 1, 2}
piezas = {0,1,2}

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

def ubicacion_nodo(matriz, fila_central, columna_central, left_dir, right_dir, up_dir, down_dir):
    num_filas = len(matriz)
    num_columnas = len(matriz[0])
    
    nodos = {
        "Arriba": (fila_central - 1, columna_central),
        "Abajo": (fila_central + 1, columna_central),
        "Izquierda": (fila_central, columna_central - 1),
        "Derecha": (fila_central, columna_central + 1)
    }
    
    vecinos = OrderedDict()  
    vecinos_agregados = 0
    for direccion, (fila, columna) in nodos.items():
        if 0 <= fila < num_filas and 0 <= columna < num_columnas:
            if matriz[fila][columna] is not None and (direccion == "Arriba" and matriz[fila][columna] in down_dir or matriz[fila][columna] > 10 and vecinos_agregados < 2):
                vecinos[direccion] = matriz[fila][columna]
                vecinos_agregados += 1
            elif matriz[fila][columna] is not None and (direccion == "Abajo" and matriz[fila][columna] in up_dir or matriz[fila][columna] > 10 and vecinos_agregados < 2):
                vecinos[direccion] = matriz[fila][columna]
                vecinos_agregados += 1
            elif matriz[fila][columna] is not None and (direccion == "Izquierda" and matriz[fila][columna] in right_dir or matriz[fila][columna] > 10 and vecinos_agregados < 2):
                vecinos[direccion] = matriz[fila][columna]
                vecinos_agregados += 1
            elif matriz[fila][columna] is not None and (direccion == "Derecha" and matriz[fila][columna] in left_dir or matriz[fila][columna] > 10 and vecinos_agregados < 2):
                vecinos[direccion] = matriz[fila][columna]
                vecinos_agregados += 1
    
    return vecinos

def imprimir_vecinos(matriz, fila_central, columna_central, left_dir, right_dir, up_dir, down_dir):
    num_filas = len(matriz)
    num_columnas = len(matriz[0])
    
    nodos = {
        "Arriba": (fila_central - 1, columna_central),
        "Abajo": (fila_central + 1, columna_central),
        "Izquierda": (fila_central, columna_central - 1),
        "Derecha": (fila_central, columna_central + 1)
    }
    
    vecinos = OrderedDict()  
    vecinos_agregados = 0
    for direccion, (fila, columna) in nodos.items():
        if 0 <= fila < num_filas and 0 <= columna < num_columnas:
            if matriz[fila][columna] is not None and (direccion == "Arriba" and matriz[fila][columna] not in piezas or matriz[fila][columna] > 10 and vecinos_agregados < 2):
                vecinos[direccion] = (fila, columna)
                vecinos_agregados += 1
            elif matriz[fila][columna] is not None and (direccion == "Abajo" and matriz[fila][columna] not in piezas or matriz[fila][columna] > 10 and vecinos_agregados < 2):
                vecinos[direccion] = (fila, columna)
                vecinos_agregados += 1
            elif matriz[fila][columna] is not None and (direccion == "Izquierda" and matriz[fila][columna] not in piezas or matriz[fila][columna] > 10 and vecinos_agregados < 2):
                vecinos[direccion] = (fila, columna)
                vecinos_agregados += 1
            elif matriz[fila][columna] is not None and (direccion == "Derecha" and matriz[fila][columna] not in piezas or matriz[fila][columna] > 10 and vecinos_agregados < 2):
                vecinos[direccion] = (fila, columna)
                vecinos_agregados += 1
    
    return vecinos
 
def asignar_valor(vecinos):
    if len(vecinos) == 1:
        if "Arriba" in vecinos or "Abajo" in vecinos:
            return 6
        elif "Izquierda" in vecinos or "Derecha" in vecinos:
            return 5
    elif len(vecinos) == 2:
        if "Arriba" in vecinos and "Abajo" in vecinos:
            return 6
        if "Izquierda" in vecinos and "Derecha" in vecinos:
            return 5
        if "Arriba" in vecinos and "Derecha" in vecinos:
            return 7
        elif "Derecha" in vecinos and "Abajo" in vecinos:
            return 8
        elif "Abajo" in vecinos and "Izquierda" in vecinos:
            return 9
        elif "Izquierda" in vecinos and "Arriba" in vecinos:
            return 10
    return 3 

def insertarNumero11(fila, columna, matriz):
    try:
        matriz[fila][columna] = 11

        posiciones_vecinos = imprimir_vecinos(matriz, fila, columna, left_dir, right_dir, up_dir, down_dir)
        print("Nodos vecinos:")
        for direccion, (fila_vecino, columna_vecino) in posiciones_vecinos.items():
            print(matriz[fila_vecino][columna_vecino])
        print("Filas y columnas de vecinos:")
        for direccion, (fila_vecino, columna_vecino) in posiciones_vecinos.items():
            print(matriz[fila_vecino][columna_vecino])
            print(direccion, ":", "Fila:", fila_vecino, "Columna:", columna_vecino)
            if matriz[fila_vecino][columna_vecino]:
                vecinos_del_vecinos = ubicacion_nodo(matriz, fila_vecino, columna_vecino, left_dir, right_dir, up_dir, down_dir)
                valor = asignar_valor(vecinos_del_vecinos)
                matriz[fila_vecino][columna_vecino] = valor
                print("por ubicacion_nodo del vecino:")
                print(valor)

        nuevos_vecinos = ubicacion_nodo(matriz, fila, columna, left_dir, right_dir, up_dir, down_dir)
        valor = asignar_valor(nuevos_vecinos)
        nuevos_vecinos = ubicacion_nodo(matriz, fila, columna, left_dir, right_dir, up_dir, down_dir)
        valor = asignar_valor(nuevos_vecinos)
           
        matriz[fila][columna] = valor
        print("por ubicacion_nodo directo:")
        print(valor)
    except Exception as e:
        
        print("Ocurrió un error:", e)

    
    