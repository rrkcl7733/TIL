input()
A = list(map(int, input().split()))
B = list(map(int, input().split()))

count = 0
for a in A:
    for b in B:
        if a <= b:
            count += 1

print(count)
