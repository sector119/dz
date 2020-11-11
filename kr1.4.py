s = 'тест1 аб тест2 апн в тест.'

words = []

for word in s[:-1].split():
    if len(word) > 1:
        words.append(word[1:] + word[0])
    else:
        words.append(word)

print(' '.join(words) + '.')

