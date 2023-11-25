a, b, c = map(int, input().split())
bought = False
spent = 0
current = input()

while current != "end":
    if bought:
        print("self")
    elif spent + (a - c) > b:
        bought = True
        print("buy")
    else:
        spent += (a - c)
        print("airline")
    current = input()
