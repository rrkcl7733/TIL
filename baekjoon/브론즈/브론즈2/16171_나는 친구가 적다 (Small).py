S = input()
K = input()

filtered = ''.join([ch for ch in S if not ch.isdigit()])

if K in filtered:
    print(1)
else:
    print(0)
