n, a, b = map(int, input().split())
is_min_exist = is_max_exist = 0

for _ in range(n - 1):
    w = int(input())
    if w == a:
        is_min_exist = 1
    elif w == b:
        is_max_exist = 1

if is_min_exist and is_max_exist:
    for i in range(1, n + 1):
        print(i)
elif is_min_exist:
    print(b)
elif is_max_exist:
    print(a)
else:
    print(-1)
