while 1:
    word = input()
    if word == "quit!":
        exit()
    if len(word) > 4 and word.endswith("or") and word[-3].lower() not in 'aeiouy':
        # 미국식 철자일 경우 캐나다식으로 변환
        word = word[:-2] + "our"
    print(word)
