a = list(map(int, input().split()))
b = list(map(int, input().split()))
total = win = 0
for x in a:
    for y in b:
        if x != y: total += 1
        if x > y: win += 1
print(f'{round(win / total, 5):.5f}')
