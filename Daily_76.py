def get_chunks(seq, size, step=1):
    for x in range(len(seq) - size + step):
        yield seq[x:x + size]


# THE DESCRIPTION CONTAINS MANY DETAILS BE SURE YOU
# UNDERSTAND THEM ALL BEFORE START CODING.
# Cost: Worst case (n^2). If we always have to remove a column
# on the last pair of rows we iterate the matrix n + n-1 + ... + 1
# The algorithm is overall easy to understand but tedious to implement,
# specially the details regarding where to update the column index
# and updating the matrix can be tricky, pay extra attention to those.
#
# The solving algorithm works as follows:
# - Iterate the matrix in pairs of rows.
# - For each pair of rows check that the characters are ordered lexicographically.
# - If the characters are not sorted mark the column, remove it from the matrix and
# - start all over again.
def rows_to_remove(mat):
    total = 0

    removed = True
    while removed:
        removed = False
        # Functional approach vs normal iteration.
        # for r1, r2 in get_chunks(mat, 2):
        for x in range(len(mat) - 1):
            r1 = mat[x]
            r2 = mat[x + 1]

            column = 0
            for c1, c2 in zip(r1, r2):
                if c1 > c2:
                    removed = True
                    break
                column += 1
            if removed:
                break

        if removed:
            total += 1
            temp_m = []
            for row in mat:
                temp_m.append(row[:column] + row[column + 1:])
            mat = temp_m

    return total, mat


m = [['c', 'b', 'a'], ['d', 'a', 'f'], ['g', 'h', 'i']]
print(rows_to_remove(m))
m = [['a', 'b', 'c', 'd', 'e', 'f']]
print(rows_to_remove(m))
m = [['z', 'y', 'x'], ['w', 'v', 'u'], ['t', 's', 'r']]
print(rows_to_remove(m))
