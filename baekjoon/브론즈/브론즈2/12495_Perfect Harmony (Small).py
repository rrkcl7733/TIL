def is_harmonious(f, others):
    for note in others:
        if f % note != 0 and note % f != 0:
            return False
    return True


for t in range(int(input())):
    N, L, H = map(int, input().split())
    others = list(map(int, input().split()))
    
    result = "NO"
    for f in range(L, H + 1):
        if is_harmonious(f, others):
            result = str(f)
            break
    
    print(f"Case #{t + 1}: {result}")
