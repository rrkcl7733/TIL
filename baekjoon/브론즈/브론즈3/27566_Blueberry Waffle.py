r, f = map(int, input().split())
print('down' if 90 <= 180 * (f / r) % 360 <= 270 else 'up')
