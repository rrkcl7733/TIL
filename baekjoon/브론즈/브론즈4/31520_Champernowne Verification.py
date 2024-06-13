num = input()

for i in range(len(num)):
    if int(num[i]) != i + 1:
        print(-1)
        exit()
print(num[-1])
