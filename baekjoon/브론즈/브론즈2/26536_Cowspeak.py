for _ in range(int(input())):
    s = input().split()
    answer = ""

    for i in s:
        answer += chr(i.count('M') * 16 + i.count('O'))

    print(answer)
