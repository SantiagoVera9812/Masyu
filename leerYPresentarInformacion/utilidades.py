import sys
import matplotlib.pyplot as plt
from logicaMasyu import constantes
from logicaMasyu import listaAdyecencia

def leer_archivo(input_file):
    try:
        with open(input_file, 'r') as f:
            # Lee el primer número de la primera línea para obtener filas y columnas
            rows_cols = int(f.readline().strip())
            matriz = [[0] * rows_cols for _ in range(rows_cols)]  # Crea una matriz cuadrada de ceros

            for line in f:
                if not line.strip():
                    continue
                elements = list(map(int, line.strip().split(',')))
                matriz[elements[0] - 1][elements[1] - 1] = elements[2]  # Asigna el valor en la posición correspondiente

        return matriz
    except FileNotFoundError:
        print("El archivo especificado no existe.")
        sys.exit(1)
    except Exception as e:
        print("Ocurrió un error:", e)
        sys.exit(1)

def mostrar_matriz_ascii(matriz):
    # Funciones lambda para definir la representación entendida por la linea de comando y el usuario de cada elemento
    #Un punto representara un lugar en donde el jugador no ha puesto nada, un 0 representara las blancas, y un negro representara las negras
    get_ascii = lambda x: ' . ' if x == constantes.Constantes.NADA else (' O ' if x == constantes.Constantes.BLANCO else (' X ' if x == constantes.Constantes.NEGRO else (' - ' if x == constantes.Constantes.NO_VECINOS else (' / ' if x == constantes.Constantes.ESQUINA else ('---' if x == constantes.Constantes.AL_LADO else ' | ')))))


    for fila in matriz:
        # Mapea cada elemento de la fila a su representación usando la función lambda
        fila_ascii = ''.join(map(get_ascii, fila))
        print(fila_ascii)

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

    
def obtener_primera_ficha(matriz, lista_adyacencia):
    lista_adyacencia = listaAdyecencia.matriz_a_lista_de_adyacencia(matriz)
    for nodo, vecinos in lista_adyacencia.items():
        for vecino, peso in vecinos:
            if peso in [1, 2]:
                print(nodo)
                print(peso)
                return nodo, peso
        else:
            continue
    # Si no se encontró ningún nodo con peso 1 o 2, devolver el primer nodo con su peso
    primer_nodo = list(lista_adyacencia.keys())[0]
    peso_primer_nodo = lista_adyacencia[primer_nodo][0][1]
    print("No se encontró ningún nodo con peso 1 o 2. Devolviendo el primer nodo:", primer_nodo, "con peso:", peso_primer_nodo)
    return primer_nodo, peso_primer_nodo

def eliminar_nodo_y_vecinos(fila, columna, lista_adyacencia):
    fila = int(fila) - 1  # Convertir fila a entero
    columna = int(columna) - 1
    lista_adyacencia = listaAdyecencia.matriz_a_lista_de_adyacencia(matriz)

    
    nodo = (fila, columna)

    # Eliminar el nodo de la lista de adyacencia
    if nodo in lista_adyacencia:
        print("Nodo en la lista de adyacencia")
        eliminar_nodo_y_vecinos_matriz(fila,columna,matriz)
        del lista_adyacencia[nodo]
    else:
        print("Nodo no encontrado:", nodo)
        return  # Salir de la función si el nodo no se encuentra
    
    # Eliminar el nodo de la lista de vecinos de otros nodos
    for vecinos in lista_adyacencia.values():
        vecinos[:] = [vecino for vecino in vecinos if vecino[0] != nodo]

    return lista_adyacencia

def eliminar_nodo_y_vecinos_matriz(fila, columna, matriz, lista_adyacencia):
    fila = int(fila) - 1  # Convertir fila a entero
    columna = int(columna) - 1
    lista_adyacencia = listaAdyecencia.matriz_a_lista_de_adyacencia(matriz)

    nodo = (fila, columna)

    # Eliminar el nodo de la lista de adyacencia
    if nodo in lista_adyacencia:
        print("Nodo en la lista de adyacencia")
        del lista_adyacencia[nodo]
    else:
        print("Nodo no encontrado:", nodo)
        return  # Salir de la función si el nodo no se encuentra
    
    # Eliminar el nodo de la lista de vecinos de otros nodos
    for vecinos in lista_adyacencia.values():
        vecinos[:] = [vecino for vecino in vecinos if vecino[0] != nodo]

    # Eliminar el valor correspondiente en la matriz
    matriz[fila][columna] = 0

    return lista_adyacencia



def agregar_a_nodos_por_ignorar(filas, columnas, matriz, lista_nodos):
    fila = int(filas) - 1  # Convertir fila a entero
    columna = int(columnas) - 1

    # Verificar si las dimensiones son válidas

    # Crear nodos con pesos
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if fila == i and columna == j:
                print("Se encontro el nodo")
                peso = matriz[i][j] if i < len(matriz) and j < len(matriz[0]) else None
                nodo = (i, j, peso)
                lista_nodos.append(nodo)

    # Imprimir los nodos creados
    print("Nodos creados con éxito:")
    for nodo in lista_nodos:
        print(nodo)

def imprimir_lista_nodos(lista_nodo):
    print("Lista de nodos:")
    for nodo in lista_nodo:
        print("Fila:", nodo[0] + 1, "Columna:", nodo[1] + 1)

