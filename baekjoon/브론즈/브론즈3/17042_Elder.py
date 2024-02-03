label = input()
n = int(input())

obeys = set(label)

for _ in range(n):
    z1, z2 = input().split()

    if z2 == label:
        label = z1
        obeys.add(z1)

print(label)
print(len(obeys))
