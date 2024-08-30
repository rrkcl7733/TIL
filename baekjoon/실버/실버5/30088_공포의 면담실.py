N = int(input())
spend = [0] * N

for i in range(N):
    _, *t = map(int, input().split())
    spend[i] = sum(t)

spend.sort(reverse=True)
print(sum((i + 1) * v for i, v in enumerate(spend)))
