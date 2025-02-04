def count_below_average(n, incomes):
    average_income = sum(incomes) / n
    count = sum(1 for income in incomes if income <= average_income)
    return count


while True:
    n = int(input())
    if not n:
        exit()
    incomes = list(map(int, input().split()))
    print(count_below_average(n, incomes))
