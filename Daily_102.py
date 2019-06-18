# Cost O(n), Trivial solution: O(n^2)
# To solve the problem use a slide window with two counters with a counter sum
# if at any point the sum is higher thant the desired number move the left side of the slide window
# if it is higher move the right side.
# Dificult things about this problem
# the condition to break out of the loop which happens when the right side of the
# window arrives to the and or we need a new value from the right or the left side also
# arrives to the end.
# Check out the indexes!!!
# Also the conditions to advance the loop are a little bit tricky.
def get_subsequence_sum(seq, k):
    i = j = 0
    sum_count = 0

    while True:
        if j == len(seq) and\
           (i == j or sum_count < k):
            break

        if sum_count == k:
            return seq[i:j]

        if sum_count < k and j < len(seq):
            sum_count += seq[j]
            j += 1
        if sum_count > k:
            sum_count -= seq[i]
            i += 1

    return []


print(get_subsequence_sum([1, 2, 3, 4, 5], 9))
