for t in range(int(input())):
    S = input()
    answer = 1
    for i in range(len(S)):
        possible_letters = set()
        for j in range(i - 1, i + 2):
            if 0 <= j < len(S):
                possible_letters.add(S[j])
        answer = (answer * len(possible_letters)) % 1_000_000_007
    print(f"Case #{t + 1}: {answer}")
