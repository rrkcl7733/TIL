def determine_ruler(country):
    last_char = country[-1].lower()
    if last_char == 'y':
        return "nobody"
    elif last_char in 'aeiou':
        return "a queen"
    else:
        return "a king"


for i in range(int(input())):
    country = input().strip()
    ruler = determine_ruler(country)
    print(f"Case #{i + 1}: {country} is ruled by {ruler}.")
