from heapq import *


n,k = list(map(int, input().split()))
arr = list(map(int, input().split()))
heap,tasks = arr[:k], arr[:k-1:-1]
heapify(heap)
best = 0
time = 0
while heap:
    newtime = heappop(heap)
    best = max(newtime-time,best)
    time = newtime
    if tasks: heappush(heap,time+tasks.pop())
print(best)
