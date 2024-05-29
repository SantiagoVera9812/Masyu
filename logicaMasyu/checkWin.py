
def contar_casillas_1_2(matriz):
    total_casillas_1_2 = 0
    for fila in matriz:
        for elemento in fila:
            if elemento == 1 or elemento == 2:
                total_casillas_1_2 += 1

    print(total_casillas_1_2)
    return total_casillas_1_2

def encontrar_primer_valor_no_comun(matriz):
    valores_comunes = {0, 1, 2, 3}
    for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila):
            if valor not in valores_comunes:
                return (i, j)
    return None, None 

def verificarRespuesta(matriz):
    total_pearls = contar_casillas_1_2(matriz)
    i, j = encontrar_primer_valor_no_comun(matriz)
    print(total_pearls)
    print(i)
    print(j)
    ganador = check_connections2(i, j, i, j, None, None, matriz,total_pearls,0)
    print(ganador)

def check_connections2(x, y, initial_x, initial_y, last_x, last_y, matrix, total_pearls, pearls_visited, visited=None):
    if visited is None:
        visited = set()
        visited.add((x, y))

    connections = []

    # Check the type of pearl in the cell
    pearl_type = matrix[x][y]
    if pearl_type in [1, 2]:
        pearls_visited += 1

    print("aca: " + str(matrix[x][y]) + "/coord: " + str(x) +","+str(y))
    # Check up cell
    if pearl_type in [1, 2, 6, 9, 10]:
        #print('hereU: ' + str(matrix[x - 1][y]))
        if x > 0 and (matrix[x - 1][y] in [1, 2, 6, 8, 7]):
            connections.append((x - 1, y))

    # Check down cell
    if pearl_type in [1, 2, 6, 7, 8]:
        #print('hereD: ' + str(matrix[x + 1][y]))
        if x < len(matrix) - 1 and (matrix[x + 1][y] in [1, 2, 6, 10, 9]):
            connections.append((x + 1, y))

    # Check right cell
    if pearl_type in [1, 2, 5, 7, 9]:
        #print('hereR: ' + str(matrix[x][y + 1]))
        if y < len(matrix[x]) - 1 and (matrix[x][y + 1] in [1, 2, 5, 8, 10]):
            connections.append((x, y + 1))

    # Check left cell
    if pearl_type in [1, 2, 5, 8, 10]:
        #print('hereL: ' + str(matrix[x][y - 1]))
        if y > 0 and (matrix[x][y - 1] in [1, 2, 5, 7, 9]):
            connections.append((x, y - 1))

    # Remove (last_x, last_y) from connections if it exists
    if (last_x, last_y) in connections:
        connections.remove((last_x, last_y))
    print(connections)
    # Additional checks for the last_x, last_y cell
    if last_x is not None:
        if matrix[x][y] == 1:  # If current cell contains pearl 1
            if last_x > x or last_x < x:  # Last move was down or up
                if matrix[x - 1][y] not in [6, 7, 8] or matrix[x + 1][y] not in [7, 8, 9, 10]:
                    return False
            elif last_y > y or last_y < y:  # Last move was right or left
                if matrix[x][y + 1] not in [5, 8, 10] or matrix[x][y - 1] not in [5, 7, 9]:
                    return False
        elif matrix[x][y] == 2:  # If current cell contains pearl 2
            if last_x > x or last_x < x:  # Last move was down or up
                if not (matrix[x][y - 1]  in [5, 7, 9] or matrix[x][y + 1] in [5, 8, 10]):
                    return False
            elif last_y > y or last_y < y:  # Last move was right or left
                if not(matrix[x - 1][y] in [6, 7, 8] or matrix[x + 1][y] in [6, 9, 10]):
                    return False

    if len(connections) != 1 and last_x is not None:
        return False
    else:
        other_x, other_y = connections[0]
        if (other_x, other_y) == (initial_x, initial_y):
            return total_pearls == pearls_visited  # Closed loop detected
        elif (other_x, other_y) not in visited:
            visited.add((other_x, other_y))
            if check_connections2(other_x, other_y, initial_x, initial_y, x, y, matrix, total_pearls, pearls_visited, visited):
                return True

    return False