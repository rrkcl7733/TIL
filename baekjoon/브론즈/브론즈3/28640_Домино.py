a, b = input().split('|')
c, d = input().split('|')
x = (len(c), len(d))
print('Yes' if len(a) in x or len(b) in x else 'No')
