earthlings = aboriginals = others = 0

for _ in range(int(input())):
    answer = input()
    if 'blue' in answer and 'black' in answer:
        earthlings += 1
    elif 'white' in answer and 'gold' in answer:
        aboriginals += 1
    else:
        others += 1

total = earthlings + aboriginals + others
print(earthlings / total * 100)
print(aboriginals / total * 100)
print(others / total * 100)
