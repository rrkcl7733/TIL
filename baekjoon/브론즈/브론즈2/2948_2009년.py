D, M = map(int, input().split())

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekdays = ['Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday']

days = sum(days_in_month[:M-1]) + (D-1)
print(weekdays[days % 7])
