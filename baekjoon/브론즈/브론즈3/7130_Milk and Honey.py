M, H = map(int, input().split())
N = int(input())
fields = [list(map(int, input().split())) for _ in range(N)]
happiness = 0
for C, B in fields:
    happiness += max(C * M, B * H)
print(happiness)
