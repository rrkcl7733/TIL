N, _ = map(int, input().split())

multiples = set()
for k in map(int, input().split()):
    for x in range(k, N+1, k):
        multiples.add(x)

print(sum(multiples))
