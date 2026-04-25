for i in range(int(input())):
    words = input().split()
    print(f"Case #{i + 1}: {" ".join(reversed(words))}")
