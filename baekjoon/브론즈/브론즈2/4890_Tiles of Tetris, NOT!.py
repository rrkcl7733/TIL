import sys
import math

input = sys.stdin.readline
while 1:
    w, h = map(int, input().split())
    if w == 0:
        exit()
    g = math.gcd(w, h)
    # 최소 x = h/g, y = w/g 이므로 총 타일 수 = x * y = (h/g) * (w/g)
    tiles = (w // g) * (h // g)
    print(tiles)
