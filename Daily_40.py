def get_bit(num, i):
    return num & (1 << i)

def get_unique(s, BIT_SIZE=32):
    res = 0

    for x in xrange(BIT_SIZE):
        total_bits = 0

        for v in s:
            if get_bit(v, x):
                total_bits += 1

        if (total_bits % 3) == 0:
            continue

        res += (1 << x)

    return res


print get_unique([2,11,3,2,3,2,3])
