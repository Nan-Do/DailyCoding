def check_init_end(s, init, end):
    temp_init = init
    temp_end = end

    while temp_init > 0 and\
          temp_end < len(s) - 1 and\
          s[temp_init] == s[temp_end]:
        temp_init -= 1
        temp_end += 1

    return temp_init, temp_end

def find_longest_palindrome(s):
    init = end = 0

    for x in xrange(len(s)-1):
        if s[x] == s[x+1]:
            temp_init, temp_end = check_init_end(s, x, x+1)
            if (temp_end - temp_init) > (end - init):
                init = temp_init
                end = temp_end

        if x > 0 and s[x-1] == s[x+1]:
            temp_init, temp_end = check_init_end(s, x-1, x+1)
            if (temp_end - temp_init) > (end - init):
                init = temp_init
                end = temp_end

    return init, end


print find_longest_palindrome('race')
print find_longest_palindrome('google')
print find_longest_palindrome('googles')
