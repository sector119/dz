import random
import string


chars = string.ascii_letters

words_chars_number = 1000 - 100 - 10 - 10
comma_number = 10
dot_number = 9
words_number = 101
word_size = 8

words = []

while words_number > 0:
    words.append(''.join(random.choices(chars, k=word_size)))
    words_number -= 1

words[-1] += ''.join(random.choices(chars, k=words_chars_number - 101 * word_size)) + '.'

while comma_number > 0:
    i = random.randint(0, 100)
    words[i] += ','
    comma_number -= 1

while dot_number > 0:
    i = random.randint(0, 100)
    words[i] += '.'
    dot_number -= 1

text = ' '.join(words)

lowercase_words = []

for word in text.split(' '):
    if not word.islower():
        word = word.lower()

    lowercase_words.append(word)

text = ' '.join(lowercase_words)

print(text)
print(len(text))
