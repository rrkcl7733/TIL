encoding_map = {
        ' ': '%20',
        '!': '%21',
        '$': '%24',
        '%': '%25',
        '(': '%28',
        ')': '%29',
        '*': '%2a'
}

while 1:
    s = input()
    if s == '#':
        exit()
    encoded_string = ''
    for char in s:
        if char in encoding_map:
            encoded_string += encoding_map[char]
        else:
            encoded_string += char
    print(encoded_string)
