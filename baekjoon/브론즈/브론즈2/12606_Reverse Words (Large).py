T = int(input())  # the number of cases

for x in range(1, T + 1):
    words = input().split()
    reversed_words = ' '.join(reversed(words))
    print(f"Case #{x}: {reversed_words}")
