def powerset(s):
    res = [[]]

    for x in s:
        res += map(lambda t_r: t_r + [x], res)

    return res

print powerset([1,2,3])
