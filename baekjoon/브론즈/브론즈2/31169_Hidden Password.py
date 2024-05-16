z = int(input())

for _ in range(z):
    for c in input():
        print(chr(((ord(c) - ord('a') + 13) % 26) + ord('a')), end='')
    print()
