def decode_word(word):
    total = sum(ord(c) - ord('a') for c in word)
    remainder = total % 27
    if remainder == 26:
        return ' '
    else:
        return chr(ord('a') + remainder)

test_cases = [input().split() for _ in range(int(input()))]
for words in test_cases:
    decoded = ''.join(decode_word(word) for word in words)
    print(decoded)
