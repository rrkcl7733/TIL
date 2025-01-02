from collections import Counter


def can_form_word(word, available_count):
    word_count = Counter(word)
    for letter, count in word_count.items():
        if available_count[letter] < count:
            return 0
    return 1


available_letters = input()
n = int(input())
words = [input() for _ in range(n)]

available_count = Counter(available_letters)

for word in words:
    if can_form_word(word, available_count):
        print(word)
