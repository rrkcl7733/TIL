target = input()
s = ""

for i in range(1, int(target)+1):
    s += str(i)

pos = s.find(target) + 1
print(pos)
