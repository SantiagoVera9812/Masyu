from leerYPresentarInformacion import utilidades
from logicaMasyu import listaAdyecencia
from logicaMasyu.constantes import Constantes


def insertar_elementos(fila, columna, matriz):
    fila = int(fila) - 1  # Convertir fila a entero
    columna = int(columna) - 1
    if 0 <= fila < len(matriz) and 0 <= columna < len(matriz[fila]):
        if matriz[fila][columna] != 0:
            print("Ya se encuentra un elemento en esa posición")
        else:
            
            print("asignando valores")
            try:
             
             listaAdyecencia.insertarNumero11(fila,columna,matriz)
            except Exception as e:
             print("Error:", e)
            
            print("mostrar matriz")
            utilidades.mostrar_matriz_ascii(matriz)
    else:
        print("Argumentos numéricos no válidos")

def editar_elemento(fila,columna,nuevoValor,matriz,lista_nodo):
    NO_VECINOS = Constantes.NO_VECINOS
    ESQUINA = Constantes.ESQUINA
    AL_LADO = Constantes.AL_LADO
    VERTICAL = Constantes.VERTICAL
    DOWN_LEFT = Constantes.DOWN_LEFT
    RIGHT_DOWN = Constantes.RIGHT_DOWN
    LEFT_UP = Constantes.LEFT_UP
    UP_RIGHT = Constantes.UP_RIGHT
    fila = int(fila) - 1  # Convertir fila a entero
    columna = int(columna) - 1
    nuevoValor = int(nuevoValor)
    if 0 <= fila < len(matriz) and 0 <= columna < len(matriz):
        
            if(matriz[fila][columna] not in [NO_VECINOS,ESQUINA,AL_LADO,VERTICAL, DOWN_LEFT, LEFT_UP,RIGHT_DOWN,UP_RIGHT]):
              print("No existe un elemento en el lugar propuesto")
              print("Valor existente:", matriz[fila][columna])
            else:
                if(nuevoValor not in [NO_VECINOS,ESQUINA,AL_LADO,VERTICAL, DOWN_LEFT, LEFT_UP,RIGHT_DOWN,UP_RIGHT]):
                    print("Nuevo valor no valido")
                else:
                    matriz[fila][columna] = nuevoValor
                    lista_nodo.append((fila, columna)) 
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