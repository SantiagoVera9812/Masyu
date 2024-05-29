from copy import deepcopy
from logicaMasyu.constantes import DirSeleccion
from logicaMasyu.constantes import Constantes
from logicaMasyu.checkWin import contar_casillas_1_2
import traceback

def jugadorAutomatico(matriz):

    numero_casillas = contar_casillas_1_2(matriz)

    print(numero_casillas)
    
    try:  
           startingPearl = find_starting_pearl(matriz)
          
           handle_starting_pearl(startingPearl, matriz, numero_casillas)
        
    except SolutionFound as e:
      print(f"Target found: {e}")
        

    """
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
                 apply_black_rule(solucion, pearl[1], pearl[2])
                except Exception as e:
                 print("An error occurred:", e)
            elif pearl[0] == 1:
                try:
                 apply_white_rule(solucion, pearl[1], pearl[2])
                except Exception as e:
                 print("An error occurred:", e)

        for r in range(num_filas):
                for c in range(num_columnas):
                    if len(solucion[r][c]) == 1:
                     try:
                        filter_adj(solucion, r, c, num_filas, num_columnas)
                     except Exception as e:
                          print("An error occurred:", e)
                          print("Details:")
                          print(f"r: {r}, c: {c}, num_filas: {num_filas}, num_columnas: {num_columnas}")
                          print("solucion[r][c]:", solucion[r][c] if r < len(solucion) and c < len(solucion[0]) else "Out of bounds")
                          print(traceback.format_exc()) */
 
    print_solution(solucion)
  """
    

#AUTOPLAYER
def find_starting_pearl(matrix):
    size = len(matrix)

    # Check for a white pearl on the first/last row
    for i in range(size):
        if matrix[0][i] == 1:
            return (0, i, 1)  # Type 1
        if matrix[size-1][i] == 1:
            return (size-1, i, 1)  # Type 1

    # Check for a white pearl on the first/last column
    for i in range(size):
        if matrix[i][0] == 1:
            return (i, 0, 2)  # Type 2
        if matrix[i][size-1] == 1:
            return (i, size-1, 2)  # Type 2

    # Check for a black pearl in the corners
    if matrix[0][0] == 2:
        return (0, 0, 3)  # Type 3
    if matrix[0][size-1] == 2:
        return (0, size-1, 3)  # Type 3
    if matrix[size-1][0] == 2:
        return (size-1, 0, 3)  # Type 3
    if matrix[size-1][size-1] == 2:
        return (size-1, size-1, 3)  # Type 3

    # Check for any white pearl
    for x in range(size):
        for y in range(size):
            if matrix[x][y] == 1:
                return (x, y, 4)  # Type 4

    # Check for any black pearl
    for x in range(size):
        for y in range(size):
            if matrix[x][y] == 2:
                return (x, y, 5)  # Type 5

    return None
