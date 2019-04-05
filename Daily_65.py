from itertools import cycle


def is_valid(current, m, visited):
    if current in visited:
        return False
    r, c = current
    if r < 0 or c < 0 or r >= len(m) or c >= len(m[0]):
        return False

    return True


def isValid(position, d, visited, m, n):
    next_x = position[0] + d[0]
    next_y = position[1] + d[1]

    if (next_x, next_y) in visited or next_x < 0 or next_y < 0 or\
       next_x >= m or next_y >= n:
        return False

    return True


def spiralMatrix(mat):
    m = len(mat)
    n = len(mat[0])

    res = []
    visited = set()
    current = (0, 0)
    directions = cycle([(0, 1), (1, 0), (0, -1), (-1, 0)])

    for _ in range((m * 2) - 1):
        d = next(directions)

        while isValid(current, d, visited, m, n):
            visited.add(current)
            res.append(mat[current[0]][current[1]])

            current = current[0] + d[0], current[1] + d[1]

    res.append(mat[current[0]][current[1]])
    return res


def _spiral_matrix(m):
    res = []
    visited = set()
    current = (0, 0)

    directions = cycle([(0, 1), (1, 0), (0, -1), (-1, 0)])
    r_d, c_d = next(directions)

    added = True
    while added:
        added = False
        while is_valid(current, m, visited):
            r, c = current
            res.append(m[r][c])
            added = True
            visited.add(current)
            current = r + r_d, c + c_d

        current = current[0] - r_d, current[1] - c_d
        r_d, c_d = next(directions)
        current = current[0] + r_d, current[1] + c_d

    return res


def spiral_matrix(mat):
    n = len(mat)
    m = len(mat[0])

    res = []
    current = (0, 0)
    dirs = cycle([(0, 1), (1, 0), (0, -1), (-1, 0)])
    t = 0

    while (n - t) > 1:
        for _ in range(n - t - 1):
            d = next(dirs)
            z = abs(d[0] * n) + abs(d[1] * m) - t
            for _ in range(z - 1):
                r, c = current
                res.append(mat[r][c])
                current = r + d[0], c + d[1]
        t += 1
    d = next(dirs)
    z = abs(d[0] * n) + abs(d[1] * m) - t
    for _ in range(z + 1):
        r, c = current
        res.append(mat[r][c])
        current = r + d[0], c + d[1]

    return res


m = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
     [16, 17, 18, 19, 20]]
# print(spiral_matrix(m))
print(spiralMatrix(m))
m = [range(1, 5), range(5, 9), range(9, 13), range(13, 17)]
# print(spiral_matrix(m))
print(spiralMatrix(m))
