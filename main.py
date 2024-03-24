import sys
from leerYPresentarInformacion import utilidades
if __name__ == "__main__":
    ## Check arguments
    if len( sys.argv ) < 2:
     print( "Usage: python3", sys.argv[ 0 ], "input_file" )
     sys.exit( 1 )

    input_file = sys.argv[1]
    matriz = utilidades.leer_archivo(input_file)
    
    utilidades.mostrar_matriz_ascii(matriz)
