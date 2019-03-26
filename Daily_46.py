def get_pal_len(seq, s, e):
    if s < 0: return s, s
    
    while s >= 0 and e < len(seq) and seq[s] == seq[e]:
        s -= 1
        e += 1

    return s+1, e-1

def longest_palindrome(seq):
    w = ''

    for x in xrange(0, len(seq) - 1):
        s, e = get_pal_len(seq, x, x+1)
        if e + 1 - s > len(w):
            w = seq[s:e+1]
        s, e  = get_pal_len(seq, x-1, x+1)
        if e + 1 - s > len(w):
            w = seq[s:e+1]

    return w

print longest_palindrome("bananas")
print longest_palindrome("aabcdcb")
print longest_palindrome("abc")
print longest_palindrome("aaaaa")
