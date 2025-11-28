_, K = map(int, input().split())
T = input()

print(T[:K-1] + T[K-1:].swapcase())
