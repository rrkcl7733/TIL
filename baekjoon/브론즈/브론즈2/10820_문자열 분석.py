import sys

for line in sys.stdin:
    line = line.rstrip("\n")
    lower = upper = digit = space = 0
    for ch in line:
        if ch.islower():
            lower += 1
        elif ch.isupper():
            upper += 1
        elif ch.isdigit():
            digit += 1
        else:
            space += 1
    print(lower, upper, digit, space)
