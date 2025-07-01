def inverse_mtf(sequence):
    lst = [chr(ord('a') + i) for i in range(26)]
    result = []
    for idx in sequence:
        ch = lst[idx]
        result.append(ch)
        # 해당 문자를 앞으로 이동
        lst.pop(idx)
        lst.insert(0, ch)
    print("".join(result))


for _ in range(int(input())):
    n = int(input())
    seq = list(map(int, input().split()))
    inverse_mtf(seq)
