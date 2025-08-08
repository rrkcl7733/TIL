import math

def min_surface_area(n):
    min_area = float('inf')
    
    for l in range(1, int(n ** (1/3)) + 2):
        if n % l != 0:
            continue
        rem1 = n // l
        for w in range(1, int(math.sqrt(rem1)) + 2):
            if rem1 % w != 0:
                continue
            h = rem1 // w
            area = 2 * (l*w + w*h + h*l)
            if area < min_area:
                min_area = area
    return min_area


for _ in range(int(input())):
    print(min_surface_area(int(input())))

