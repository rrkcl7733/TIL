t = ("1QAZ", "2WSX", "3EDC", "4RFV5TGB", "6YHN7UJM", "8IK,", "9OL.", "0P;/-['=]")
ans = [0] * 8
for c in input():
    for i in range(8):
        if c in t[i]:
            ans[i] += 1
print(*ans, sep='\n')
