first_die = list(map(int, input().split()))
second_die = list(map(int, input().split()))

a = b = 0
for i in first_die:
    for j in second_die:
        if i > j:
            a += 1
        elif i < j:
            b += 1

print(f'{a / (a + b):.5f}')
