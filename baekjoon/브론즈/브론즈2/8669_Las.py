import sys


input = sys.stdin.readline
species_max = {}

for _ in range(int(input())):
    g, r = map(int, input().split())
    if r not in species_max or g > species_max[r]:
        species_max[r] = g

print(len(species_max))
