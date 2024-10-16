vowel = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0, 'y': 0}
text = input().lower()

for i in text:
    if i in vowel:
        vowel[i] += 1

y_yes = sum(vowel.values())
y_no = y_yes - vowel.get('y')
print(y_no, y_yes)
