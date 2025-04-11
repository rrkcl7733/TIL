while 1:
    input_line = input()
    if input_line[0] == '0':
        exit()

    m, n = map(int, input_line.split())
    customer_key = list(map(int, input().split()))
    trash_keys = [list(map(int, input().split())) for _ in range(n)]

    count = 0

    for trash_key in trash_keys:
        for i in range(m):
            if trash_key[i] > customer_key[i]:
                break
        else:
            count += 1

    print(count)
