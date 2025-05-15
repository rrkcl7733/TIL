for t in range(int(input())):
    input()
    key = input()
    responses = input()

    wrong = sum(1 for a, b in zip(key, responses) if a != b)
    print(f"Case {t + 1}: {wrong}")
