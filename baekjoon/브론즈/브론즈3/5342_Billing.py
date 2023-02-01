d = {'Paper': 57.99, 'Printer': 120.5, 'Planners': 31.25, 'Binders': 22.5, 'Calendar': 10.95, 'Notebooks': 11.2, 'Ink': 66.95}
x = 0
while 1:
    a = input()
    if a == 'EOI':
        print(f'${x:.2f}')
        exit()
    x += d[a]
