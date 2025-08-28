from collections import Counter


n, code, guess = input().split()
r = s = 0

unmatched_code = []
unmatched_guess = []

# 먼저 정확히 일치하는 문자(r)
for i in range(int(n)):
    if code[i] == guess[i]:
        r += 1
    else:
        unmatched_code.append(code[i])
        unmatched_guess.append(guess[i])

# 색상만 일치하는 문자(s)
code_counter = Counter(unmatched_code)
guess_counter = Counter(unmatched_guess)

for color in guess_counter:
    s += min(code_counter.get(color, 0), guess_counter[color])

print(r, s)

