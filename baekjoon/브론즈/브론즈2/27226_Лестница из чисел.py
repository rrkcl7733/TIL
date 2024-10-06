a = int(input())
b = int(input())
k = int(input())

for i in range(a, b + 1):
    first = i * (i - 1) // 2

    for j in range(1, min(i, k) + 1):
        print(first + j, end=" ")

    print()
