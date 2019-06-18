# Auxiliary function to reverse an array
def reverse(s, i, j):
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1


# Cost O(n)
# Algorithim:
#   Find the first element that is minor than the next one starting from the end of the array
#   (this will be the swtiching position)
#   Find the minimum element on the right side of the swtiching position which is greater than
#   the switching value and swtich those two values
#   Reverse the array starting from the next position of the switching position until the end
#   Ex -> [1, 3, 4, 2]:
#     The first element that is minor than the next one is 3, and the minimum element greater
#     than 3 on the right side is 4 the array at this point would be [1, 4, 3, 2]
#     The remaining step is to reverse the array starting from the next position of the switching position
#     until the end in this case we have to switch the 3 and the 2 giving us the solution [1, 4, 2, 3]
def next_permutation(s):
    i = 0
    is_reversed = True
    for x in range(len(s) - 2, -1, -1):
        if s[x] < s[x + 1]:
            i = x
            is_reversed = False
            break

    if is_reversed:
        reverse(s, 0, len(s) - 1)
        return

    j = i + 1
    x = j
    while x < len(s):
        if s[x] < s[j] and s[x] > s[i]:
            j = x
        x += 1

    s[i], s[j] = s[j], s[i]

    i += 1
    j = len(s) - 1
    reverse(s, i, j)


p = [1, 2, 3, 4]
next_permutation(p)
print(p)
next_permutation(p)
print(p)
next_permutation(p)
print(p)
next_permutation(p)
print(p)
next_permutation(p)
print(p)
next_permutation(p)
print(p)
