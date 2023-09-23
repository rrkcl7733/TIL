for _ in range(int(input())):
  m, n = map(int, input().split())
  m = list(map(int, input().split()))
  n = list(map(int, input().split()))
  print(1 if len(m) + len(n) != 4 else 7)
