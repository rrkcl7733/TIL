from decimal import Decimal


a1, a2, a3, a4 = map(int, input().split())
print(int(Decimal(min(a1, a2) + min(a3, a4)).sqrt()))
