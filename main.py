import sys
from leerYPresentarInformacion import utilidades
from leerYPresentarInformacion import insercionUsuario
from logicaMasyu import listaAdyecencia
from logicaMasyu import checkWin
from logicaMasyu import jugadorAutomatico
funciones = {
   "insertar_elemento": insercionUsuario.insertar_elementos,
   "salir":insercionUsuario.salir,
   "mostrar_matriz":utilidades.mostrar_matriz_ascii,
   "reiniciar":insercionUsuario.reiniciar,
   "jugador_automatico":jugadorAutomatico.jugadorAutomatico,
   "mostrar_matriz_numerica":utilidades.mostrar_matriz,
   "editar_elemento":insercionUsuario.editar_elemento,
   "obtener_primera_ficha": utilidades.obtener_primera_ficha,
   "eliminar_nodo":utilidades.eliminar_nodo_y_vecinos_matriz,
   "ignorar_nodo":utilidades.agregar_a_nodos_por_ignorar,
   "imprimir_lista_nodos":utilidades.imprimir_lista_nodos,
   "leer_matriz_de_archivo":utilidades.leer_matriz_numerica,
   "verificar_respuesta":checkWin.verificarRespuesta
}

if __name__ == "__main__":
    ## Check arguments
    if len( sys.argv ) < 2:
     print( "Usage: python3", sys.argv[ 0 ], "input_file" )
     sys.exit( 1 )

    input_file = sys.argv[1]
    matriz = utilidades.leer_archivo(input_file)
    lista_adyacencia = listaAdyecencia.matriz_a_lista_de_adyacencia(matriz)
    utilidades.mostrar_matriz_ascii(matriz)
    ejecutar_bucle = True
    lista_nodos = []

    print("Nodos creados con éxito:")
    for nodo in lista_nodos:
        print(nodo)


    while ejecutar_bucle:
     comando = input("$")
     partes = comando.split()
     nombre_del_comando = partes[0]
     argumentos = partes[1:]

     try:
      if nombre_del_comando in funciones:
            funcion = funciones[nombre_del_comando]
            if nombre_del_comando == "ignorar_nodo":  # Verificar si es la función específica
             print("se encuentra ignorar nodo")
             if len(argumentos) != 2:  # Se esperan exactamente 2 argumentos: filas y columnas
                print("Se esperan exactamente 2 argumentos: filas y columnas")
                continue
                
             filas, columnas = map(int, argumentos)  # Convertir los argumentos a enteros

            # Llamar a la función con los argumentos proporcionados
             utilidades.agregar_a_nodos_por_ignorar(filas=filas, columnas=columnas, matriz=matriz, lista_nodos=lista_nodos)

            elif nombre_del_comando ==  "leer_matriz_de_archivo":
               print("leyendo...")
               if len(argumentos) != 1:  # Se esperan exactamente 2 argumentos: filas y columnas
                print("Se esperan exactamente 1 argumento")
                continue

               inputMatriz = argumentos[0]
               matriz = utilidades.leer_matriz_numerica(inputMatriz)
            else:
             if len(argumentos) > 0:
                # Check if the number of arguments matches the function's expected number
                if abs(len(argumentos) - funcion.__code__.co_argcount) not in (1, 2):
                    print("Argumentos incorrectos para el comando", nombre_del_comando)
                    continue  # Continue with the next iteration of the loop
                # Call the function with arguments
                try: 
                   print("llego")
                   funcion(*argumentos,matriz)
               
                except Exception as e:
                   print("An error occurred:", e)
                   funcion(*argumentos,lista_adyacencia)
                finally:
                   try:
                    funcion(*argumentos,matriz,lista_nodos)
                   except:
                     funcion(*argumentos,matriz,lista_adyacencia)
             else:
                # Call the function without arguments
                try:
                  funcion()
                except:
                   #Una funcion que requiera la matriz
                   try:
                    try:
                     funcion(matriz)
                    except:
                       funcion(lista_nodos)
                   except:
                      print("llamado a la funcion ", nombre_del_comando)
                      funcion(matriz,lista_adyacencia)
                finally:
                   #El caso especial para salir
                   ejecutar_bucle = funcion(ejecutar_bucle)
      
      else:
            print("Nombre del comando no reconocido", nombre_del_comando)
     except TypeError:
        # If there's a TypeError (indicating function call with incorrect arguments), handle it here
        print("llamada a", nombre_del_comando)
