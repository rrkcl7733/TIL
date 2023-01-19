a = input()

x = ''

d = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5'}

for i in a:
    print(d[i] if i in d.keys() else i, end='')
