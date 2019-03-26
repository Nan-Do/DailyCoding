def maximum_profit(arr):
    maxs = [0] * len(arr)

    maxs[-1] = arr[-1]
    for x in xrange(len(arr) - 2, -1, -1):
        maxs[x] = max(arr[x], maxs[x+1])

    max_difference = 0
    for x in xrange(len(arr)):
        max_difference = max(max_difference, maxs[x] - arr[x])

    return max_difference


print maximum_profit([9,11,8,5,7,10])
