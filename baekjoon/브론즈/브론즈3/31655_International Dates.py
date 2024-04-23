day, month, year = map(int, input().split('/'))
print('EU' if day > 12 else 'US' if month > 12 else 'either')
