def find_words(m):
    frontier = []
    res = []

    valid_words = {'FOAM', 'MASS', 'BEAR', 'DOOR'}
    for r in range(len(m)):
        for c in range(len(m)):
            frontier.append(((r, c), m[r][c]))

    while len(frontier):
        (r, c), word = frontier.pop()

        if word in valid_words:
            res.append(word)

        for d_r, d_c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            n_r = r + d_r
            n_c = c + d_c

            if n_r < 0 or n_r >= len(m) or n_c < 0 or n_c >= len(m):
                continue

            n_word = word + m[n_r][n_c]
            valid_prefix = False
            for w in valid_words:
                if n_word == w[:len(n_word)]:
                    valid_prefix = True
                    break
            if valid_prefix:
                frontier.append(((n_r, n_c), word + m[n_r][n_c]))

    return res


m = [['F', 'A', 'C', 'I'], ['O', 'B', 'Q', 'P'], ['A', 'N', 'O', 'B'],
     ['M', 'A', 'S', 'S']]
print(find_words(m))
