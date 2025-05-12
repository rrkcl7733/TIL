M, _, K = map(int, input().split())

for _ in range(M):
    row = input()
    enlarged_row = [ch * K for ch in row]
    for _ in range(K):
        print(*enlarged_row, sep='')
