n, r = map(int, input().split())
g = sorted(list(zip(*([int(x) > n for x in input().split()] for _ in range(r)))))
print("possible" if g == [tuple(not x for x in row) for row in g][::-1] else "impossible")
