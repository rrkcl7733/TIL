s = input()
print(chr(sum(ord(char) for char in s) // len(s)))
