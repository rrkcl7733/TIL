int(input())
file_sizes = list(map(int, input().split()))
cluster_size = int(input())

total_space = sum(
    0 if f == 0 else ((f + cluster_size - 1) // cluster_size) * cluster_size
    for f in file_sizes
)

print(total_space)
