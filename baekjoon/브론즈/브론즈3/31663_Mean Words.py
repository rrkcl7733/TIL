n = int(input())
words = [input() for _ in range(n)]
mean_word = ""
max_length = max(len(word) for word in words)

for i in range(max_length):
    sum_ascii = c = 0
    for word in words:
        if i < len(word):
            sum_ascii += ord(word[i])
            c += 1

    mean_word += chr(sum_ascii // c)
print(mean_word)
