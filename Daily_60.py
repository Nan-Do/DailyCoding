def two_equal_subsets(s):
    elems = sorted(s)

    left_sums = []
    temp_sum = 0
    for x in elems:
        temp_sum += x
        left_sums.append(temp_sum)

    right_sums = []
    temp_sum = 0
    for x in range(len(elems) - 1, -1, -1):
        temp_sum += elems[x]
        right_sums.append(temp_sum)

    for x in range(1, len(elems) - 1):
        if left_sums[x] == right_sums[len(elems) - x - 2]:
            return True

    return False


print(two_equal_subsets([15, 5, 20, 10, 35, 15, 10]))
print(two_equal_subsets([15, 5, 20, 10, 35, 10]))
print(two_equal_subsets([1, 1, 1]))
print(two_equal_subsets([1, 2, 1]))
print(two_equal_subsets([1, 1, 1, 1]))
