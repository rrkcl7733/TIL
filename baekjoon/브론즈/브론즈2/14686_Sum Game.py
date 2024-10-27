N = int(input())
swifts = list(map(int, input().split()))
semaphores = list(map(int, input().split()))
swift_sum = semaphore_sum = k = 0

for i in range(N):
    swift_sum += swifts[i]
    semaphore_sum += semaphores[i]
    if swift_sum == semaphore_sum:
        k = i + 1

print(k)
