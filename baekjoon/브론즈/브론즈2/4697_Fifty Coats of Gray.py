while 1:
    first_line = list(map(int, input().split()))
    if not first_line[0]:
        exit()
    n, width, length, height, area, m = first_line
    # (4개의 벽 + 천장)
    total_paint_area = n * (2 * width * height + 2 * length * height + width * length)

    # 창문 및 문 면적 
    for _ in range(m):
        w, h = map(int, input().split())
        total_paint_area -= n * (w * h)

    # 필요한 페인트 통 수
    cans_of_paint = (total_paint_area + area - 1) // area
    print(cans_of_paint)
