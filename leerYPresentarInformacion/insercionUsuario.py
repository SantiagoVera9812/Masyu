from leerYPresentarInformacion import utilidades
from logicaMasyu import listaAdyecencia
from logicaMasyu.constantes import Constantes

def insertar_elementos(fila, columna, matriz, lista_nodo):
    fila = int(fila) - 1  # Convertir fila a entero
    columna = int(columna) - 1
    if 0 <= fila < len(matriz) and 0 <= columna < len(matriz):
        if matriz[fila][columna] != 0:
            print("Ya se encuentra un elemento en esa posición")
        else:
            
            matriz[fila][columna] = 7
            
            lista_adyacencia = listaAdyecencia.matriz_a_lista_de_adyacencia(matriz)
            print("asignando valores")
            try:
             listaAdyecencia.asignar_valor_nodo(matriz, fila, columna, lista_adyacencia, lista_nodo)
            except Exception as e:
             print("Error:", e)
            print("procesar matriz")
            listaAdyecencia.procesar_matriz(matriz,lista_nodo)
            print("mostrar matriz")
            utilidades.mostrar_matriz_ascii(matriz)
    else:
        print("Argumentos numéricos no válidos")

def editar_elemento(fila,columna,nuevoValor,matriz,lista_nodo):
    NO_VECINOS = Constantes.NO_VECINOS
    ESQUINA = Constantes.ESQUINA
    AL_LADO = Constantes.AL_LADO
    VERTICAL = Constantes.VERTICAL
    fila = int(fila) - 1  # Convertir fila a entero
    columna = int(columna) - 1
    nuevoValor = int(nuevoValor)
    if 0 <= fila < len(matriz) and 0 <= columna < len(matriz):
        
            if(matriz[fila][columna] not in [NO_VECINOS,ESQUINA,AL_LADO,VERTICAL]):
              print("No existe un elemento en el lugar propuesto")
              print("Valor existente:", matriz[fila][columna])
            else:
                if(nuevoValor not in [NO_VECINOS,ESQUINA,AL_LADO,VERTICAL]):
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