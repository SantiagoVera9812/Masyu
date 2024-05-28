from copy import deepcopy
from logicaMasyu.constantes import DirSeleccion
from logicaMasyu.constantes import Constantes 


def get_ascii(x):
    if x == Constantes.NADA:
        return ' . '  # Valor 0: Punto (Vacío)
    elif x == Constantes.BLANCO:
        return ' O '  # Valor 1: Círculo blanco (Blanco)
    elif x == Constantes.NEGRO:
        return ' X '  # Valor 2: X (Negro)
    elif x == Constantes.NO_VECINOS:
        return ' - '  # Valor 3: Guión (Sin Vecinos)
    elif x == Constantes.ESQUINA:
        return ' / '  # Valor 4: Diagonal (/) (Esquina)
    elif x == Constantes.AL_LADO:
        return '---'  # Valor 5: Tres guiones (---) (Al lado)
    elif x == Constantes.UP_RIGHT:
        return ' / '  # Valor 7: Diagonal (/) (UP_RIGHT)
    elif x == Constantes.RIGHT_DOWN:
        return ' \\ '  # Valor 8: Diagonal invertida (\) (RIGHT_DOWN)
    elif x == Constantes.DOWN_LEFT:
        return ' / '  # Valor 9: Diagonal (/) (DOWN_LEFT)
    elif x == Constantes.LEFT_UP:
        return ' \\ '  # Valor 10: Diagonal invertida (\) (LEFT_UP)
    else:
        return ' | '  # Valor predeterminado: Barra vertical (|)


#Agregar un array para cada posible seleccion de direcciones
def create_solution_array(rows, cols):
    all_dir = {Constantes.NO_VECINOS, Constantes.UP_RIGHT, Constantes.RIGHT_DOWN, Constantes.DOWN_LEFT, Constantes.LEFT_UP, Constantes.AL_LADO, Constantes.VERTICAL}
    solution = [[all_dir.copy() for _ in range(cols)] for _ in range(rows)]
    return solution

#Eliminar soluciones invalidas a lo mas alto, lo mas bajo la parte a la derecha y la parte a la izquierda del problema
def remove_invalid_edge_shapes(solution):
    rows = len(solution)
    cols = len(solution[0])

    for c in range(cols):
        solution[0][c] -= DirSeleccion.up_dir     # top row
        solution[rows - 1][c] -= DirSeleccion.down_dir   # bottom row

    for r in range(rows):
        solution[r][0] -= DirSeleccion.left_dir   # leftmost column
        solution[r][cols - 1] -= DirSeleccion.right_dir  # rightmost column

    return solution


def apply_pearl_constraints(matrix, solution):
    rows = len(matrix)
    cols = len(matrix[0])

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1:  # Black pearl
                solution[r][c] &= DirSeleccion.bend_dir
                # Remove black near edge
                if r + 2 > rows - 1:
                    solution[r][c] &= DirSeleccion.up_dir
                if r - 2 < 0:
                    solution[r][c] &= DirSeleccion.down_dir
                if c + 2 > cols - 1:
                    solution[r][c] &= DirSeleccion.left_dir
                if c - 2 < 0:
                    solution[r][c] &= DirSeleccion.right_dir

            elif matrix[r][c] == 2:  # White pearl
                solution[r][c] &= DirSeleccion.straight_dir

    return solution

def print_solution(solution):
    num_filas = len(solution)
    num_columnas = len(solution[0]) if solution else 0

    for r in range(num_filas):
        for c in range(num_columnas):
            # Convierte el conjunto a cadena y ajusta la longitud
            
            for item in solution[r][c]:
                ascii_art = get_ascii(item)
                print(ascii_art, end="")

            print(" $ ", end="")
        print()
    print()

  
def todasLasPosiblesCombinaciones(matriz):
    num_filas = len(matriz)
    num_columnas = len(matriz[0]) if matriz else 0
    solution = create_solution_array(num_filas, num_columnas)
    solution = remove_invalid_edge_shapes(solution)
    solution = apply_pearl_constraints(matriz, solution)   
    
    return solution

def jugadorAutomatico(matriz):
    num_filas = len(matriz)
    num_columnas = len(matriz[0]) if matriz else 0
    solucion = todasLasPosiblesCombinaciones(matriz)

    pearls = set()
    for r in range(len(matriz)):
        for c in range(len(matriz[0])):
            if matriz[r][c] in [1, 2]:
                pearls.add((matriz[r][c], r, c))
    
    print("Pearls:", pearls)
    print_solution(solucion)

    tmp = None
    while tmp != solucion:
        # Make a deepcopy of the current solution
        tmp = deepcopy(solucion)
        
        # Apply rules for each pearl
        for pearl in pearls:
            if pearl[0] == 0:
                try:
                 apply_black_rule(tmp, pearl[1], pearl[2])
                except Exception as e:
                 print("An error occurred:", e)
            elif pearl[0] == 1:
                try:
                 apply_white_rule(tmp, pearl[1], pearl[2])
                except Exception as e:
                 print("An error occurred:", e)

        for r in range(num_filas):
                for c in range(num_columnas):
                    if len(solucion[r][c]) == 1:
                     try:
                        filter_adj(tmp, r, c, num_filas, num_columnas)
                     except Exception as e:
                        print("An error occurred:", e)

    print_solution(solucion)

    



