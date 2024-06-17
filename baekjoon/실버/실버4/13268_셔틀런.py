def get_section(local_dist, phase):
    diff = abs(local_dist - phase * 5) // 5
    print(phase - diff)


n = int(input()) % 100

if n < 10:
    get_section(n, 1)
elif n < 30:
    get_section(n - 10, 2)
elif n < 60:
    get_section(n - 30, 3)
else:
    get_section(n - 60, 4)
