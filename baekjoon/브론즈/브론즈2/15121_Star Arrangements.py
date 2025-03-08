print(f'{(N := int(input()))}:')
for i in range(2, N):
    for j in range(i - 1, i + 1):
        k = total = 0
        while total < N:
            if k % 2:
                total += j
            else:
                total += i
            k += 1
        if total == N:
            print(f'{i},{j}')