def handle_starting_pearl(start_pearl, matrix, total_pearls):
    x, y, pearl_type = start_pearl

    if pearl_type == 1:
        # White pearl on the first row
        if x == 0:
            matrix[x][y + 1] = 8  # Assign UL to the cell on the right
            buildRoad(x, y + 1, x, y, x, y, matrix, total_pearls, 0)  # Call function on the right cell
        # White pearl on the last row
        elif x == len(matrix) - 1:
            matrix[x][y + 1] = 10  # Assign DL to the cell on the right
            buildRoad(x, y + 1, x, y, x, y, matrix, total_pearls, 0)  # Call function on the right cell
    # Handle other pearl types similarly
    elif pearl_type == 2:
        # White pearl on the first/last column
        if y == 0:
            matrix[x - 1][y] = 7  # Assign UR to the up cell
            buildRoad(x - 1, y, x, y, x, y, matrix, total_pearls, 0)  # Call function on the up cell
        elif y == len(matrix) - 1:
            matrix[x - 1][y] = 8  # Assign UL to the up cell
            buildRoad(x - 1, y, x, y, x, y, matrix, total_pearls, 0)  # Call function on the up cell
    elif pearl_type == 3:
        # Black pearl in a corner
        if (x, y) == (0, 0):
            matrix[x][y + 1] = 5  # H
            buildRoad(x, y + 1, x, y, x, y, matrix, total_pearls, 0)  # Call function on the right cell
            matrix[x][y + 1] = 8  # Assign UL to the right cell
            buildRoad(x, y + 1, x, y, x, y, matrix, total_pearls, 0)  # Call function on the right cell with new UL value
        elif (x, y) == (0, len(matrix) - 1):
            matrix[x][y - 1] = 5  # H
            buildRoad(x, y - 1, x, y, x, y, matrix, total_pearls, 0)  # Call function on the left cell
            matrix[x][y - 1] = 7  # Assign UR to the left cell
            buildRoad(x, y - 1, x, y, x, y, matrix, total_pearls, 0)  # Call function on the left cell with new UR value
        elif (x, y) == (len(matrix) - 1, 0):
            matrix[x][y + 1] = 5  # H
            buildRoad(x, y + 1, x, y, x, y, matrix, total_pearls, 0)  # Call function on the right cell
            matrix[x][y + 1] = 10  # Assign DL to the right cell
            buildRoad(x, y + 1, x, y, x, y, matrix, total_pearls, 0)  # Call function on the right cell with new DL value
        else:  # (x, y) == (len(matrix) - 1, len(matrix) - 1)
            matrix[x][y - 1] = 5  # H
            buildRoad(x, y - 1, x, y, x, y, matrix, total_pearls, 0)  # Call function on the left cell
            matrix[x][y - 1] = 9  # Assign DR to the left cell
            buildRoad(x, y - 1, x, y, x, y, matrix, total_pearls, 0)  # Call function on the left cell with new DR value
    elif pearl_type == 4:
        matrix[x - 1][y] = 7  # Assign UR to the up cell
        buildRoad(x - 1, y, x, y, x, y, matrix, total_pearls, 0)  # Call function on the up cell
        matrix[x - 1][y] = 8  # Assign UL to the up cell
        buildRoad(x - 1, y, x, y, x, y, matrix, total_pearls, 0)  # Call function on the up cell with new UL value

        matrix[x][y + 1] = 8  # Assign UL to the right cell
        buildRoad(x, y + 1, x, y, x, y, matrix, total_pearls, 0)  # Call function on the right cell with new UL value

        matrix[x][y + 1] = 10  # Assign DL to the right cell
        buildRoad(x, y + 1, x, y, x, y, matrix, total_pearls, 0)  # Call function on the right cell with new DL value

    elif pearl_type == 5:
        matrix[x - 1][y] = 6  # Assign V to the up cell
        buildRoad(x - 1, y, x, y, x, y, matrix, total_pearls, 0)  # Call function on the up cell
        matrix[x - 1][y] = 7  # Assign UR to the up cell
        buildRoad(x - 1, y, x, y, x, y, matrix, total_pearls, 0)  # Call function on the up cell
        matrix[x - 1][y] = 8  # Assign UL to the up cell
        buildRoad(x - 1, y, x, y, x, y, matrix, total_pearls, 0)  # Call function on the up cell with new UL value

        matrix[x + 1][y] = 6  # Assign V to the down cell
        buildRoad(x + 1, y, x, y, x, y, matrix, total_pearls, 0)  # Call function on the down cell
        matrix[x + 1][y] = 9  # Assign DR to the down cell
        buildRoad(x + 1, y, x, y, x, y, matrix, total_pearls, 0)  # Call function on the down cell
        matrix[x + 1][y] = 10  # Assign DL to the down cell
        buildRoad(x + 1, y, x, y, x, y, matrix, total_pearls, 0)  # Call function on the down cell with new DL value

class SolutionFound(Exception):
    pass

