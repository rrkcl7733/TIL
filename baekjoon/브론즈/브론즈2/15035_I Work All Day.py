N = int(input())
H = list(map(int, input().split()))
T = int(input())

min_waste = float('inf')
best_setting = 0

for setting in H:
    waste = T % setting
    if waste < min_waste:
        min_waste = waste
        best_setting = setting

print(best_setting)
