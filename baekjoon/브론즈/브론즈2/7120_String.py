s = ''
for ch in input():
    if not s or s[-1] != ch:
        s += ch
print(s)
