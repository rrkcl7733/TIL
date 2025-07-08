N = int(input())
heights = [int(input()) for _ in range(N)]

avg = sum(heights) // N
moves = 0
for h in heights:
    if h > avg:
        moves += h - avg

print(moves)
