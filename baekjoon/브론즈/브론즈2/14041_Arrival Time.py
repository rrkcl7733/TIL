h, m = map(int, input().split(':'))
hm = h * 60 + m

for _ in range(120):
    if (420 <= hm < 600) or (900 <= hm < 1140):
        hm += 2
    else:
        hm += 1

m = hm % 60
h = (hm // 60) % 24

print(f'{h:02d}:{m:02d}')
