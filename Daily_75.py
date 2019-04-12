# Cost function exponential: worst case (n * n - 1 * .... * 1)
# Recursion keeping the recurring index, biggest value so far and
# the accumulated index, for each value of the array we check if
# we can recur and create a longer sequence
def compute_longest_increasing_subsequence(seq, index, biggest_val, length):
    vals = []

    for x in range(index + 1, len(seq)):
        val = seq[x]
        if val > biggest_val:
            r = compute_longest_increasing_subsequence(seq, x, val, length + 1)
            vals.append(r)

    if len(vals):
        return max(vals)

    return length + 1


# Cost function: n^2
# For each value of the array starting from the right check the values that
# are greater than itself and how many greater values do they have until
# the end of the array.
# Keep the greatest value
def compute_longest_increasing_subsequence(seq):
    s = [1] * len(seq)

    for x in range(len(seq) - 2, -1, -1):
        for y in range(x + 1, len(seq)):
            if seq[y] > seq[x]:
                s[x] = max(s[x], s[y] + 1)

    return max(s)


a = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
# a = [0, 8, 4, 12]
# print(compute_longest_increasing_subsequence(a, 0, 0, 0))
print(compute_longest_increasing_subsequence(a))
