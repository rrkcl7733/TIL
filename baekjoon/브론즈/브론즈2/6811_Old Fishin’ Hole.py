trout_points = int(input())
pike_points = int(input())
pickerel_points = int(input())
total_points = int(input())

count = 0

for trout in range(total_points // trout_points + 1):
    for pike in range(total_points // pike_points + 1):
        for pickerel in range(total_points // pickerel_points + 1):
            total = trout * trout_points + pike * pike_points + pickerel * pickerel_points
            if 0 < total <= total_points:
                print(f"{trout} Brown Trout, {pike} Northern Pike, {pickerel} Yellow Pickerel")
                count += 1

print(f"Number of ways to catch fish: {count}")
