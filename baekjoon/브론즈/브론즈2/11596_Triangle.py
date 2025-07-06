def is_right_and_legs(sides):
    sides.sort()
    a, b, c = sides
    return (a*a + b*b == c*c, (a, b))


tri1 = list(map(int, input().split()))
tri2 = list(map(int, input().split()))

ok1, legs1 = is_right_and_legs(tri1)
ok2, legs2 = is_right_and_legs(tri2)

if ok1 and ok2 and legs1 == legs2:
    print("YES")
else:
    print("NO")
