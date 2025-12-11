input()
name = input()

score = sum(ord(ch) - ord('A') + 1 for ch in name)

print(score)
