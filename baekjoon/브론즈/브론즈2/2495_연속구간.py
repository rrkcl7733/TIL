for _ in range(3):
    num = input()
    max_len = 1
    current_len = 1

    for i in range(1, len(num)):
        if num[i] == num[i - 1]:
            current_len += 1
            max_len = max(max_len, current_len)
        else:
            current_len = 1

    print(max_len)
