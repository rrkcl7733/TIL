text = ''.join(input().split()).lower()

for i in range(len(text)-1):
    t1 = text[i:i+2]
    t2 = text[i:i+3]

    if t1 == t1[::-1] or t2 == t2[::-1]:
        print("Palindrome")
        exit()
print("Anti-palindrome")
