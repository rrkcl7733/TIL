input()
A = list(map(int, input().split()))  # 보물상자에 적힌 숫자
B = set(map(int, input().split()))   # 사용할 수 있는 열쇠 숫자 집합

print(sum(1 for a in A if a in B))
