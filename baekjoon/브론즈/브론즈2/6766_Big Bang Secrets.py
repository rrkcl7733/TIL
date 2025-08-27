K = int(input())
word = input()
for i, ch in enumerate(word, start=1):
    shift = 3 * i + K
    original_pos = (ord(ch) - ord('A') - shift) % 26
    print(chr(original_pos + ord('A')), end='')
