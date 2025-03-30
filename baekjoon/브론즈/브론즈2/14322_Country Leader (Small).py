for i in range(int(input())):
    names = [input() for _ in range(int(input()))]
    leader_name = None
    max_unique_letters = -1

    for name in names:
        unique_letters = len(set(name.replace(" ", "")))

        if (unique_letters > max_unique_letters) or \
                (unique_letters == max_unique_letters and name < leader_name):
            leader_name = name
            max_unique_letters = unique_letters

    print(f'Case #{i + 1}: {leader_name}')