def buildRoad(x, y, initial_x, initial_y, last_x, last_y, matrix, total_pearls, pearls_visited, visited=None, ex = 0):
    connections = []
    # Check the type of pearl in the cell
    pearl_type = matrix[x][y]
    if pearl_type in [1, 2]:
        pearls_visited += 1
    # Check up cell
    if pearl_type in [6, 9, 10]:
        if x > 0 and (matrix[x - 1][y] in [1, 2, 6, 7, 8, 0]):
            connections.append((x - 1, y))

    # Check down cell
    if pearl_type in [6, 7, 8]:
        if x < len(matrix) - 1 and (matrix[x + 1][y] in [1, 2, 6, 9, 10, 0]):
            connections.append((x + 1, y))

    # Check right cell
    if pearl_type in [5, 7, 9]:
        if y < len(matrix[x]) - 1 and (matrix[x][y + 1] in [1, 2, 5, 8, 10, 0]):
            connections.append((x, y + 1))

    # Check left cell
    if pearl_type in [5, 8, 10]:
        if y > 0 and (matrix[x][y - 1] in [1, 2, 5, 7, 9, 0]):
            connections.append((x, y - 1))

    # Remove (last_x, last_y) from connections if it exists
    if (last_x, last_y) in connections:
        connections.remove((last_x, last_y))
    if len(connections) == 0 and last_x is not None:
        return False
    new_x, new_y = connections[0]
    if (new_x, new_y) == (initial_x, initial_y):
        print('PRUEBA: ', matrix)
        if pearls_visited == total_pearls:
          raise SolutionFound(matrix) # Closed loop detected
        else:
          return False
    # Additional checks for the last_x, last_y cell
    if last_x is not None:
        if matrix[x][y] == 1:  # If current cell contains pearl 1
            if last_x > x:  # Last move was down
                for value in [6, 7, 8]:
                  if x > 0:
                    matrix[x - 1][y] = value
                    buildRoad(x - 1, y, initial_x, initial_y, x, y, matrix, total_pearls, pearls_visited + 1, visited, ex+1)
                    matrix[x - 1][y] = 0  # Reset the cell

            if last_x < x:  # Last move was up
                for value in [6, 9, 10]:
                  if x < len(matrix) - 1:
                    matrix[x + 1][y] = value
                    buildRoad(x + 1, y, initial_x, initial_y, x, y, matrix, total_pearls, pearls_visited + 1, visited, ex+1)
                    matrix[x + 1][y] = 0  # Reset the cell

            if last_y > y:  # Last move was right
                for value in [5, 8, 10]:
                  if y < len(matrix[x]) - 1:
                    matrix[x][y + 1] = value
                    buildRoad(x, y + 1, initial_x, initial_y, x, y, matrix, total_pearls, pearls_visited + 1, visited, ex+1)
                    matrix[x][y + 1] = 0  # Reset the cell

            if last_y < y:  # Last move was left
                for value in [5, 7, 9]:
                  if y > 0:
                    matrix[x][y - 1] = value
                    buildRoad(x, y - 1, initial_x, initial_y, x, y, matrix, total_pearls, pearls_visited + 1, visited, ex+1)
                    matrix[x][y - 1] = 0  # Reset the cell

        elif matrix[x][y] == 2:  # If current cell contains pearl 2
            print('here')
            if last_x > x or last_x < x:  # Last move was down or Last move was up
                for value in [5, 7, 9]:
                  if y > 0:
                    matrix[x][y - 1] = value
                    buildRoad(x, y - 1, initial_x, initial_y, x, y, matrix, total_pearls, pearls_visited + 1, visited, ex+1)
                    matrix[x][y - 1] = 0  # Reset the cell
                for value in [5, 8, 10]:
                  if y < len(matrix) - 1:
                    matrix[x][y + 1] = value
                    buildRoad(x, y + 1, initial_x, initial_y, x, y, matrix, total_pearls, pearls_visited + 1, visited, ex+1)
                    matrix[x][y - 1] = 0  # Reset the cell

            if last_y > y or last_y < y:  # Last move was right or Last move was left
                for value in [6, 9, 10]:
                  if x < len(matrix[x]) - 1:
                    matrix[x + 1][y] = value
                    buildRoad(x + 1, y, initial_x, initial_y, x, y, matrix, total_pearls, pearls_visited + 1, visited, ex+1)
                    matrix[x + 1][y] = 0  # Reset the cell
                for value in [6, 7, 8]:
                  if x > 0:
                    matrix[x - 1][y] = value
                    buildRoad(x - 1, y, initial_x, initial_y, x, y, matrix, total_pearls, pearls_visited + 1, visited, ex+1)
                    matrix[x - 1][y] = 0  # Reset the cell
        elif matrix[new_x][new_y] in [1,2]:
            print(new_x, '-' ,new_y)
            buildRoad(new_x, new_y, initial_x, initial_y, x, y, matrix, total_pearls, pearls_visited, visited, ex+1)
        else:
            if len(connections) != 1 and last_x is not None:
              return False
            if new_x > x:  # connection move is down
                for value in [6, 9, 10]:
                    matrix[new_x][new_y] = value
                    buildRoad(new_x, new_y, initial_x, initial_y, x, y, matrix, total_pearls, pearls_visited, visited, ex+1)
                    matrix[new_x][new_y] = 0  # Reset the cell

            if new_x < x:  # connection move is up
                for value in [6, 7, 8]:
                    matrix[new_x][new_y] = value
                    buildRoad(new_x, new_y, initial_x, initial_y, x, y, matrix, total_pearls, pearls_visited, visited, ex+1)
                    matrix[new_x][new_y] = 0  # Reset the cell

            if new_y > y:  # connection move is right
                for value in [5, 8, 10]:
                    matrix[new_x][new_y] = value
                    buildRoad(new_x, new_y, initial_x, initial_y, x, y, matrix, total_pearls, pearls_visited, visited, ex+1)
                    matrix[new_x][new_y] = 0  # Reset the cell

            if new_y < y:  # connection move is left
                for value in [5, 7, 9]:
                    matrix[new_x][new_y] = value
                    buildRoad(new_x, new_y, initial_x, initial_y, x, y, matrix, total_pearls, pearls_visited, visited, ex+1)
                    matrix[new_x][new_y] = 0  # Reset the cell
    return False