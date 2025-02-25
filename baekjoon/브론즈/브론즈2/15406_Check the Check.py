import sys


input = sys.stdin.readline
total_calculated = 0

while 1:
    if input() == 'TOTAL':
        total_given = int(input())
        print('PAY' if total_given <= total_calculated else 'PROTEST')
        exit()

    price, quantity = map(int, input().split())
    total_calculated += price * quantity
