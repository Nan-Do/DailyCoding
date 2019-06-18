# Naive solution. Cost O(n log n)
# Sort the sequence and check the longest number of consecutive elements
def P_99_1(s):
    s.sort()

    current = longest = 0
    for x in range(0, len(s) - 1):
        if s[x] == s[x + 1] - 1:
            current += 1
        else:
            current = 0

        longest = max(current, longest)

    return longest + 1


# Cost O(k). Note always k >= n for positive distinct integers
# Solution: obtain the maximum number of the sequence,
# convert the sequence into a set,
# iterate over the integers from 1 to maximum number checking
# the longest number of consecutive elements
def P_99_2(s):
    maximum_val = max(s)
    s = set(s)

    longest = current = 0
    for x in range(1, maximum_val + 1):
        # If the current element and the next one are in the
        # set we are in the middle of the sequence, otherwhise
        # we have to reset the seuquence count
        if x in s and x + 1 in s:
            current += 1
        else:
            current = 0

        longest = max(longest, current)

    # The sequence doesn't take into account the first element so
    # we have to count it on the final solution
    return longest + 1


# Cost O(n)
# Turn the sequence into a set, check each element of the array,
# if (element - 1) is not in the set it means that it is
# the begginig of a sequence, iterate adding one to the inital
# element until the first value that is not in the set,
# that means that we reached the end of the sequence, the lenght
# of the sequence is the last element - the first one. Check if
# the computed length is greater than the previous one.
def P_99(s):
    s = set(s)
    longest = 1

    for x in s:
        # Is the begginig of a sequence
        if x - 1 not in s:
            j = x + 1
            while j in s:
                j += 1

            longest = max(longest, j - x)

    return longest


print(P_99([100, 4, 200, 1, 3, 2]))
