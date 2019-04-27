# Cost m*n (n^2) if it is a squared matrix
# Algorithm:
# Get all the possible starting position for the islands.
# For each one of those positions do the following:
#  If the position hasn't been marked update the number of islands
#  Mark all the contigous positions.
# Notes:
#  Use a copy of the matrix to keep track of which positions have been visited
#  The possible starting positions must be visited in increasing order.
# This works because the invariant assures us that if we find a position that can
# be a island and hasn't been marked before is a new island.
# Another possible algorithm would be to check each 1 positon of the matrix; for each one
# that hasn't been marked before start a bfs marking all the possible elements along the way.
def compute_islands(mat):
    total_islands = 0
    c_m = [[0] * len(mat[x]) for x in range(len(mat))]

    frontier = []
    for r in range(len(mat)):
        for c in range(len(mat[r])):
            if mat[r][c] == 1:
                frontier.append((r, c))

    while len(frontier):
        r, c = frontier.pop(0)

        if c_m[r][c] == 0:
            total_islands += 1

        for d_r in [-1, 0, 1]:
            for d_c in [-1, 0, 1]:
                n_r = r + d_r
                n_c = c + d_c
                if n_r >= 0 and n_r < len(mat) and\
                   n_c >= 0 and n_c < len(mat[0]):
                    c_m[n_r][n_c] = 1

    return total_islands


m = [[1, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0],
     [1, 1, 0, 0, 1], [1, 1, 0, 0, 1]]
print(compute_islands(m))
