import sys


input = sys.stdin.readline
T = int(input())
l = []
r = []
for _ in range(T):
    l_t, r_t = map(int, input().split())
    l.append(l_t)
    r.append(r_t)

fun = 0
prev_l = 0
prev_r = 0
for t in range(T):
    l_t = l[t]
    r_t = r[t]
    if l_t != 0 and l_t == prev_l:
        fun += 1
    if r_t != 0 and r_t == prev_r:
        fun += 1
    if l_t != 0 and r_t != 0 and l_t == r_t:
        fun += 1
    prev_l = l_t
    prev_r = r_t

print(fun)
