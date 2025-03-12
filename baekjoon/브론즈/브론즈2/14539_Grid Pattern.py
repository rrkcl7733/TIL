def generate_grid(row, col, w, h):
    grid = []

    for r in range(row):
        grid.append('+' + ('-' * w + '+') * col)
        for _ in range(h):
            grid.append('|' + ('*' * w + '|') * col)

    grid.append('+' + ('-' * w + '+') * col)

    return '\n'.join(grid)


N = int(input())
for case_num in range(1, N + 1):
    row, col, w, h = map(int, input().split())

    print(f'Case #{case_num}:')
    print(generate_grid(row, col, w, h))
