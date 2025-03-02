def determine_winner():

    kangaroo_score = sum(secret_phrase.count(char) for char in 'kangaroo')
    kiwi_score = sum(secret_phrase.count(char) for char in 'kiwibird')

    if kangaroo_score > kiwi_score:
        return 'Kangaroos'
    elif kiwi_score > kangaroo_score:
        return 'Kiwis'
    else:
        return 'Feud continues'


secret_phrase = input().lower()
result = determine_winner()

print(result)
