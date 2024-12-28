while (n := int(input())) > 0:
    A = list(input() for _ in range(n))
    print(sorted(A, key=lambda x: -sum([x.count(i + i) for i in "aeiouy"]))[0])
