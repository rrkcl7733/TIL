for _ in range(int(input())):
    sascha_word = input()
    dictionary = [input() for _ in range(int(input()))]
    min_substitutions = float('inf')
    likely_word = ''

    for word in dictionary:
        substitutions = sum(a != b for a, b in zip(sascha_word, word))
        if substitutions < min_substitutions:
            min_substitutions = substitutions
            likely_word = word

    print(likely_word)
