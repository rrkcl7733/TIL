import sys
input = sys.stdin.readline


for t in range(int(input())):
    n, k = map(int, input().split())
    my_traits = input()
    ancestors = [input() for _ in range(n)]

    mutant_count = 0
    for i in range(k):
        if all(ancestor[i] != my_traits[i] for ancestor in ancestors):
            mutant_count += 1

    print(f'Data Set {t + 1}:')
    print(f'{mutant_count}/{k}')
    print('')
