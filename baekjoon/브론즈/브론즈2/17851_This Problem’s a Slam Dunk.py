state_u_sorted = sorted(list(map(int, input().split())), reverse=True)
u_state_sorted = sorted(list(map(int, input().split())), reverse=True)

count = 0
for s, u in zip(state_u_sorted, u_state_sorted):
    if s > u:
        count += 1
print(count)
