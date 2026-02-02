n = int(input())
arr = sorted(list(map(int, input().split())))

total = 0
for i, x in enumerate(arr, start=1):
    coeff = 2*i - n - 1
    total += coeff * x

print(2 * total)
