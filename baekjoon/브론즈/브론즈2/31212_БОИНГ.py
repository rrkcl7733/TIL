n = int(input())
reserved = input()
seats = ['A', 'B', 'C', 'D', 'E', 'F']
special_rows = ['1', '21']
all_seats = []
for row in range(1, 22):
    if str(row) in special_rows:
        if row == 1:
            all_seats.extend([str(row) + seat for seat in seats[3:]])
        else:
            all_seats.extend([str(row) + seat for seat in seats[3:5]])
    else:
        all_seats.extend([str(row) + seat for seat in seats])
all_seats.remove(reserved)
if n < len(all_seats):
    print(all_seats[n])
else:
    print('full')
