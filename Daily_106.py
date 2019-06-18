# Cost Exponential max_hop ^ n
# Recursive function to solve the problem
def jump(index, s):
    if index >= len(s) - 1:
        return True

    r = []
    hops = s[index]
    if hops == 0:
        return False

    for x in range(1, hops + 1):
        r.append(jump(index + x, s))

    return any(r)


# Cost O(n)
# We can take advantage that at every point we can compute the position that will
# make us advance the most. We can compute this using the fact that index + hops (s[index])
# will tell us the furthest position we can reach from any given index.
# Therefore, given a position we can compute the next best position.
# If at any given time we get stuck in a position we can't advance any further return False
def jump_it(s):
    current = 0

    while current < len(s) - 1:
        hops = s[current]
        next_index = max_pos = 0

        if current + hops >= len(s) - 1:
            return True

        for x in range(1, hops + 1):
            n = current + x
            if s[n] > 0:
                if s[n] + n > max_pos:
                    max_pos = s[n] + n
                    next_index = n

        if next_index == 0:
            return False

        current = next_index

    return True


a = [2, 0, 1, 0]
print(jump_it(a))

a = [1, 1, 0, 1]
print(jump_it(a))
