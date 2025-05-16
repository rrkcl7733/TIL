import sys
input = sys.stdin.readline


def costToSwap(word1, word2):
    total = 0
    for c1, c2 in zip(word1, word2):
        diff = abs(ord(c1) - ord(c2))
        if c1 < c2:
            total -= diff
        elif c1 > c2:
            total += diff

    return total


for _ in range(int(input())):
    word1, word2 = input().split()

    cost = costToSwap(word1, word2)
    if cost > 0:
        result = f'earned {cost} coins.'
    elif cost < 0:
        result = f'cost {-cost} coins.'
    else:
        result = 'was FREE.'

    print(f'Swapping letters to make {word1} look like {word2} {result}')
