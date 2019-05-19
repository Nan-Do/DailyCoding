dirs = {
    'NW': (0, 0),
    'N': (0, 1),
    'NE': (0, 2),
    'W': (1, 0),
    'E': (1, 2),
    'SW': (2, 0),
    'S': (2, 1),
    'SE': (2, 2)
}

opposites = {
    'NW': 'SE',
    'N': 'S',
    'NE': 'SW',
    'W': 'E',
    'E': 'W',
    'SW': 'NE',
    'S': 'N',
    'SE': 'NW',
}


def interpret_rule(rule):
    letter1_1 = rule[2]
    letter1_2 = rule[0]
    dir1 = dirs[rule[1]]

    letter2_1 = rule[0]
    letter2_2 = rule[2]
    dir2 = dirs[opposites[rule[1]]]

    return ((letter1_1, letter1_2, dir1), (letter2_1, letter2_2, dir2))


def valid_north(letter1, north_pos, positions):
    letters = list(filter(lambda x: x is not None, north_pos))

    if len(letters) == 0:
        return True
    if letter1 in letters:
        return False

    for l in letters:
        if l not in positions:
            continue

        if not valid_north(letter1, positions[l][0], positions):
            return False

    return True


def valid_west(letter1, west_pos, positions):
    letters = list(filter(lambda x: x is not None, west_pos))

    if len(letters) == 0:
        return True
    if letter1 in letters:
        return False

    for l in letters:
        if l not in positions:
            continue

        west_next = map(lambda x: x[2], positions)
        if not valid_west(letter1, west_next, positions):
            return False

    return True


def are_rules_valid(rules):
    positions = dict()

    for rule in rules:
        for x in interpret_rule(rule):
            letter1, letter2, pos = x

            if letter1 not in positions:
                positions[letter1] = [[None] * 3 for _ in range(3)]

            mat = positions[letter1]

            if mat[pos[0]][pos[1]] is not None:
                return False
            mat[pos[0]][pos[1]] = letter2

        if not valid_north(letter1, mat[0], positions):
            return False
        w = map(lambda x: x[2], mat)
        if not valid_north(letter1, w, positions):
            return False

    print(positions)
    return True


rules = [['A', 'NE', 'B'], ['A', 'SW', 'C']]
print(are_rules_valid(rules))
rules = [['A', 'N', 'B'], ['B', 'NE', 'C'], ['C', 'N', 'A']]
print(are_rules_valid(rules))
