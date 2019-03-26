def get_live_cells(matrix):
    positions = set()

    for r in xrange(len(matrix)):
        for c in xrange(len(matrix[r])):
            if matrix[r][c] == '*':
                positions.add((r, c))

    return positions


def get_live_neighs(r, c, positions):
    total = 0

    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if x == 0 and y == 0:
                continue

            if (r + x, c + y) in positions:
                total += 1

    return total

            
def game_of_life(init_state):
    current = init_state

    while True:
        new_state = [['.'] * len(current[0]) for _ in xrange(len(current))] 
        positions = get_live_cells(current)

        for r in xrange(len(current)):
            for c in xrange(len(current[r])):
                neighs = get_live_neighs(r, c, positions)

                current_cell = current[r][c]
                cell = '.' 
                if current_cell == '*' and neighs == 2:
                    cell = '*'
                if neighs == 3:
                    cell = '*'

                new_state[r][c] = cell

        current = new_state
        yield current


init_state = [['*','.','*','.'], ['.','*','*','.'], ['*','.','.','*']]
print '\n'.join(map(lambda x: ''.join(x), init_state))
print '\n'
i = game_of_life(init_state)
for _ in xrange(5):
    m = i.next()
    print '\n'.join(map(lambda x: ''.join(x), m))
    print '\n'
