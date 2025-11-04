N = int(input())
S = input()

target = ''.join(['I' if i % 2 == 0 else 'O' for i in range(N)])

count = sum(1 for a, b in zip(S, target) if a != b)

print(count)
