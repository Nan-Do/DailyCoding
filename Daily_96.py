# Cost O(Factorial)
# Solution:
# The solution will be composed by taking each element of the sequence and adding it to all the
# elements generated by the permutations of the sequence minus that element. It recurs until
# the sequence only have one element (could be zero to take into account the empty sequence)
def permutations(s):
    # Base case
    if len(s) == 1:
        return [s]

    res = []

    # Compute the permutations
    for x in range(len(s)):
        # Obtain the sequence minus the current element x
        r = permutations(s[:x] + s[x + 1:])
        # Build the new solution adding the element x to the solutions computed by the previous
        # recursions
        res += list((map(lambda z: [s[x]] + z, r)))

    return res


print(permutations([1, 2, 3]))
