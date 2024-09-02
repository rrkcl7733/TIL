while 1:
    N = int(input())
    if not N:
        exit()

    answer = []
    idx = 0

    for i in range(N):
        a, n = input().split()
        match a[0]:
            case 'I':
                answer.insert(idx, n)
                idx += 1
            case 'L':
                idx = max(idx - 1, 0)
            case 'R':
                idx = min(idx + 1, len(answer))

    print(''.join(answer))
