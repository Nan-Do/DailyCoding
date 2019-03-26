def distance(x, y, m, n):
    if m == 0: return n
    if n == 0: return m

    if x[m] == y[n]:
        return distance(x, y, m-1, n-1)
    else:
        return min(distance(x, y, m-1, n),
                   distance(x, y, m, n-1)) + 1

print distance('kitten', 'sitting', 5, 6)
