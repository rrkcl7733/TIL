import sys


for line in sys.stdin:
    if line == "":
        exit()
    a, rest = line.split('+')
    b, c = rest.split('=')
    if int(a[::-1]) + int(b[::-1]) == int(c[::-1]):
        print('True')
    else:
        print('False')
