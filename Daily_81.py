# Recursive top down solution for each number we usge the first number and recurse on the rest
# then we combine the solutions by adding each character to first number can be mapped to with all
# the previous computed solutions.
# Cost: Exponential (length of the mapping ^ length of the number)
def generate_strings(mapping, number):
    res = []

    if len(number) == 0:
        return ['']

    temp_list = generate_strings(mapping, number[1:])
    for char in mapping[number[0]]:
        res += list(map(lambda x: char + x, temp_list))

    return res


# Iterative solution, python doesn't like recursion too much and the previous solution is not
# tail recursive.
def generate_strings2(mapping, number):
    res = []
    frontier = [('', number)]

    while frontier:
        c_string, c_number = frontier.pop()

        if len(c_number) == 0:
            res.append(c_string)
            continue

        for x in mapping[c_number[0]]:
            frontier.append((c_string + x, c_number[1:]))

    return res


m = {"2": ['a', 'b', 'c'], "3": ['d', 'e', 'f']}
print(generate_strings(m, "23"))
