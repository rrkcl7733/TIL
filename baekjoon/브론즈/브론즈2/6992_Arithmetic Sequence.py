def is_arithmetic(seq):
    diff = seq[1] - seq[0]
    for i in range(2, len(seq)):
        if seq[i] - seq[i - 1] != diff:
            return False
    return True


for _ in range(int(input())):
    seq = list(map(int, input().split()))[1:]

    if is_arithmetic(seq):
        diff = seq[1] - seq[0]
        next_five = [seq[-1] + diff * i for i in range(1, 6)]
        print(f"The next 5 numbers after {seq} are: {next_five}")
    else:
        print(f"The sequence {seq} is not an arithmetic sequence.")
