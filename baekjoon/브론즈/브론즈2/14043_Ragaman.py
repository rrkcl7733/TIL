from collections import Counter


s1 = input()
s2 = input()
counter1 = Counter(s1)
counter2 = Counter(c for c in s2 if c != '*')
asterisk_count = s2.count('*')

for char, count in counter2.items():
    if count > counter1.get(char, 0):
        print('N')
        exit()

remaining_chars = sum(counter1[char] - counter2.get(char, 0) for char in counter1)

if remaining_chars == asterisk_count:
    print('A')
else:
    print('N')
