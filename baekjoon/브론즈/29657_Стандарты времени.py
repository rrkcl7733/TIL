a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())
h1, m1, s1 = map(int, input().split())

total_seconds = h1 * b1 * c1 + m1 * c1 + s1

h2 = total_seconds // (b2 * c2)
total_seconds %= (b2 * c2)
m2 = total_seconds // c2
s2 = total_seconds % c2
print(h2, m2, s2)
