for _ in range(int(input())):
    a, op, b, _, c = input().split()
    a, b = int(a), int(b)

    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    else:
        result = a // b  #항상 나누어떨어짐

    if result == int(c):
        print("correct")
    else:
        print("wrong answer")
