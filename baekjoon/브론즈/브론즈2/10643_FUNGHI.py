pizza = [int(input()) for _ in range(8)]
ans = 0

pizza += pizza[:3:]
for i in range(8):
    ans = max(ans, sum(pizza[i:i+4]))

print(ans)
