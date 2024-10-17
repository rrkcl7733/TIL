L = int(input())
N = int(input())

already = [0 for _ in range(L + 1)]
expect = [0, 0]
real = [0 for _ in range(N)]

for i in range(N):
    P, K = map(int, input().split())
    if expect[1] < K - P:
        expect = [i + 1, K - P]

    for key in range(P, K + 1):
        if not already[key]:
            already[key] = 1
            real[i] += 1

print(expect[0])
print(real.index(max(real)) + 1)
