def valid_coloring(m, colors, v):
    vertex_color = colors[v]

    for succ in range(len(m)):
        if m[v][succ] == 1 and colors[succ] == vertex_color:
            return False

    return True


def _graph_colouring(m, k, colors, v):
    if v == len(m):
        return True

    for c in range(1, k + 1):
        colors[v] = c
        if valid_coloring(m, colors, v):
            return _graph_colouring(m, k, colors, v + 1)
        colors[v] = 0

    return False


def graph_colouring(m, k):
    colors = [0] * len(m)

    if _graph_colouring(m, k, colors, 0) is False:
        print("No solution")
    else:
        print(colors)


graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
k = 3
graph_colouring(graph, k)
k = 2
graph_colouring(graph, k)
