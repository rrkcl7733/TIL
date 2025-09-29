a = int(input())
b = int(input())

count = 0
x = 1
while x**6 <= b:
    if a <= x**6 <= b:
        count += 1
    x += 1

print(count)
