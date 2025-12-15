N = int(input())

if N % 2 == 0:
    print("I LOVE CBNU")
else:
    print("*" * N)

    k = (N + 1) // 2
    for i in range(k):
        left_spaces = k - 1 - i
        if i < 1:
            print(" " * left_spaces + "*")
        else:
            inner_spaces = 2 * i - 1
            print(" " * left_spaces + "*" + " " * inner_spaces + "*")
