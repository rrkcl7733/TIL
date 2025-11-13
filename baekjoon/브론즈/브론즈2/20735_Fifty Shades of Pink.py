import sys
input = sys.stdin.readline


count = 0
for _ in range(int(input())):
    label = input().lower()
    if "pink" in label or "rose" in label:
        count += 1

if count < 1:
    print("I must watch Star Wars with my daughter")
else:
    print(count)
