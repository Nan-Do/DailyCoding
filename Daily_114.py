def reverse_word(s, i, j):
    while i < j:
        temp = s[i]
        s[i] = s[j]
        s[j] = temp

        i += 1
        j -= 1


# Not really sure what the question was asking by watching at the
# examples
# I made an algorithim that reverses the words maintaining the
# relative order of the delimieters as in if you have these
# delimiters "aba/aak:aksd" you switch first the words
# separated by : and then /
# It works by using a stack and when a mismatch on the delimiters is
# found it extracts elements of the stack until the matching one is
# found recursing on the substring.
# The basic functioning to reverse the words in place is the same as
# usual when a separator is found the word is reversed and then before
# finishing the function the whole string is reversed
def reverse_string(s, i, j):
    stack = []
    delimeters = ['/', ':']

    last = 0
    for pos in range(i, j):
        x = s[pos]
        if x in delimeters:
            reverse_word(s, last, pos - 1)
            last = pos + 1

            if len(stack) != 0 and stack[-1][0] != x:
                while len(stack):
                    delim, old_pos = stack.pop()
                    if delim == x:
                        reverse_string(s, old_pos, pos)

            stack.append((x, pos))

    if s[j - 1] not in delimeters:
        reverse_word(s, last, j - 1)

    reverse_word(s, i, j - 1)


# string = 'hello/world:here'
string = 'hello/world:here'
s = [x for x in string]
reverse_string(s, 0, len(s))
print(''.join(s))
