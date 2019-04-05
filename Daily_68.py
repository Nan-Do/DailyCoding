def compute_bishops(bishops, M):
    total = 0
    for x in range(0, len(bishops)):
        for y in range(x + 1, len(bishops)):
            c1, c2 = bishops[x]
            d1, d2 = bishops[y]

            if abs(c1 - d1) == abs(c2 - d2):
                total += 1

    return total


def compute_bishops2(bishops, M):
    total = 0
    bishops = set(bishops)

    for x, y in bishops:
        for c in range(1, M):
            if (x + c, y + c) in bishops:
                total += 1
            if (x - c, y + c) in bishops:
                total += 1
            if (x + c, y - c) in bishops:
                total += 1
            if (x - c, y - c) in bishops:
                total += 1

    return total / 2


print(compute_bishops([(0, 0), (1, 2), (2, 2), (4, 0)], 5))
print(compute_bishops2([(0, 0), (1, 2), (2, 2), (4, 0)], 5))
