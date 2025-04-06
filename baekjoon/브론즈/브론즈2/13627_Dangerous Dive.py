n, _ = map(int, input().split())
returned_set = set(map(int, input().split()))

all_volunteers = set(range(1, n + 1))

missing = all_volunteers - returned_set

if missing:
    print(*sorted(missing))
else:
    print('*')
