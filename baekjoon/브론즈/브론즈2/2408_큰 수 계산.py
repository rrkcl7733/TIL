N = int(input())
tokens = [input() for _ in range(2 * N - 1)]

# 1차 처리: *, /
stack = []
i = 0
while i < len(tokens):
    if tokens[i] in ('*', '/'):
        op = tokens[i]
        prev = int(stack.pop())
        nxt = int(tokens[i + 1])

        stack.append(prev * nxt if op == '*' else prev // nxt)
        i += 2
    else:
        stack.append(tokens[i])
        i += 1

# 2차 처리: +, -
result = int(stack[0])
i = 1
while i < len(stack):
    op = stack[i]
    nxt = int(stack[i + 1])
    if op == '+':
        result += nxt
    else:
        result -= nxt
    i += 2

print(result)
