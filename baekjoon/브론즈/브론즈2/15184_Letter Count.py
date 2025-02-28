text = input().upper()
counts = dict()

for char in text:
    counts[char] = counts.get(char, 0) + 1

for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    print(f'{letter} | {'*' * counts.get(letter, 0)}')
