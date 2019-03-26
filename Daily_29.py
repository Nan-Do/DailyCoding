def encode_str(s):
    encoded_str = ''
    c = s[0]
    c_l = 1

    for x in xrange(1, len(s)):
        if c != s[x]:
            encoded_str += (str(c_l) + c)
            c = s[x]
            c_l = 1
        else:
            c_l += 1

    encoded_str += (str(c_l) + c)
    return encoded_str
    

print encode_str('AAAABBBCCDAA')
