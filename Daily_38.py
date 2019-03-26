def is_valid(sol, N):
    x, y = sol[-1]
    positions = set(sol[:-1])

    for r in xrange(N+1):
        # check row
        if (x, y-r) in positions:
            return False

        # check diagonals
        if (x - r, y - r) in positions:
            return False
        if (x + r, y - r) in positions:
            return False

    return True


def place_queens(sol, col, N):
    if len(sol) == N:
        print sol

    for x in xrange(N):
        sol.append((x, col))

        if is_valid(sol, col):
            place_queens(sol, col+1, N)

        sol.pop()


place_queens([], 0, 11)
