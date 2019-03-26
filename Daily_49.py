def compute_max_sum(seq):
    max_sum = current_sum = 0
    pos = 0

    while pos != len(seq):
        current_sum += seq[pos]
        if current_sum <= 0:
            current_sum = 0
        max_sum = max(max_sum, current_sum)
        pos += 1

    return max_sum


print compute_max_sum([34, -50, 42, 14, -5, 86])
print compute_max_sum([-5, -1, -8, -9])
