def find_nth_digit(x, n):
    sequence = '1'
    current_number = 1

    while len(sequence) < n:
        current_number *= x
        sequence += str(current_number)

    return sequence[n - 1]


x, n = map(int, input().split())
print(find_nth_digit(x, n))