def apply_white_rule(solution, r, c):
    
    # No bend on adjacent vertical, must be horizontal
    if len(solution[r][c]) > 1:
        adj_verts = set()
        if r != 0:
            adj_verts |= solution[r - 1][c]
        if r != len(solution) - 1:
            adj_verts |= solution[r + 1][c]

        if not adj_verts & DirSeleccion.bend_dir:
            solution[r][c] = DirSeleccion.horizontal_dir

        # No bend on adjacent horizontal, must be vertical
        adj_hors = set()
        if c != 0:
            adj_hors |= solution[r][c - 1]
        if c != len(solution[0]) - 1:
            adj_hors |= solution[r][c + 1]

        if not adj_hors & DirSeleccion.bend_dir:
            solution[r][c] = DirSeleccion.vertical_dir

    # Horizontal
    if solution[r][c] == DirSeleccion.horizontal_dir:
        solution[r][c - 1] &= DirSeleccion.right_dir
        solution[r][c + 1] &= DirSeleccion.left_dir
        if r != 0:
            solution[r - 1][c] -= DirSeleccion.down_dir
        if r != len(solution) - 1:
            solution[r + 1][c] -= DirSeleccion.up_dir

        # No bend on left, right must bend
        if not solution[r][c - 1] & DirSeleccion.bend_dir:
            solution[r][c + 1] &= DirSeleccion.bend_dir
        # No bend on right, left must bend
        if not solution[r][c + 1] & DirSeleccion.bend_dir:
            solution[r][c - 1] &= DirSeleccion.bend_dir

    # Vertical
    if solution[r][c] == DirSeleccion.vertical_dir:
        solution[r - 1][c] &= DirSeleccion.down_dir
        solution[r + 1][c] &= DirSeleccion.up_dir
        if c != 0:
            solution[r][c - 1] -= DirSeleccion.right_dir
        if c != len(solution[0]) - 1:
            solution[r][c + 1] -= DirSeleccion.left_dir

        # No bend on down, up must bend
        if not solution[r - 1][c] & DirSeleccion.bend_dir:
            solution[r + 1][c] &= DirSeleccion.bend_dir
        # No bend on up, down must bend
        if not solution[r + 1][c] & DirSeleccion.bend_dir:
            solution[r - 1][c] &= DirSeleccion.bend_dir
    
    return solution




def apply_black_rule(solution, r, c):
    # Ensure valid directions around a black pearl
    if len(solution[r][c]) > 1:
        # Check and update possible directions for the black pearl
        if r > 0:
            if not solution[r - 1][c] & DirSeleccion.vertical_dir:
                solution[r][c] -= DirSeleccion.up_dir
            elif r > 1 and not solution[r - 2][c] & DirSeleccion.down_dir:
                solution[r][c] -= DirSeleccion.up_dir

        if r < len(solution) - 1:
            if not solution[r + 1][c] & DirSeleccion.vertical_dir:
                solution[r][c] -= DirSeleccion.down_dir
            elif r < len(solution) - 2 and not solution[r + 2][c] & DirSeleccion.up_dir:
                solution[r][c] -= DirSeleccion.down_dir

        if c > 0:
            if not solution[r][c - 1] & DirSeleccion.horizontal_dir:
                solution[r][c] -= DirSeleccion.left_dir
            elif c > 1 and not solution[r][c - 2] & DirSeleccion.right_dir:
                solution[r][c] -= DirSeleccion.left_dir

        if c < len(solution[0]) - 1:
            if not solution[r][c + 1] & DirSeleccion.horizontal_dir:
                solution[r][c] -= DirSeleccion.right_dir
            elif c < len(solution[0]) - 2 and not solution[r][c + 2] & DirSeleccion.left_dir:
                solution[r][c] -= DirSeleccion.right_dir

    # Constrain must-go directions
    if solution[r][c] == DirSeleccion.down_dir:
        solution[r + 1][c] &= DirSeleccion.vertical_dir
        solution[r + 2][c] &= DirSeleccion.up_dir
        if r > 0:
            solution[r - 1][c] -= DirSeleccion.down_dir
        if {Constantes.UP_RIGHT}.issubset(solution[r][c]):
            solution[r + 1][c + 1] -= DirSeleccion.left_dir
        if {Constantes.RIGHT_DOWN}.issubset(solution[r][c]):
            solution[r + 1][c - 1] -= DirSeleccion.right_dir

    if solution[r][c] == DirSeleccion.left_dir:
        solution[r][c - 1] &= DirSeleccion.horizontal_dir
        solution[r][c - 2] &= DirSeleccion.right_dir
        if c < len(solution[0]) - 1:
            solution[r][c + 1] -= DirSeleccion.left_dir
        if {Constantes.RIGHT_DOWN}.issubset(solution[r][c]):
            solution[r + 1][c - 1] -= DirSeleccion.up_dir
        if {Constantes.DOWN_LEFT}.issubset(solution[r][c]):
            solution[r - 1][c - 1] -= DirSeleccion.down_dir

    if solution[r][c] == DirSeleccion.up_dir:
        solution[r - 1][c] &= DirSeleccion.vertical_dir
        solution[r - 2][c] &= DirSeleccion.down_dir
        if r < len(solution) - 1:
            solution[r + 1][c] -= DirSeleccion.up_dir
        if {Constantes.DOWN_LEFT}.issubset(solution[r][c]):
            solution[r - 1][c - 1] -= DirSeleccion.right_dir
        if {Constantes.LEFT_UP}.issubset(solution[r][c]):
            solution[r - 1][c + 1] -= DirSeleccion.left_dir

    if solution[r][c] == DirSeleccion.right_dir:
        solution[r][c + 1] &= DirSeleccion.horizontal_dir
        solution[r][c + 2] &= DirSeleccion.left_dir
        if r > 0:
            solution[r][c - 1] -= DirSeleccion.right_dir
        if {Constantes.UP_RIGHT}.issubset(solution[r][c]):
            solution[r + 1][c + 1] -= DirSeleccion.up_dir
        if {Constantes.UP_RIGHT}.issubset(solution[r][c]):
            solution[r - 1][c + 1] -= DirSeleccion.down_dir
    
    return solution

