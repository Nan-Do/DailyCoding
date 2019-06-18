# Cost O(n): at worst we check each character twice
# Starting from each letter in a check if it matches with the letters in b
# Keep two counters and use the modulo when checking the letters in a to avoid
# accessing the wrong position.
def is_shifted(a, b):
    if len(a) != len(b):
        return False

    for pos, c in enumerate(a):
        shifted = True
        for x in range(0, len(b)):
            if a[(pos + x) % len(a)] != b[x]:
                shifted = False
                break
        if shifted:
            return True

    return False


print(is_shifted('abcde', 'cdeab'))
print(is_shifted('abcde', 'cdeac'))
