def in_div(t, d):
    for c in d:
        if int(c) == t:
            return 1
    return 0


r = int(input())
d = input()

t = 2
if r <= 1600:
    t = 3
elif r > 1900:
    t = 1

if in_div(t, d):
    print(t)
else:
    for c in d:
        print(f"{c}{'*' if int(c) > t else ''}")
