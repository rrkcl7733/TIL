n = int(input())
numbers = list(map(int, input().split()))

for i in range(n):
    for j in range(n):
        if str(numbers[i]).startswith(str(numbers[j])) or str(numbers[i]).endswith(str(numbers[j])):
            print(i+1, j+1)
            exit(0)

print(-1)
