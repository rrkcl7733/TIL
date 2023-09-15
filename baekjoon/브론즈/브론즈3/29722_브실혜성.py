y, m, d = input().split('-')
y, m, d = int(y), int(m), int(d)
d += int(input())
m += (d - 1) // 30
d %= 30
d = d if d else 30
y += (m - 1) // 12
m %= 12
m = m if m else 12
d = d if d // 10 else '0' + str(d)
m = m if m // 10 else '0' + str(m)
print(f'{y}-{m}-{d}')
