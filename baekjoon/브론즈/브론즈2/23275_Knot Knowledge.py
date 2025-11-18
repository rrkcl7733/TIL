input()
X = set(map(int, input().split()))
Y = set(map(int, input().split()))

missing = X - Y
print(missing.pop())
