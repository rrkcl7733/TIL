import sys
input = sys.stdin.readline

pattern = input()
results = []
for _ in range(int(input())):
    code = input().strip()
    for p_char, c_char in zip(pattern, code):
        # '*'이면 ANY, 그 외에는 정확히 일치해야 함
        if p_char != '*' and p_char != c_char:
            break
    else:
        results.append(code)

print(len(results))
for code in results:
    print(code)
