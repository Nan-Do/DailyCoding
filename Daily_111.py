from collections import defaultdict


# Cost O(s*w)
# Solution
# Create a multiset (as a dictionary with letters as keys and
# integers to represent how many times they appear) for the word
# and for each position of the string try to rebuild the multiset
# Failing conditions to build the multiset are the letter is not
# in the pattern or if there are more letters than in the pattern
def find_anagrams(s, w):
    if len(w) > len(s):
        return []

    res = []

    hash_pat = defaultdict(int)
    for c in w:
        hash_pat[c] += 1

    current_pos = 0
    while current_pos < len(s) - len(w) + 1:
        is_complete = True
        hash_temp = defaultdict(int)
        for x in range(current_pos, current_pos + len(w)):
            if s[x] not in hash_pat:
                is_complete = False
                break
            else:
                if hash_pat[s[x]] == hash_temp[s[x]]:
                    is_complete = False
                    break
                hash_temp[s[x]] += 1
        if is_complete:
            res.append(current_pos)

        current_pos += 1

    return res


print(find_anagrams('abxaba', 'ab'))
