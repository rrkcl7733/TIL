for _ in range(int(input())):
    s = input().replace(" ", "")
    score = sum(ord(ch) - ord('A') + 1 for ch in s)
    if score == 100:
        print("PERFECT LIFE")
    else:
        print(score)
