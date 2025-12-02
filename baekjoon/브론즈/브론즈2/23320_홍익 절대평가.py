N = int(input())
A = list(map(int, input().split()))
X, Y = map(int, input().split())

relative_count = N * X // 100
absolute_count = sum(1 for score in A if score >= Y)

print(relative_count, absolute_count)
