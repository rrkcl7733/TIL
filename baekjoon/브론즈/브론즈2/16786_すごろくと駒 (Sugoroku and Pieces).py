input()
positions = list(map(int, input().split()))
input()
moves = list(map(int, input().split()))

occupied = set(positions)

for a in moves:
    idx = a - 1  # 말 번호는 1부터 시작
    current_pos = positions[idx]
    next_pos = current_pos + 1

    if next_pos <= 2019 and next_pos not in occupied:
        occupied.remove(current_pos)
        occupied.add(next_pos)
        positions[idx] = next_pos

for pos in positions:
    print(pos)
