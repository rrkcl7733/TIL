for _ in range(int(input())):
    _, *tokens = input().split()

    max_seq = current_seq = 0

    # 각 항목을 순회하며 연속된 X의 개수를 측정합니다.
    for symbol in tokens:
        if symbol == 'X':
            current_seq += 1
            if current_seq > max_seq:
                max_seq = current_seq
        else:
            current_seq = 0

    print(f"The longest contiguous subsequence of X's is of length {max_seq}")
