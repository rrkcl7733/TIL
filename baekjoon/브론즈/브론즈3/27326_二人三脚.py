input()
a = list(map(int, input().split()))
for i in range(1, 101):
    if a.count(i) == 1:
        print(i)
        exit()
