def is_generalized_fibonacci(seq):
    if len(seq) < 3:
        return True

    for i in range(2, len(seq)):
        if seq[i] != seq[i - 1] + seq[i - 2]:
            return False

    return True


for _ in range(int(input())):
    k, *seq = list(map(int, input().split()))
    print(['NO', 'YES'][is_generalized_fibonacci(seq)])
