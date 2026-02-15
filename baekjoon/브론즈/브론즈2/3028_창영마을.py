pos = 1

for m in input():
    if m == 'A':
        if pos == 1: pos = 2
        elif pos == 2: pos = 1
    elif m == 'B':
        if pos == 2: pos = 3
        elif pos == 3: pos = 2
    else:
        if pos == 1: pos = 3
        elif pos == 3: pos = 1

print(pos)
