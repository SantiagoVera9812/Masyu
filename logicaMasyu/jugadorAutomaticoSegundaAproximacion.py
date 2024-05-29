from logicaMasyu.constantes import DirSeleccion
from logicaMasyu.constantes import Constantes

def apply_white_rule(solution, r, c):
    
    #  es una perla blanca o aún no está restringida a una única dirección.
    if len(solution[r][c]) > 1:

        print(".....................viendo las celdas adyacentes.........................................")
        #las posibles direcciones de línea en las celdas adyacentes verticalmente (arriba y abajo) a la celda [r][c].
        adj_verts = set()
        if r != 0:
            adj_verts |= solution[r - 1][c]
        if r != len(solution) - 1:
            adj_verts |= solution[r + 1][c]
        
        #Si ninguna de las celdas verticalmente adyacentes permite una curva (no tiene bend_dir), entonces la celda [r][c] debe ser una línea horizontal (horizontal_dir),
        if not adj_verts & DirSeleccion.bend_dir:
            solution[r][c] = DirSeleccion.horizontal_dir

        print(solution)
        print("...........................................................................................")

        # No bend on adjacent horizontal, must be vertical
        #las posibles direcciones de línea en las celdas adyacentes horizontales a la celda [r][c].
        print(".....................viendo las celdas adyacentes horizontales.........................................")
        adj_hors = set()
        if c != 0:
            adj_hors |= solution[r][c - 1]
        if c != len(solution[0]) - 1:
            adj_hors |= solution[r][c + 1]

        if not adj_hors & DirSeleccion.bend_dir:
            solution[r][c] = DirSeleccion.vertical_dir

        print(solution)
        print("..............................................................................................")
    

    
    # la celda actual (solution[r][c]) tiene la dirección horizontal (DirSeleccion.horizontal_dir).
    if solution[r][c] == DirSeleccion.horizontal_dir:
        print("...................................celda en horizontal.....................................................")

        #Esto ajusta las posibles direcciones de las celdas a la izquierda (c - 1) y a la derecha (c + 1). La celda a la izquierda (c - 1) debe tener una dirección que continúe hacia la derecha (DirSeleccion.right_dir), y la celda a la derecha (c + 1) debe tener una dirección que continúe hacia la izquierda (DirSeleccion.left_dir).
        solution[r][c - 1] &= DirSeleccion.right_dir
        solution[r][c + 1] &= DirSeleccion.left_dir

        #Si hay celdas en la fila superior (r - 1) o en la fila inferior (r + 1), se eliminan las direcciones que apuntan hacia abajo (DirSeleccion.down_dir) y hacia arriba (DirSeleccion.up_dir) respectivamente
        if r != 0:
            solution[r - 1][c] -= DirSeleccion.down_dir
        if r != len(solution) - 1:
            solution[r + 1][c] -= DirSeleccion.up_dir

        # Si la celda a la izquierda (c - 1) no puede doblarse (bend_dir), entonces la celda a la derecha (c + 1) debe doblarse (bend_dir).
        if not solution[r][c - 1] & DirSeleccion.bend_dir:
            solution[r][c + 1] &= DirSeleccion.bend_dir
        # De manera similar, si la celda a la derecha (c + 1) no puede doblarse (bend_dir), entonces la celda a la izquierda (c - 1) debe doblarse (bend_dir).
        if not solution[r][c + 1] & DirSeleccion.bend_dir:
            solution[r][c - 1] &= DirSeleccion.bend_dir

        print(solution)
        print(".......................................................................................................................")

    # la celda actual (solution[r][c]) tiene la dirección vertical (DirSeleccion.vertical_dir).
    if solution[r][c] == DirSeleccion.vertical_dir:
        print("....................................................celda en vertical.................................................")

        #posibles direcciones de las celdas arriba (r - 1) y abajo (r + 1). La celda arriba debe tener una dirección que continúe hacia abajo (DirSeleccion.down_dir), y la celda abajo debe tener una dirección que continúe hacia arriba (DirSeleccion.up_dir)
        solution[r - 1][c] &= DirSeleccion.down_dir
        solution[r + 1][c] &= DirSeleccion.up_dir

        #Si hay celdas a la izquierda (c - 1) o a la derecha (c + 1), se eliminan las direcciones que apuntan hacia la derecha (DirSeleccion.right_dir) y hacia la izquierda (DirSeleccion.left_dir) respectivamente.
        if c != 0:
            solution[r][c - 1] -= DirSeleccion.right_dir
        if c != len(solution[0]) - 1:
            solution[r][c + 1] -= DirSeleccion.left_dir

        # Si la celda arriba (r - 1) no puede doblarse (bend_dir), entonces la celda abajo (r + 1) debe doblarse (bend_dir).
        if not solution[r - 1][c] & DirSeleccion.bend_dir:
            solution[r + 1][c] &= DirSeleccion.bend_dir
        # De manera similar, si la celda abajo (r + 1) no puede doblarse (bend_dir), entonces la celda arriba (r - 1) debe doblarse (bend_dir).
        if not solution[r + 1][c] & DirSeleccion.bend_dir:
            solution[r - 1][c] &= DirSeleccion.bend_dir
        print(".......................................................................................................................")
    
    return solution




