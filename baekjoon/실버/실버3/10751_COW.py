n = int(input())
word = input()
cow = [[0] * 3 for _ in range(n)]

if word[0] == "C":
    cow[0][0] = 1

for i in range(1, n):
    cow[i] = cow[i - 1][:3]
    if word[i] == "C":
        cow[i][0] += 1
    elif word[i] == "O":
        cow[i][1] += cow[i - 1][0]
    elif word[i] == "W":
        cow[i][2] += cow[i - 1][1]

print(cow[n - 1][2])
