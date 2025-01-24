for i in range(int(input())):
    input()
    l = list(map(int, input().split()))
    for j in map(int, input().split()):
        l[j - 1] -= 1
    print(f'Data Set {i + 1}:\n{max(l)}\n')
