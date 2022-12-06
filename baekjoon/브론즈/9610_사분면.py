n = int(input())
a = [0] * 5
for i in [list(map(int, input().split())) for _ in range(n)]:
    if 0 in i:
        a[0] += 1
    elif i[0] > 0 and i[1] > 0:
        a[1] += 1
    elif i[0] < 0 and i[1] > 0:
        a[2] += 1
    elif i[0] < 0 and i[1] < 0:
        a[3] += 1
    else:
        a[4] += 1
for i in range(1, 5):
    print(f'Q{i}: {a[i]}')
print(f'AXIS: {a[0]}')
