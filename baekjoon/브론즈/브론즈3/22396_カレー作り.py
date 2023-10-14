while 1:
    r0, w0, c, r = map(int, input().split())
    if not c:
        break
    d = r0 / w0
    if d >= c:
        print(0)
    else:
        required_density = c - d
        required_roux = required_density * w0
        required_roux_count = required_roux // r
        if required_roux % r:
            required_roux_count += 1
        print(int(required_roux_count))
