def is_next_char_wildcard(pos, regexp):
    if pos == len(regexp) - 1:
        return False
    
    return regexp[pos + 1] == '*'

def next_char_withwildcard(pos, regexp):
    if pos >= len(regexp) - 2:
        return None

    return regexp[pos+2]

def compare_char(a, b):
    if a == '.':
        return True

    return a == b

def match(regex, string):
    index_s = 0
    pos = 0
    while pos < len(regex):
        if index_s >= len(string):
            return False

        val = regex[pos]
        wild_card = is_next_char_wildcard(pos, regex)

        if wild_card:
            next_char = next_char_withwildcard(pos, regex)

            if next_char is None:
                while index_s < len(string):
                    if not compare_char(val, string[index_s]):
                        return False
                    index_s += 1
                return True
            else:
                while index_s < len(string) and string[index_s] != next_char:
                    if not compare_char(val, string[index_s]):
                        return False
                    index_s += 1
                pos += 2
        else:
            if not compare_char(val, string[index_s]):
                return False
            index_s += 1
            pos += 1

    if index_s != len(string):
        return False

    return True

print match('.*at', 'ray')
print match('.*', 'ray')
print match('ra.', 'ray')
print match('.*a', 'chat')
print match('.*at', 'chat')
