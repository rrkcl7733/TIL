set_num = 1
while 1:
    n = int(input().strip())
    if n < 1:
        exit()
    heights = list(map(int, input().split()))
    target = sum(heights) // n
    moves = sum(h - target for h in heights if h > target)

    print(f'Set #{set_num}')
    print(f'The minimum number of moves is {moves}.')
    print()

    set_num += 1
