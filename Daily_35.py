def swap(s, x, y):
    temp = s[x]
    s[x] = s[y]
    s[y] = temp

def f(s):
    last = 0
    for letter in ['R', 'G', 'B']:
        while last < len(s) and s[last] == letter: last += 1
        for x in xrange(last+1, len(s)):
            if s[x] == letter:
                swap(s, last, x)
                last += 1

s = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
f(s)
print s
