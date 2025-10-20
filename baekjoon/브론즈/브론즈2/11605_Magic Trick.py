def is_messed_up(k):
    for op, x in ops:
        x = int(x)
        if op == "ADD":
            k += x
        elif op == "SUBTRACT":
            k -= x
        elif op == "MULTIPLY":
            k *= x
        elif op == "DIVIDE":
            if k % x != 0:
                return True
            k //= x
        if k < 0:
            return True
    return False


ops = [input().split() for _ in range(int(input()))]
count = sum(is_messed_up(k) for k in range(1, 101))
print(count)
