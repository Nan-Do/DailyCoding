def find_paths(n):
    total_paths = 0
    frontier = []
    total_sqares = n * n

    for r in range(n):
        for c in range(n):
            pos = (r, c)
            frontier.append((pos, set()))

    while frontier:
        current, visited = frontier.pop()

        visited.add(current)
        if len(visited) == total_sqares:
            total_paths += 1
            continue

        r, c = current
        for d_r, d_c in [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2),
                         (1, -2), (1, 2)]:
            n_r = r + d_r
            n_c = c + d_c

            new_pos = (n_r, n_c)
            if n_r < 0 or n_r >= n or n_c < 0 or n_c >= n or new_pos in visited:
                continue

            frontier.append((new_pos, visited))

    return total_paths


# print(find_paths(3))
# print(find_paths(4))
# print(find_paths(5))
# print(find_paths(10))
# print(find_paths(15))
print(find_paths(24))
