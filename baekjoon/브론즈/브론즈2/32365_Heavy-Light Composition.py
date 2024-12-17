from collections import Counter

T, N = map(int, input().split())

for _ in range(T):
    s = input()
    cnt = Counter(s)
    for i in range(N - 1):
        if (cnt[s[i]] > 1) == (cnt[s[i + 1]] > 1):
            print('F')
            break
    else:
        print('T')
