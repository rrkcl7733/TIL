n = int(input())
t1 = input()
t2 = input()
x = 0
for i in range(n):
  moves_up = (ord(t2[i]) - ord(t1[i]) + 26) % 26
  moves_down = (ord(t1[i]) - ord(t2[i]) + 26) % 26
  x += min(moves_up, moves_down)
print(x)
