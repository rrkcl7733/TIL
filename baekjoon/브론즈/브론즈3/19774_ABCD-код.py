for _ in range(int(input())):
  x = input()
  print('YES' if ((int(x[0]) * 10 + int(x[1]))** 2 + (int(x[2]) * 10 + int(x[3])) ** 2) % 7 == 1 else 'NO')
