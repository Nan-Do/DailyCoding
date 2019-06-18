# Cost O(n) (we traverse the string two times)
# Traverse the string putting each word in a stack and then
# extract words from the stack that will return the words in
# a reversed order.
def reverse_words(s):
    words = []

    word = ''
    for x in s:
        if x == ' ':
            words.insert(0, word)
            word = ''
            continue
        word += x
    words.insert(0, word)

    return ' '.join(words)


def reverse_from(s, init, end):
    while init < end:
        temp = s[init]
        s[init] = s[end]
        s[end] = temp

        init += 1
        end -= 1


# Cost O(n) We traverse the string three times, one to detect the words
# another one to reverse each word and the last time to reverse the whole
# string
# The algorithm works as follows traverse the string reversing each word # and then return the reverse of the string (if we reverse each word and # then we reverse the whole string we obtain the desired answer without
# having to care about where to put the spaces on the reversed string
# which can complicate the exercise quite a lot
def reverse_words_mutable(s):
    last_init = 0

    for pos, x in enumerate(s):
        if x == ' ':
            reverse_from(s, last_init, pos - 1)
            last_init = pos + 1
    # Reverse last word
    reverse_from(s, last_init, len(s) - 1)

    reverse_from(s, 0, len(s) - 1)


print(reverse_words("hello world here"))
s = [
    'h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', ' ', 't', 'h', 'e',
    'r', 'e'
]
reverse_words_mutable(s)
print(s)
