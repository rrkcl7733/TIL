S1, S2, S3 = map(int, input().split())

freq = {}

for i in range(1, S1+1):
    for j in range(1, S2+1):
        for k in range(1, S3+1):
            s = i + j + k
            freq[s] = freq.get(s, 0) + 1

max_freq = max(freq.values())
answer = min(key for key, val in freq.items() if val == max_freq)

print(answer)
