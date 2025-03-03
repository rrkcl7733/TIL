def move_station(current_station, direction, steps):
    if direction == 'A':
        return (current_station - steps - 1) % 8 + 1
    else:
        return (current_station + steps - 1) % 8 + 1


start = int(input())
stations = list(range(1, 9))
visited_stations = [start]
current_station = start

while (step := input()) != '#':
    direction, move_steps = step[0], int(step[1])
    next_station = move_station(current_station, direction, move_steps)
    visited_stations.append(next_station)
    current_station = next_station

if len(set(visited_stations)) < 5 or len(visited_stations) != len(set(visited_stations)):
    visited_stations.append('reject')

print(*visited_stations)
