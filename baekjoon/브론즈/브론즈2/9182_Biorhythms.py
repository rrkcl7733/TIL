c = 1
while 1:
    p, e, i, d = map(int, input().split())
    
    if p == -1:
        exit()
    
    triple_peak = (5544 * p + 14421 * e + 1288 * i) % 21252

    if triple_peak <= d:
        triple_peak += 21252

    result = triple_peak - d

    print(f'Case {c}: the next triple peak occurs in {result} days.')
    c += 1
