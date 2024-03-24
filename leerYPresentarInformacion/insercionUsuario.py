from leerYPresentarInformacion import utilidades

def insertar_elementos(fila,columna,matriz):
    fila = int(fila) - 1 # Convertir fila a entero
    columna = int(columna) - 1
    if 0 <= fila < len(matriz) and 0 <= columna < len(matriz):
     if matriz[fila][columna] != 0:
        print("Ya se encuentra un elemento en esa posicion")
     else:
        matriz[fila][columna]=3
    else:
       print("argumentos numericos no validos")
    utilidades.mostrar_matriz_ascii(matriz)

def salir(ejecutar_bucle):
    if(ejecutar_bucle):
       ejecutar_bucle = False
    return ejecutar_bucle

def reiniciar(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == 3 or matriz[i][j] == 4:
                matriz[i][j] = 0
    utilidades.mostrar_matriz_ascii(matriz)