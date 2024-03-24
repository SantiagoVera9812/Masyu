import sys
import matplotlib.pyplot as plt
from logicaMasyu import constantes

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

    
