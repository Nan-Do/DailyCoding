def compute_water(s):
    max_right = [0] * len(s)
    max_right[-1] = s[-1]

    for x in xrange(len(s)-2, -1, -1):
        max_right[x] = max(s[x], max_right[x+1])

    max_left = s[0]
    total = 0

    for x in xrange(1,len(s)):
        a = min(max_left, max_right[x]) - s[x]
        if a > 0:
            total += a
        max_left = max(max_left, s[x])

    return total


print compute_water([2,1,2])
print compute_water([3,0,1,3,0,5])
