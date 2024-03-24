from leerYPresentarInformacion import utilidades

def insertar_elementos(fila,columna,matriz):
    fila = int(fila) - 1 # Convertir fila a entero
    columna = int(columna) - 1
    if 0 <= fila < len(matriz) and 0 <= columna < len(matriz):
     matriz[fila][columna]=3
    else:
       print("argumentos numericos no validos")
    utilidades.mostrar_matriz_ascii(matriz)

def salir(ejecutar_bucle):
    if(ejecutar_bucle):
       ejecutar_bucle = False
    return ejecutar_bucle