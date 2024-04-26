N, M = map(int, input().split())
schoolClass = [list(input()) for _ in range(N)]
zipClass = list(map(list, zip(*schoolClass)))

for i in range(M):
    if zipClass[i].count("X") == N:
        print(i + 1)
        break
else:
    print("ESCAPE FAILED")
