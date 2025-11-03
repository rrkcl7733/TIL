input()
A = set(map(int, input().split()))
B = set(map(int, input().split()))

# 교집합 연산자
common = sorted(A & B)

print(*common, sep='\n')
