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
            if direccion == "Arriba" and matriz[fila][columna] in down_dir or matriz[fila][columna] > 10 and vecinos_agregados < 2:
                vecinos[direccion] = matriz[fila][columna]
                vecinos_agregados += 1
            elif direccion == "Abajo" and matriz[fila][columna] in up_dir or matriz[fila][columna] > 10 and vecinos_agregados < 2:
                vecinos[direccion] = matriz[fila][columna]
                vecinos_agregados += 1
            elif direccion == "Izquierda" and matriz[fila][columna] in right_dir or matriz[fila][columna] > 10 and vecinos_agregados < 2:
                vecinos[direccion] = matriz[fila][columna]
                vecinos_agregados += 1
            elif direccion == "Derecha" and matriz[fila][columna] in left_dir or matriz[fila][columna] > 10 and vecinos_agregados < 2:
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
            if direccion == "Arriba" and matriz[fila][columna] not in piezas or matriz[fila][columna] > 10 and vecinos_agregados < 2:
                vecinos[direccion] = (fila, columna)
                vecinos_agregados += 1
            elif direccion == "Abajo" and matriz[fila][columna] not in piezas or matriz[fila][columna] > 10 and vecinos_agregados < 2:
                vecinos[direccion] = (fila, columna)
                vecinos_agregados += 1
            elif direccion == "Izquierda" and matriz[fila][columna] not in piezas or matriz[fila][columna] > 10 and vecinos_agregados < 2:
                vecinos[direccion] = (fila, columna)
                vecinos_agregados += 1
            elif direccion == "Derecha" and matriz[fila][columna] not in piezas or matriz[fila][columna] > 10 and vecinos_agregados < 2:
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
    return None 

def insertarNumero11(fila, columna,matriz):

    fila = int(fila)   # Convertir fila a entero
    columna = int(columna) 
    matriz[fila][columna] = 11
    
    posiciones_vecinos = imprimir_vecinos(matriz,fila,columna,left_dir,right_dir,up_dir,down_dir)
    print("Nodos vecinos:")
    for direccion, (fila_vecino,columna_vecino) in posiciones_vecinos.items():
     print(matriz[fila_vecino][columna_vecino])
    print("Filas y columnas de vecinos:")
    for direccion, (fila_vecino, columna_vecino) in posiciones_vecinos.items():
        print(matriz[fila_vecino][columna_vecino])
        print(direccion, ":", "Fila:", fila_vecino, "Columna:", columna_vecino)
        if matriz[fila_vecino][columna_vecino]:
         vecinos_del_vecinos = ubicacion_nodo(matriz,fila_vecino,columna_vecino,left_dir,right_dir,up_dir,down_dir)
         valor = asignar_valor(vecinos_del_vecinos)
         matriz[fila_vecino][columna_vecino] = valor
         print("por ubicacion_nodo del vecino:")
         print(valor)

    nuevos_vecinos = ubicacion_nodo(matriz,fila,columna,left_dir,right_dir,up_dir,down_dir)
    valor = asignar_valor(nuevos_vecinos)
    matriz[fila][columna] = valor
    print("por ubicacion_nodo directo:")
    print(valor)

"""
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
    lista_adyacencia = matriz_a_lista_de_adyacencia(matriz)
    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            if matriz[fila][columna] not in [0, 1, 2] and matriz[fila][columna] not in lista_nodo:
            # Convierte la matriz en lista de adyacencia
             ubicacion_nodo(matriz, fila, columna)
 """           
    
    