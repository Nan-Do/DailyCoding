def split_sentence(sentence, k):
    word = ''
    res = []
    current_words = []

    for c in sentence:
        if c == ' ':
            if len(word) + sum(map(len,
                                   current_words)) + len(current_words) <= k:
                current_words.append(word)
            else:
                res.append(' '.join(current_words))
                current_words = [word]
            word = ''
            continue
        word += c

    if len(word) + sum(map(len, current_words)) + len(current_words) <= k:
        current_words.append(word)
        res.append(' '.join(current_words))
    else:
        res.append(' '.join(current_words))
        res.append(word)

    return res


sentence = 'the quick brown fox jumps over the lazy dog'
print(split_sentence(sentence, 10))
