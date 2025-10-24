def is_comparable(w1, h1, w2, h2):
    if (w1 <= w2 and h1 <= h2) or (h1 <= w2 and w1 <= h2):
        return True

    if (w2 <= w1 and h2 <= h1) or (h2 <= w1 and w2 <= h1):
        return True
    return False

def count_incomparable_pairs(rectangles):
    sizes = [(x2 - x1, y2 - y1) for x1, y1, x2, y2 in rectangles]
    count = 0
    n = len(sizes)
    for i in range(n):
        for j in range(i + 1, n):
            w1, h1 = sizes[i]
            w2, h2 = sizes[j]
            if not is_comparable(w1, h1, w2, h2):
                count += 1
    return count


rectangles = [tuple(map(int, input().split())) for _ in range(int(input()))]
print(count_incomparable_pairs(rectangles))
