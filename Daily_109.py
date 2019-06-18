def get_bit(n, i):
    m = (1 << i)

    if (n & m) > 0:
        return 1
    else:
        return 0


def set_bit(n, i):
    m = (1 << i)
    return (n | m)


def clear_bit(n, i):
    m = ~(1 << i)
    return (n & m)


def swap_bits(n, p1, p2):
    b1 = get_bit(n, p1)
    b2 = get_bit(n, p2)

    if b1:
        n = set_bit(n, p2)
    else:
        n = clear_bit(n, p2)

    if b2:
        n = set_bit(n, p1)
    else:
        n = clear_bit(n, p1)

    return n


# Naive solution: Traverse each pair of bits and swap them
def update_bits(n):
    for x in range(0, 8 - 2 + 1, 2):
        n = swap_bits(n, x, x + 1)

    return n


# Solution taken from the web: get the bits for the even and odd positions displace it one bit and then return the or
def _swap_bits(x):
    EVEN = 0b10101010
    ODD = 0b01010101
    return (x & EVEN) >> 1 | (x & ODD) << 1


print(update_bits(170))
print(_swap_bits(170))
