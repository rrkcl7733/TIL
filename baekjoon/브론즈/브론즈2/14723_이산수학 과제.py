N = int(input())

diag, count = 1, 0
while count + diag < N:
    count += diag
    diag += 1

pos = N - count

print(diag - pos + 1, pos)
