from collections import deque

N = int(input())
li = list(map(int, input().split()))
li.reverse()

dq = deque()
for i in range(N):
    if li[i] == 1:
        dq.appendleft(i + 1)
    elif li[i] == 2:
        dq.insert(1, i + 1)
    elif li[i] == 3:
        dq.append(i + 1)

for i in dq:
    print(i, end=" ")
