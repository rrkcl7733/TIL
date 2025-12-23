input()
seats = list(map(int, input().split()))

occupied = set()
rejected = 0

for seat in seats:
    if seat in occupied:
        rejected += 1
    else:
        occupied.add(seat)

print(rejected)
