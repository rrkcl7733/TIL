def find_bully_and_victim(class_data):
    volumes = []
    for entry in class_data:
        x, y, z, name = entry
        volume = int(x) * int(y) * int(z)
        volumes.append((volume, name))
    
    # 피해자: 최소 부피, 가해자: 최대 부피
    victim = min(volumes)
    bully = max(volumes)
    return f"{bully[1]} took clay from {victim[1]}."



while 1:
    n = int(input())
    if n < 1:
        exit()

    parts = [input().split() for _ in range(n)]
    print(find_bully_and_victim(parts))

