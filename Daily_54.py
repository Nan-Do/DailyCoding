def get_free_positions(sudoku):
    free_positions = []
    for r in range(9):
        for c in range(9):
            if sudoku[r][c] == -1:
                free_positions.append((r, c))
    return free_positions


def get_square_val(position):
    r = position[0]
    c = position[1]

    ri = 0
    re = 3
    if r >= 3 and r <= 5:
        ri = 3
        re = 6
    if r >= 6 and r <= 8:
        ri = 6
        re = 9

    ci = 0
    ce = 3
    if c >= 3 and c <= 5:
        ci = 3
        ce = 6
    if c >= 6 and c <= 8:
        ci = 6
        ce = 9

    return ri, re, ci, ce


def get_possible_values(sudoku, position):
    values = set(range(1, 10))

    r = position[0]
    c = position[1]

    values = values.difference(sudoku[r])
    for x in range(9):
        values.discard(sudoku[x][c])

    ri, re, ci, ce = get_square_val(position)
    for x in range(ri, re):
        for y in range(ci, ce):
            values.discard(sudoku[x][y])

    return iter(values)


def check_board(sudoku, position, value):
    r = position[0]
    c = position[1]

    for v in range(9):
        if sudoku[r][v] == value or\
           sudoku[v][c] == value:
            return False

    ri, re, ci, ce = get_square_val(position)
    for x in range(ri, re):
        for y in range(ci, ce):
            if sudoku[x][y] == value:
                return False

    return True


def sudoku_solver(sudoku):
    free_positions = get_free_positions(sudoku)

    pos = 0
    positions_generator = {}
    while True and len(free_positions):
        position = free_positions[pos]

        if position not in positions_generator or \
           positions_generator[position] is None:
            positions_generator[position] = get_possible_values(
                sudoku, position)

        try:
            value = next(positions_generator[position])
        except StopIteration:
            if pos == 0:
                return False
            else:
                positions_generator[position] = None
                sudoku[position[0]][position[1]] = -1
                pos -= 1
                continue

        if check_board(sudoku, position, value):
            sudoku[position[0]][position[1]] = value
            pos += 1
            if pos == len(free_positions):
                return True
        else:
            if pos > 0:
                sudoku[position[0]][position[1]] = -1
                positions_generator[position] = None
                pos -= 1

    return True


# sudoku = [[1,5,2,4,8,9,3,7,6],
#           [7,3,9,2,5,6,8,4,1],
#           [4,6,8,3,7,1,2,9,5],
#           [3,8,7,1,2,4,6,5,9],
#           [5,9,1,7,6,3,4,2,8],
#           [2,4,6,8,9,5,7,1,3],
#           [9,1,4,6,3,7,5,8,2],
#           [6,2,5,9,4,8,1,3,7],
#           [8,7,3,5,1,2,9,6,4]]

sudoku = [[-1, 5, 2, -1, -1, 9, -1, -1, -1], [7, 3, -1, 2, -1, -1, -1, -1, 1],
          [-1, 6, -1, -1, 7, 1, -1, -1, 5], [-1, -1, -1, 1, -1, -1, 6, -1, 9],
          [-1, -1, 1, -1, 6, -1, 4, 2, -1], [-1, -1, 6, -1, 9, -1, 7, 1, 3],
          [-1, 1, -1, 6, -1, -1, 5, -1, -1], [6, -1, -1, -1, 4, -1, 1, -1, -1],
          [-1, -1, 3, -1, 1, -1, -1, 6, 4]]

for r in sudoku:
    print(" ".join(map(str, r)))
print(sudoku_solver(sudoku))
for r in sudoku:
    print(" ".join(map(str, r)))
