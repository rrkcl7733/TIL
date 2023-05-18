x = 0
input()
a = map(int, input().split())
input()
b = list(map(int, input().split()))
for i in a:
    x += i
    if x in b:
        x = 0
print(x)
