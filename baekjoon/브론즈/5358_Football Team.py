while 1:
    try:
        x = ''
        for i in input():
            x = x + 'e' if i == 'i' else x + 'i' if i == 'e' else x + 'E' if i == 'I' else x + 'I' if i == 'E' else x + i
        print(x)
    except EOFError:
        exit()
