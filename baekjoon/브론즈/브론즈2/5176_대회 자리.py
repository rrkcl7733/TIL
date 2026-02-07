import sys
input = sys.stdin.readline


for _ in range(int(input())):
    P, _ = map(int, input().split())
    occupied = set()
    eliminated = 0
    for _ in range(P):
        seat = int(input())
        if seat in occupied:
            eliminated += 1
        else:
            occupied.add(seat)
    print(eliminated)
