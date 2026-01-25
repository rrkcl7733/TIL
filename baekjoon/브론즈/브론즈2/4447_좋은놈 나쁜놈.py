for _ in range(int(input())):
    name = input()
    lower_name = name.lower()
    g_count = lower_name.count('g')
    b_count = lower_name.count('b')

    if g_count > b_count:
        result = "GOOD"
    elif b_count > g_count:
        result = "A BADDY"
    else:
        result = "NEUTRAL"

    print(f"{name} is {result}")
