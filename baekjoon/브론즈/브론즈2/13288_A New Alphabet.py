mapping = {
    'A': '@',
    'B': '8',
    'C': '(',
    'D': '|)',
    'E': '3',
    'F': '#',
    'G': '6',
    'H': '[-]',
    'I': '|',
    'J': '_|',
    'K': '|<',
    'L': '1',
    'M': '[]\\/[]',
    'N': '[]\\[]',
    'O': '0',
    'P': '|D',
    'Q': '(,)',
    'R': '|Z',
    'S': '$',
    'T': "']['",
    'U': '|_|',
    'V': '\\/',
    'W': '\\/\\/',
    'X': '}{',
    'Y': '`/',
    'Z': '2'
}

for c in input():
    if c.isalpha():
        print(mapping[c.upper()], end='')
    else:
        print(c, end='')
