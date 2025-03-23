N = int(input())

if N <= 10:
    print(1)
    exit()

card = '1'
while N >= int(card):
    card += '1'

print(len(str(int(card) // 10)))
