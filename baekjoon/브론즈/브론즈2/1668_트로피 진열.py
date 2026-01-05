trophies = [int(input()) for _ in range(int(input()))]

# 왼쪽에서 보는 경우
left_count = 0
max_height = 0
for h in trophies:
    if h > max_height:
        left_count += 1
        max_height = h

# 오른쪽에서 보는 경우
right_count = 0
max_height = 0
for h in reversed(trophies):
    if h > max_height:
        right_count += 1
        max_height = h

print(left_count)
print(right_count)
