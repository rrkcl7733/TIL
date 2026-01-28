import sys

for line in sys.stdin:
    line = line.rstrip()
    if line == "#":
        break
    total = 0
    for i, ch in enumerate(line, start=1):
        if ch == " ":
            continue
        total += i * (ord(ch) - ord('A') + 1)
    print(total)
