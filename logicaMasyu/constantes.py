class Constantes:
    NADA = 0
    BLANCO = 1
    NEGRO = 2
    NO_VECINOS = 3
    ESQUINA = 4
    AL_LADO = 5
    VERTICAL = 6
    UP_RIGHT = 7
    RIGHT_DOWN = 8
    DOWN_LEFT = 9
    LEFT_UP = 10

class Direcciones:
    DERECHA = 'derecha'
    IZQUIERDA = 'izquierda'
    ARRIBA = 'arriba'
    ABAJO = 'abajo'

class DirSeleccion:
    all_dir = {Constantes.NADA,   Constantes.UP_RIGHT, Constantes.RIGHT_DOWN, Constantes.DOWN_LEFT, Constantes.LEFT_UP, Constantes.AL_LADO, Constantes.VERTICAL}
    left_dir = {Constantes.RIGHT_DOWN,Constantes.DOWN_LEFT,Constantes.AL_LADO,Constantes.BLANCO,Constantes.NEGRO}
    right_dir = {Constantes.UP_RIGHT,Constantes.LEFT_UP,Constantes.AL_LADO,Constantes.BLANCO,Constantes.NEGRO}
    up_dir = {Constantes.DOWN_LEFT,Constantes.LEFT_UP,Constantes.VERTICAL,Constantes.BLANCO,Constantes.NEGRO}
    down_dir = {Constantes.UP_RIGHT,Constantes.RIGHT_DOWN,Constantes.VERTICAL,Constantes.BLANCO,Constantes.NEGRO}
    straight_dir = {Constantes.AL_LADO, Constantes.VERTICAL }
    bend_dir = {Constantes.UP_RIGHT,Constantes.RIGHT_DOWN,Constantes.DOWN_LEFT,Constantes.LEFT_UP}
    horizontal_dir = {Constantes.AL_LADO}
    piezas = {Constantes.BLANCO,Constantes.NEGRO}

"""
 get_ascii = lambda x: (
    ' . ' if x == constantes.Constantes.NADA else  # Valor 0: Punto (Vacío)
    (' O ' if x == constantes.Constantes.BLANCO else  # Valor 1: Círculo blanco (Blanco)
    (' X ' if x == constantes.Constantes.NEGRO else  # Valor 2: X (Negro)
    (' - ' if x == constantes.Constantes.NO_VECINOS else  # Valor 3: Guión (Sin Vecinos)
    (' / ' if x == constantes.Constantes.ESQUINA else  # Valor 4: Diagonal (/) (Esquina)
    ('---' if x == constantes.Constantes.AL_LADO else  # Valor 5: Tres guiones (---) (Al lado)
    (' / ' if x == constantes.Constantes.UP_RIGHT else  # Valor 7: Diagonal (/) (UP_RIGHT)
    (' \\ ' if x == constantes.Constantes.RIGHT_DOWN else  # Valor 8: Diagonal invertida (\) (RIGHT_DOWN)
    (' / ' if x == constantes.Constantes.DOWN_LEFT else  # Valor 9: Diagonal (/) (DOWN_LEFT)
    (' \\ ' if x == constantes.Constantes.LEFT_UP else  # Valor 10: Diagonal invertida (\) (LEFT_UP)
    ' | '))))))))))  # Valor predeterminado: Barra vertical (|)
"""