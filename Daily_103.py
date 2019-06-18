def all_chars(s, c):
    for char in c:
        if char not in s:
            return False

    return True


# Cost O(n^3) brute force compute, all the possible substrings, check if the
# substring contains all the required chars and then return the minimum
def P103_2(s, c):
    res = []
    for s1 in range(len(s)):
        for s2 in range(s1 + 1, len(s)):
            if all_chars(s[s1:s2 + 1], c):
                res.append((s2 - s1 + 1, (s1, s2)))
    return min(res)


# Cost O(n)
# Had to check the solution at
# https://www.geeksforgeeks.org/find-the-smallest-window-in-a-string-containing-all-characters-of-another-string/
# How does it work:
# Create 2 multi hash_sets (a hash table with keys having characters and as values an integer representing
# how many times do we need them).
# Initialize one of them with the characters required for the pattern
# Check each character of the string, update the string multi hash_set, if the character is in the
# multi hash_set of the pattern and we didn't reach the limit yet update a count.
# The count represents the number of characters of the pattern matched, once this count reaches
# the lenght of the pattern we know we have a valid answer
# From this point on we have to check if the letter we are checking is also at the start, in that case
# we know we can move the start one position and still have a valid answer.
# Corner cases:
# The pattern is longer than the string
# The pattern can't be matched (that is why start_index is -1)
def P103(s, c):
    if len(s) < len(c):
        return ''

    s_pat = [0] * 256
    c_pat = [0] * 256

    for char in c:
        c_pat[ord(char)] += 1

    start_index = -1
    start = count = 0
    min_len = float('inf')

    for pos, char in enumerate(s):
        s_pat[ord(char)] += 1

        if c_pat[ord(char)] != 0 and\
           s_pat[ord(char)] <= c_pat[ord(char)]:
            count += 1

        if count == len(c):
            while s_pat[ord(s[start])] > c_pat[ord(s[start])] or\
                  c_pat[ord(s[start])] == 0:
                if s_pat[ord(s[start])] > c_pat[ord(s[start])]:
                    s_pat[ord(s[start])] -= 1
                start += 1

            if min_len > (pos - start + 1):
                min_len = pos - start + 1
                start_index = start

    if start_index == -1:
        return ''

    return s[start_index:start_index + min_len]


print(P103("figehaeci", set('aei')))
