n = int(input())
for i in range(n):
    words = input().rstrip('\n').split(' ')
    # 4글자인 단어만 ****로 치환
    for j, w in enumerate(words):
        if len(w) == 4:
            words[j] = '****'
    print(' '.join(words))
    # 마지막 줄 뒤에는 빈 줄을 넣지 않음
    if i != n - 1:
        print()
