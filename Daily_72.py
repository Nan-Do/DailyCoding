# General way of solving: Cost (n2 * e)
# Compute DFS/BFS starting on each letter/node while storing the sequence of letters of
# each possible path, when we arrive to the end of the path check the number of letters
# are equal to the first one (of the path).
# If we hit a loop discard that path.
def find_largest_path(chars, edges):
    longest_paths = {}
    frontier = []

    for pos, char in enumerate(chars):
        longest_paths[pos] = -1
        frontier.append((pos, pos, ''))

    while frontier:
        current, start, path = frontier.pop()

        # There is a loop:
        #  - We reach again the starting position
        #  (If the path is empty we can't reach the starting position again)
        if current == start and len(path) > 0:
            longest_paths[start] = -1
            continue

        # Check successors
        has_successors = False
        for edge in edges:
            if edge[0] == current:
                frontier.append((edge[1], start, path + chars[current]))
                has_successors = True

        # We reached the end of the path check its length
        if not has_successors and len(path) > 0:
            total = path.count(path[0])
            # We didn't add the current char to the path yet so we have
            # to check if it is equal to the the start of the path
            # to compute the length correctly.
            if chars[current] == path[0]:
                total += 1
            if total > longest_paths[start]:
                longest_paths[start] = total

    max_path = max(longest_paths.values())
    if max_path == -1:
        return None

    return max_path


print(find_largest_path('ABACA', [(0, 1), (0, 2), (2, 3), (3, 4)]))
print(find_largest_path('A', [(0, 0)]))
