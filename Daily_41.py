def find_path(start, connections):
    res = []
    frontier = [[(start,), set(connections)]]

    while frontier:
        path, conns = frontier.pop()

        orig = path[-1]
        if len(conns) == 0:
            res.append(path)

        for x in conns:
            conn_orig, conn_dest = x
            if orig == conn_orig:
                frontier.append([path + (conn_dest,), conns.difference([x])])

    if len(res) == 0:
        return None
        
    return sorted(res)[0]

print find_path('YUL', [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')])
print find_path('COM', [('SFO', 'COM'), ('COM', 'YYZ')])
print find_path('A', [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')])
