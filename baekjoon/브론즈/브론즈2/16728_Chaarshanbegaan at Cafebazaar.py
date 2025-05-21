score = 0

for _ in range(int(input())):
    x, y = map(int, input().split())
    d = (x * x + y * y) ** .5

    if d <= 10:
        score += 10
    elif d <= 30:
        score += 9
    elif d <= 50:
        score += 8
    elif d <= 70:
        score += 7
    elif d <= 90:
        score += 6
    elif d <= 110:
        score += 5
    elif d <= 130:
        score += 4
    elif d <= 150:
        score += 3
    elif d <= 170:
        score += 2
    elif d <= 190:
        score += 1


print(score)
