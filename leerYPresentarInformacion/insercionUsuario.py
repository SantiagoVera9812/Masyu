from leerYPresentarInformacion import utilidades
from logicaMasyu import listaAdyecencia

def insertar_elementos(fila, columna, matriz):
    fila = int(fila) - 1  # Convertir fila a entero
    columna = int(columna) - 1
    if 0 <= fila < len(matriz) and 0 <= columna < len(matriz):
        if matriz[fila][columna] != 0:
            print("Ya se encuentra un elemento en esa posición")
        else:
            matriz[fila][columna] = 7
            lista_adyacencia = listaAdyecencia.matriz_a_lista_de_adyacencia(matriz)
            print(lista_adyacencia)
            listaAdyecencia.asignar_valor_nodo(matriz, fila, columna, lista_adyacencia)
            utilidades.mostrar_matriz_ascii(matriz)
            listaAdyecencia.procesar_matriz(matriz)
            utilidades.mostrar_matriz_ascii(matriz)
            
    else:
        print("Argumentos numéricos no válidos")


def salir(ejecutar_bucle):
    if(ejecutar_bucle):
       ejecutar_bucle = False
    return ejecutar_bucle

def reiniciar(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] not in [0, 1, 2]:
                matriz[i][j] = 0
    utilidades.mostrar_matriz_ascii(matriz)