N, M = map(int, input().split())
cnt = 1

for i in range(N):
    cnt *= 2 * (i + 1)
    
print("Harshat Mata" if cnt >= M else "Nope")
