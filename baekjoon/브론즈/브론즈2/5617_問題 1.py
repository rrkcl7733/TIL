total = right = acute = obtuse = 0

while 1:
    a, b, c = sorted(map(int, input().split()))
    
    if a + b <= c: # 삼각형 안되면
        print(f"{total} {right} {acute} {obtuse}")
        exit()
    
    total += 1
    sum_sq = a*a + b*b
    c_sq = c*c
    
    if c_sq == sum_sq:
        right += 1
    elif c_sq < sum_sq:
        acute += 1
    else:
        obtuse += 1