def apply_black_rule(solution, r, c):
    # Esta condición verifica si la celda actual (solution[r][c]) tiene más de una posible dirección. Si solo tiene una dirección, ya está determinada y no necesita más restricciones.
    if len(solution[r][c]) > 1:

        # Si hay una celda arriba (r > 0), se verifica si esa celda tiene una dirección vertical (DirSeleccion.vertical_dir). Si no la tiene, se elimina la posibilidad de que la celda actual tenga una dirección hacia arriba (DirSeleccion.up_dir). Además, se verifica la celda dos filas arriba (r - 2): si no tiene una dirección hacia abajo (DirSeleccion.down_dir), 
        print("...................celda superior...........................................")
        print(solution[r][c])
        if r > 0:
            if not solution[r - 1][c] & DirSeleccion.vertical_dir:
                solution[r][c] -= DirSeleccion.up_dir
            elif r > 1 and not solution[r - 2][c] & DirSeleccion.down_dir:
                solution[r][c] -= DirSeleccion.up_dir
        print("...................................................................................")


        #se verifica la celda abajo (r + 1). Si no tiene una dirección vertical, se elimina la posibilidad de que la celda actual tenga una dirección hacia abajo. Si la celda dos filas abajo (r + 2) no tiene una dirección hacia arriba, también se elimina la posibilidad de que la celda actual tenga una dirección hacia abajo.
        print(solution[r][c])
        if r < len(solution) - 1:
            print("............celda inferior..................................................")
            print(solution[r][c])

            if not solution[r + 1][c] & DirSeleccion.vertical_dir:
                solution[r][c] -= DirSeleccion.down_dir
            elif r < len(solution) - 2 and not solution[r + 2][c] & DirSeleccion.up_dir:
                solution[r][c] -= DirSeleccion.down_dir
            print("....................................................................")

        #Si hay una celda a la izquierda (c > 0), se verifica si esa celda tiene una dirección horizontal (DirSeleccion.horizontal_dir). Si no la tiene, se elimina la posibilidad de que la celda actual tenga una dirección hacia la izquierda (DirSeleccion.left_dir). Si la celda dos columnas a la izquierda (c - 2) no tiene una dirección hacia la derecha (DirSeleccion.right_dir),

        if c > 0:
            print(".....................................celda izquierda.....................................")
            print(solution[r][c])
            if not solution[r][c - 1] & DirSeleccion.horizontal_dir:
                solution[r][c] -= DirSeleccion.left_dir
            elif c > 1 and not solution[r][c - 2] & DirSeleccion.right_dir:
                solution[r][c] -= DirSeleccion.left_dir
            print(".......................................................................................................")

        #De manera similar, se verifica la celda a la derecha (c + 1). Si no tiene una dirección horizontal, se elimina la posibilidad de que la celda actual tenga una dirección hacia la derecha. Si la celda dos columnas a la derecha (c + 2) no tiene una dirección hacia la izquierda, también se elimina la posibilidad de que la celda actual tenga una dirección hacia la derecha.
        if c < len(solution[0]) - 1:
            print("..............................................celda derecha...............................................")
            print(solution[r][c])
            if not solution[r][c + 1] & DirSeleccion.horizontal_dir:
                solution[r][c] -= DirSeleccion.right_dir
            elif c < len(solution[0]) - 2 and not solution[r][c + 2] & DirSeleccion.left_dir:
                solution[r][c] -= DirSeleccion.right_dir

            print("................................................................................................................")

    # Restriccioned de acuerdo a la posicion en la que se encuentra

    if solution[r][c] == DirSeleccion.down_dir:
        print("...........................................Dirección Abajo .............................................")
        print(solution[r][c])
        #solution[r + 1][c] &= DirSeleccion.vertical_dir: Asegura que la celda inmediatamente abajo (r + 1, c) solo permita direcciones verticales.
        solution[r + 1][c] &= DirSeleccion.vertical_dir
        #solution[r + 2][c] &= DirSeleccion.up_dir: Asegura que la celda dos filas abajo (r + 2, c) solo permita la dirección hacia arriba.
        solution[r + 2][c] &= DirSeleccion.up_dir
        #if r > 0: solution[r - 1][c] -= DirSeleccion.down_dir: Si no está en la primera fila, elimina la dirección hacia abajo de la celda de arriba.
        if r > 0:
            solution[r - 1][c] -= DirSeleccion.down_dir
        #if {Constantes.UP_RIGHT}.issubset(solution[r][c]): Si la celda actual contiene UP_RIGHT, elimina la dirección izquierda de la celda diagonal inferior derecha (r + 1, c + 1).
        if {Constantes.UP_RIGHT}.issubset(solution[r][c]):
            solution[r + 1][c + 1] -= DirSeleccion.left_dir
        #if {Constantes.RIGHT_DOWN}.issubset(solution[r][c]): Si la celda actual contiene RIGHT_DOWN, elimina la dirección derecha de la celda diagonal inferior izquierda (r + 1, c - 1).
        if {Constantes.RIGHT_DOWN}.issubset(solution[r][c]):
            solution[r + 1][c - 1] -= DirSeleccion.right_dir

        print("................................................................................................................")

    if solution[r][c] == DirSeleccion.left_dir:
        print("...........................................Dirección Izquierda .............................................")

        print(solution[r][c])
        #Asegura que la celda inmediatamente a la izquierda (r, c - 1) solo permita direcciones horizontales.
        solution[r][c - 1] &= DirSeleccion.horizontal_dir
        #Asegura que la celda dos columnas a la izquierda (r, c - 2) solo permita la dirección hacia la derecha.
        solution[r][c - 2] &= DirSeleccion.right_dir
        #Si no está en la última columna, elimina la dirección hacia la izquierda de la celda de la derecha.
        if c < len(solution[0]) - 1:
            solution[r][c + 1] -= DirSeleccion.left_dir
        #Si la celda actual contiene RIGHT_DOWN, elimina la dirección hacia arriba de la celda diagonal inferior izquierda (r + 1, c - 1).
        if {Constantes.RIGHT_DOWN}.issubset(solution[r][c]):
            solution[r + 1][c - 1] -= DirSeleccion.up_dir
        #Si la celda actual contiene DOWN_LEFT, elimina la dirección hacia abajo de la celda diagonal superior izquierda (r - 1, c - 1).
        if {Constantes.DOWN_LEFT}.issubset(solution[r][c]):
            solution[r - 1][c - 1] -= DirSeleccion.down_dir
        print("................................................................................................................")
    
    if solution[r][c] == DirSeleccion.up_dir:
        print("...........................................Dirección Arriba .............................................")
        print(solution[r][c])
        #Asegura que la celda inmediatamente arriba (r - 1, c) solo permita direcciones verticales.
        solution[r - 1][c] &= DirSeleccion.vertical_dir
        #Asegura que la celda dos filas arriba (r - 2, c) solo permita la dirección hacia abajo.
        solution[r - 2][c] &= DirSeleccion.down_dir
        
        #Si no está en la última fila, elimina la dirección hacia arriba de la celda de abajo.
        if r < len(solution) - 1:
            solution[r + 1][c] -= DirSeleccion.up_dir
        #Si la celda actual contiene DOWN_LEFT, elimina la dirección derecha de la celda diagonal superior izquierda (r - 1, c - 1).
        if {Constantes.DOWN_LEFT}.issubset(solution[r][c]):
            solution[r - 1][c - 1] -= DirSeleccion.right_dir
        #Si la celda actual contiene LEFT_UP, elimina la dirección izquierda de la celda diagonal superior derecha (r - 1, c + 1).
        if {Constantes.LEFT_UP}.issubset(solution[r][c]):
            solution[r - 1][c + 1] -= DirSeleccion.left_dir
        print("................................................................................................................")

    
    
    if solution[r][c] == DirSeleccion.right_dir:
        print("...........................................Dirección derecha .............................................")
        print(solution[r][c])
        #Asegura que la celda inmediatamente a la derecha (r, c + 1) solo permita direcciones horizontales.
        solution[r][c + 1] &= DirSeleccion.horizontal_dir
        #Asegura que la celda dos columnas a la derecha (r, c + 2) solo permita la dirección hacia la izquierda.
        solution[r][c + 2] &= DirSeleccion.left_dir
        #Si no está en la primera fila, elimina la dirección hacia la derecha de la celda de la izquierda.
        if r > 0:
            solution[r][c - 1] -= DirSeleccion.right_dir
        # Si la celda actual contiene UP_RIGHT, elimina la dirección hacia arriba de la celda diagonal inferior derecha (r + 1, c + 1).
        if {Constantes.UP_RIGHT}.issubset(solution[r][c]):
            solution[r + 1][c + 1] -= DirSeleccion.up_dir
        # Si la celda actual contiene UP_RIGHT, elimina la dirección hacia abajo de la celda diagonal superior derecha (r - 1, c + 1).
        if {Constantes.UP_RIGHT}.issubset(solution[r][c]):
            solution[r - 1][c + 1] -= DirSeleccion.down_dir
        
        print("................................................................................................................")

    
    
    return solution

