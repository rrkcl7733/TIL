N = int(input())
time = 0
k = 1

while N > 0:
    if N < k:
        k = 1
    N -= k
    k += 1
    time += 1

print(time)
