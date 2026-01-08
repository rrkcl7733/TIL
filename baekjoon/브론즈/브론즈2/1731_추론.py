seq = [int(input()) for _ in range(int(input()))]

# 등차수열인지 확인
if seq[1] - seq[0] == seq[2] - seq[1]:
    d = seq[1] - seq[0]
    print(seq[-1] + d)
else:
    r = seq[1] // seq[0]
    print(seq[-1] * r)
