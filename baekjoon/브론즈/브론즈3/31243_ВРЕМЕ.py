def time_diff(start_h, start_m, end_h, end_m):
    start = start_h * 60 + start_m
    end = end_h * 60 + end_m
    if end < start:
        end += 24 * 60
    return end - start

times = [0] * 3
for i in range(3):
    start_h, start_m, end_h, end_m = map(int, input().split())
    times[i] = time_diff(start_h, start_m, end_h, end_m)

min_time = min(times)
max_time = max(times)

print(f"{min_time // 60}:{min_time % 60:02d}")
print(f"{max_time // 60}:{max_time % 60:02d}")
