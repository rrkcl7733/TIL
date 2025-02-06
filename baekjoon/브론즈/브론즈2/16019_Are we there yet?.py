def calculate_distances(distances):
    n = len(distances) + 1
    distance_table = [[0] * n for _ in range(n)]

    for i in range(1, n):
        distance_table[0][i] = distance_table[0][i - 1] + distances[i - 1]

    for i in range(1, n):
        for j in range(i + 1, n):
            distance_table[i][j] = distance_table[0][j] - distance_table[0][i]

    for i in range(n):
        for j in range(n):
            distance_table[j][i] = distance_table[i][j]

    return distance_table


distances = list(map(int, input().split()))
distance_table = calculate_distances(distances)

for row in distance_table:
    print(*row)
