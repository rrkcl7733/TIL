N = int(input())
altitudes = list(map(int, input().split()))
max_gain = 0
current_gain = 0

for i in range(1, N):
    if altitudes[i] > altitudes[i - 1]:
        current_gain += altitudes[i] - altitudes[i - 1]
        max_gain = max(max_gain, current_gain)
    else:
        current_gain = 0
print(max_gain)
