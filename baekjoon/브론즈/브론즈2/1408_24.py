def to_seconds(h, m, s):
    return h*3600 + m*60 + s

h1, m1, s1 = map(int, input().split(":"))
h2, m2, s2 = map(int, input().split(":"))

cur_sec = to_seconds(h1, m1, s1)
start_sec = to_seconds(h2, m2, s2)

diff = (start_sec - cur_sec) % 86400

hh = diff // 3600
mm = (diff % 3600) // 60
ss = diff % 60

print(f"{hh:02d}:{mm:02d}:{ss:02d}")
