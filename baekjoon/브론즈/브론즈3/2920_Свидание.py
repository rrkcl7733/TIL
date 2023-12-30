k = int(input())
n = int(input())
a = list(map(int, input().split()))
print('YES' if any(sum(a) - i >= k for i in a) else 'NO')
