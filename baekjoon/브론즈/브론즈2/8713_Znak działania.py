a, b = map(int, input().split())
results = {
    '+': a + b,
    '-': a - b,
    '*': a * b
}

max_value = max(results.values())
best_ops = [op for op, val in results.items() if val == max_value]

if len(best_ops) != 1:
    print("NIE")
    exit()

op = best_ops[0]

# 음수이면 소괄호로 묶어 출력하는 함수
def format_num(x):
    return f"({x})" if x < 0 else str(x)

output = format_num(a) + op + format_num(b) + "=" + format_num(max_value)
print(output)

