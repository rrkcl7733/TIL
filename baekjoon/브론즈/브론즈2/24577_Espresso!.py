n, s = map(int, input().split())
total = 0
now = s

for _ in range(n):
    input_value = input()

    water = int(input_value) if len(input_value) == 1 else int(input_value[0]) + 1
    if now < water:
        now = s
        total += 1
    now -= water

print(total)
