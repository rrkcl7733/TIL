def get_ruler(country):
    last = country[-1].lower()
    if last == 'y':
        return "nobody"
    elif last in 'aeiou':
        return "a queen"
    else:
        return "a king"

for i in range(int(input())):
    country = input()
    ruler = get_ruler(country)
    print(f"Case #{i + 1}: {country} is ruled by {ruler}.")
