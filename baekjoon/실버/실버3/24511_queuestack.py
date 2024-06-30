import sys
from collections import deque


input = sys.stdin.readline
input()
A = list(map(int, input().split()))
B = list(map(int, input().split()))

q = deque()

for idx, value in enumerate(B):
    if A[idx] == 0:
        q.append(value)

M = int(input())
C = list(map(int, input().split()))
answer = []

for i in C:
    q.appendleft(i)

for _ in range(M):
    answer.append(q.pop())
print(*answer)
