n = int(input())
l = list(map(int, input().split()))
m = list(map(int, input().split()))

c = 0
for vl in l:
    for vm in m:
        if vl == vm: continue
        c += 1 if vl > vm else -1

print('first' if c > 0 else 'second' if c < 0 else 'tie')
