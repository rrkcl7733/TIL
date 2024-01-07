import math

N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

# 티셔츠를 T장씩 최소 몇 묶음 주문해야 하는지 계산
shirt_order = sum(math.ceil(size / T) for size in sizes)

# 펜을 P자루씩 최대 몇 묶음 주문할 수 있는지 계산
pen_bundle = N // P

# 그 때 펜을 한 자루씩 몇 개 주문하는지 계산
pen_single = N % P

print(shirt_order)
print(pen_bundle, pen_single)
