for x in range(int(input())):
    m = [0] * 11
    for i in range(int(input())):
        a, b = map(int, input().split())
        m[b] = max(m[b], a)
    for i in range(1, 11):
        if m[i] == 0:
            print('MOREPROBLEMS')
            break
    else:
        print(sum(m))