def filter_adj(solution, r, c, num_filas, num_columnas):


    
    if solution == {Constantes.NO_VECINOS}:
            print("...........................................filter adj .............................................")
            print(solution[r][c])
            #Si la celda adyacente está arriba (r != 0)
            if r != 0:
            #Se elimina la posibilidad de que la celda de arriba (solution[r - 1][c]) tenga una dirección hacia abajo (DirSeleccion.down_dir).
                solution[r - 1][c] -= DirSeleccion.down_dir
            #Si la celda adyacente está a la izquierda (c != 0)
            if c != 0:
            #Se elimina la posibilidad de que la celda de la izquierda (solution[r][c - 1]) tenga una dirección hacia la derecha (DirSeleccion.right_dir).
                solution[r][c - 1] -= DirSeleccion.right_dir
            #Si la celda adyacente está abajo (r != num_filas - 1)
            if r != num_filas - 1:
            #Se elimina la posibilidad de que la celda de abajo (solution[r + 1][c]) tenga una dirección hacia arriba (DirSeleccion.up_dir).
                solution[r + 1][c] -= DirSeleccion.up_dir
            #Si la celda adyacente está a la derecha (c != num_columnas - 1):
            if c != num_columnas - 1:
                #Se elimina la posibilidad de que la celda de la derecha (solution[r][c + 1]) tenga una dirección hacia la izquierda (DirSeleccion.left_dir).
                solution[r][c + 1] -= DirSeleccion.left_dir

    elif solution[r][c] == {Constantes.ESQUINA}:
            print("...........................................filter adj .............................................")
            print(solution[r][c])
            # restrict left and up
            if r != 0:
                #Si la celda actual no está en la primera fila (r != 0), se elimina la dirección down_dir de la celda directamente arriba de la celda actual (solution[r - 1][c]). 
                solution[r - 1][c] -= DirSeleccion.down_dir
            if c != 0:
                #Si la celda actual no está en la primera columna (c != 0), se elimina la dirección right_dir de la celda directamente a la izquierda de la celda actual (solution[r][c - 1]).
                solution[r][c - 1] -= DirSeleccion.right_dir

            #La celda directamente abajo de la celda actual (solution[r + 1][c]) debe tener una conexión hacia arriba (up_dir).
            if r < num_filas - 1:
             solution[r + 1][c] &= DirSeleccion.up_dir

            #La celda directamente a la derecha de la celda actual (solution[r][c + 1]) debe tener una conexión hacia la izquierda (left_dir).
            if c < num_columnas - 1:
             solution[r][c + 1] &= DirSeleccion.left_dir

        
    elif solution[r][c] == {Constantes.AL_LADO}:
            print("...........................................filter adj .............................................")
            print(solution[r][c])
            # restrict right and up
            if r != 0:
                solution[r - 1][c] -= DirSeleccion.down_dir
            if c != num_columnas - 1:
                solution[r][c + 1] -= DirSeleccion.left_dir

            # must go down and left
            if r < num_filas - 1:
             solution[r + 1][c] &= DirSeleccion.up_dir
            if c != 0:
             solution[r][c - 1] &= DirSeleccion.right_dir
            
        # if current cell is shape 3
    elif solution[r][c] == {Constantes.VERTICAL}:
            print("...........................................filter adj .............................................")
            print(solution[r][c])
            # restrict down and right
            if r != num_filas - 1:
                solution[r + 1][c] -= DirSeleccion.up_dir
            if c != num_columnas - 1:
                solution[r][c + 1] -= DirSeleccion.left_dir

            # must go up and left
            solution[r - 1][c] &= DirSeleccion.down_dir
            solution[r][c - 1] &= DirSeleccion.right_dir

        # if current cell is shape 4
    elif solution[r][c] == {Constantes.UP_RIGHT}:
            print("...........................................filter adj .............................................")
            print(solution[r][c])
            # restrict left and down
            if r != num_filas - 1:
                solution[r + 1][c] -= DirSeleccion.up_dir
            if c != 0:
                solution[r][c - 1] -= DirSeleccion.right_dir

            # must go up and right
            solution[r - 1][c] &= DirSeleccion.down_dir
            solution[r][c + 1] &= DirSeleccion.left_dir

        # if current cell is shape 5
    elif solution[r][c] == {Constantes.RIGHT_DOWN}:
            print("...........................................filter adj .............................................")
            print(solution[r][c])
            # restrict up and down
            if r != 0:
                solution[r - 1][c] -= DirSeleccion.down_dir
            if r != num_filas - 1:
                solution[r + 1][c] -= DirSeleccion.up_dir

            # must go left and right
            solution[r][c - 1] &= DirSeleccion.right_dir
            solution[r][c + 1] &= DirSeleccion.left_dir

        # if current cell is shape 6
    elif solution[r][c] == {Constantes.DOWN_LEFT}:
            print("...........................................filter adj .............................................")
            print(solution[r][c])
            # restrict left and right
            if c != 0:
                solution[r][c - 1] -= DirSeleccion.right_dir
            if c != num_columnas - 1:
                solution[r][c + 1] -= DirSeleccion.left_dir

            # must go up and down
            solution[r - 1][c] &= DirSeleccion.down_dir
            solution[r + 1][c] &= DirSeleccion.up_dir