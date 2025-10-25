for _ in range(int(input())):
    k = int(input())
    restaurant = input()
    menu = [input() for _ in range(k)]

    if "pea soup" in menu and "pancakes" in menu:
        print(restaurant)
        break

else:
    print("Anywhere is fine I guess")