def filter_adj(solution, r, c, num_filas, num_columnas):
     # if current cell is empty
    if solution == {0}:
            # no adj cell go to current cell
            if r != 0:
                solution[r - 1][c] -= DirSeleccion.down_dir
            if c != 0:
                solution[r][c - 1] -= DirSeleccion.right_dir
            if r != num_filas - 1:
                solution[r + 1][c] -= DirSeleccion.up_dir
            if c != num_columnas - 1:
                solution[r][c + 1] -= DirSeleccion.left_dir

        # if current cell is shape 1
    elif solution[r][c] == {1}:
            # restrict left and up
            if r != 0:
                solution[r - 1][c] -= DirSeleccion.down_dir
            if c != 0:
                solution[r][c - 1] -= DirSeleccion.right_dir

            # must go down and right
            solution[r + 1][c] &= DirSeleccion.up_dir
            solution[r][c + 1] &= DirSeleccion.left_dir

        # if current cell is shape 2
    elif solution[r][c] == {2}:
            # restrict right and up
            if r != 0:
                solution[r - 1][c] -= DirSeleccion.down_dir
            if c != num_columnas - 1:
                solution[r][c + 1] -= DirSeleccion.left_dir

            # must go down and left
            solution[r + 1][c] &= DirSeleccion.up_dir
            solution[r][c - 1] &= DirSeleccion.right_dir

        # if current cell is shape 3
    elif solution[r][c] == {3}:
            # restrict down and right
            if r != num_filas - 1:
                solution[r + 1][c] -= DirSeleccion.up_dir
            if c != num_columnas - 1:
                solution[r][c + 1] -= DirSeleccion.left_dir

            # must go up and left
            solution[r - 1][c] &= DirSeleccion.down_dir
            solution[r][c - 1] &= DirSeleccion.right_dir

        # if current cell is shape 4
    elif solution[r][c] == {4}:
            # restrict left and down
            if r != num_filas - 1:
                solution[r + 1][c] -= DirSeleccion.up_dir
            if c != 0:
                solution[r][c - 1] -= DirSeleccion.right_dir

            # must go up and right
            solution[r - 1][c] &= DirSeleccion.down_dir
            solution[r][c + 1] &= DirSeleccion.left_dir

        # if current cell is shape 5
    elif solution[r][c] == {5}:
            # restrict up and down
            if r != 0:
                solution[r - 1][c] -= DirSeleccion.down_dir
            if r != num_filas - 1:
                solution[r + 1][c] -= DirSeleccion.up_dir

            # must go left and right
            solution[r][c - 1] &= DirSeleccion.right_dir
            solution[r][c + 1] &= DirSeleccion.left_dir

        # if current cell is shape 6
    elif solution[r][c] == {6}:
            # restrict left and right
            if c != 0:
                solution[r][c - 1] -= DirSeleccion.right_dir
            if c != num_columnas - 1:
                solution[r][c + 1] -= DirSeleccion.left_dir

            # must go up and down
            solution[r - 1][c] &= DirSeleccion.down_dir
            solution[r + 1][c] &= DirSeleccion.up_dir

