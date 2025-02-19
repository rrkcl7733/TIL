message = input()
crib = input()

cnt = 0
for i in range(len(message) - len(crib) + 1):
    for j in range(len(crib)):
        if message[i + j] == crib[j]:
            break
    else:
        cnt += 1
print(cnt)
