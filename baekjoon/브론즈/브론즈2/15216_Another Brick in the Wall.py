h, w, _ = map(int, input().split())
bricks = map(int, input().split())
current_width = 0
current_height = 0

for brick in bricks:
    current_width += brick
    if current_width == w:
        current_height += 1
        current_width = 0
        if current_height == h:
            exit(print('YES'))
    elif current_width > w:
        exit(print('NO'))

print('NO')
