for _ in range(int(input())):
    words = input().split()
    yoda_sentence = words[2:] + words[:2]
    print(*yoda_sentence)
