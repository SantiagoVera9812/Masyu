import sys
from leerYPresentarInformacion import utilidades
from leerYPresentarInformacion import insercionUsuario
from logicaMasyu import listaAdyecencia

funciones = {
   "insertar_elemento": insercionUsuario.insertar_elementos,
   "salir":insercionUsuario.salir,
   "mostrar_matriz":utilidades.mostrar_matriz_ascii,
   "reiniciar":insercionUsuario.reiniciar,
   "jugador_automatico":insercionUsuario.reiniciar,
   "mostrar_matriz_numerica":utilidades.mostrar_matriz,
   "editar_elemento":insercionUsuario.editar_elemento,
   "obtener_primera_ficha": utilidades.obtener_primera_ficha,
   "eliminar_nodo":utilidades.eliminar_nodo_y_vecinos_matriz,
   "ignorar_nodo":utilidades.eliminar_nodo_y_vecinos
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

    while ejecutar_bucle:
     comando = input("$")
     partes = comando.split()
     nombre_del_comando = partes[0]
     argumentos = partes[1:]

     try:
      if nombre_del_comando in funciones:
            funcion = funciones[nombre_del_comando]
            # If the command requires arguments
            if len(argumentos) > 0:
                # Check if the number of arguments matches the function's expected number
                if abs(len(argumentos) - funcion.__code__.co_argcount) not in (1, 2):
                    print("Argumentos incorrectos para el comando", nombre_del_comando)
                    continue  # Continue with the next iteration of the loop
                # Call the function with arguments
                try: 
                   funcion(*argumentos,matriz)
                except:
                   funcion(*argumentos,lista_adyacencia)
                finally:
                   funcion(*argumentos,matriz,lista_adyacencia)
            else:
                # Call the function without arguments
                try:
                 funcion()
                except:
                   #Una funcion que requiera la matriz
                   try:
                    funcion(matriz)
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
