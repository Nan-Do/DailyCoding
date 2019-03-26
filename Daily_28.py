def justify_line(words, k):
    lines = []
    current_line_len = 0
    current_line = []

    for p, word in enumerate(words):
        if len(word) + current_line_len > k or\
           p == len(words) - 1:
            if p == len(words) - 1:
                current_line.append(word)
                current_line_len += len(word)
            else:
                current_line_len -= 1

            total_spaces = len(current_line) - 1
            spaces_per_word = 1
            unassigned_spaces = k - current_line_len
            if unassigned_spaces > total_spaces:
                spaces_per_word = unassigned_spaces / total_spaces
                unassigned_spaces = unassigned_spaces - (total_spaces * spaces_per_word)
            print current_line_len, spaces_per_word, total_spaces, unassigned_spaces
            line = ''
            for pos, w in enumerate(current_line):
                line += w
                if pos != len(current_line) - 1:
                    spaces = ' ' * spaces_per_word
                    if unassigned_spaces > 0:
                        spaces += ' '
                        unassigned_spaces -= 1
                    line += spaces
            lines.append(line)

            current_line = []
            current_line_len = 0
            

        current_line.append(word)
        current_line_len += len(word) + 1

    return lines


for l in justify_line(["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], 16):
    print l, len(l)
                   
