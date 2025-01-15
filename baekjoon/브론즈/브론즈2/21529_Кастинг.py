mode = int(input())
n, a, b, c = map(int, input().split())
print([0, max(0, a + b + c - 2 * n), min(a, b, c)][mode])
