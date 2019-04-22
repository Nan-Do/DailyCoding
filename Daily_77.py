# Cost of the function:
# n^3 the for loops have a cost of n^2 and the while loop will at most be exectued n times as
# at most we can merge n-1 ranges
# The algorithim checks if two given ranges overlap, if they do, it merges them creating a new list
# It tries again until no other two intervals can be merged.
def _merge_intervals(seq):
    all_merged = False
    while not all_merged:
        all_merged = True
        have_to_merge = False
        c1 = c2 = None

        for x in range(len(seq)):
            for y in range(x + 1, len(seq)):
                c1 = seq[x]
                c2 = seq[y]

                if c2[0] <= c1[0] <= c2[1] or\
                   c1[0] <= c2[0] <= c1[0]:
                    have_to_merge = True
                    break

            if have_to_merge:
                break

        if have_to_merge:
            all_merged = False
            new_range = (min(c1[0], c2[0]), max(c1[1], c2[1]))
            seq = seq[:x] + seq[x + 1:y] + [new_range] + seq[y + 1:]

    return seq


# Improved version on linear time using a stack if the sequence if ordered by the starting time.
# (It uses the fact that if interval[x] doesn't overlap with interval[x-1]).
# If the current interval overlaps with the top of the stack, then pop it and push the proper
# updated range, if not just push it.
def merge_intervals(seq):
    seq = sorted(seq)
    stack = [seq[0]]

    for x in range(1, len(seq)):
        c1 = stack[-1]
        c2 = seq[x]

        if c1[0] <= c2[0] <= c1[1]:
            stack.pop()
            stack.append((c1[0], max(c1[1], c2[1])))
        else:
            stack.append(c2)

    return stack


s = [(1, 3), (5, 8), (4, 10), (20, 25)]
print(merge_intervals(s))
