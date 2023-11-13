import sys


input = sys.stdin.readline
while 1:
  n, m = map(int, input().split())
  if not n:
      break

  found_players = set()
  for _ in range(n - 2):
      found_players.add(int(input()))

  for i in range(1, n + 1):
      if i not in found_players and i != m:
          print(i)
          break
