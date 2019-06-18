def valid_prefix(word, words):
    for w in words:
        if word == w[0:len(word)]:
            return True
    return False


# Cost: O(n^4)
# Algorithm: Starting with each position of the Matrix do a BFS
# checking at each step if the computed path can lead to a valid word
def boggle(mat, words):
    frontier = []
    res = []

    for r in range(len(mat)):
        for c in range(len(mat[0])):
            elem = ((r, c), mat[r][c])
            frontier.append(elem)

    while frontier:
        pos, word = frontier.pop()

        if word in words:
            res.append(word)
            continue

        if not valid_prefix(word, words):
            continue

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            n_x = pos[0] + dx
            n_y = pos[1] + dy
            if n_x < 0 or n_x >= len(mat) or n_y < 0 or n_y >= len(mat[0]):
                continue
            elem = ((n_x, n_y), word + mat[n_x][n_y])
            frontier.append(elem)

    return res


mat =\
[
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
]
words = set(['SEE', 'ESE', 'ASA', 'DEE'])
print(boggle(mat, words))
