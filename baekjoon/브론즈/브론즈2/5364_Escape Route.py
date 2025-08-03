import math

current, *planets = [tuple(map(int, input().split())) for _ in range(int(input()))]

min_dist = float('inf')
closest_planet = None

for planet in planets:
    dist = math.sqrt((current[0] - planet[0])**2 + (current[1] - planet[1])**2)
    if dist < min_dist:
        min_dist = dist
        closest_planet = planet

print(f"{current[0]} {current[1]}")
print(f"{closest_planet[0]} {closest_planet[1]}")
print(f"{min_dist:.2f}")
