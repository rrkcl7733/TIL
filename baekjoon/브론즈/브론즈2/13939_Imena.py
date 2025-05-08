def is_name(word):
    # 만약 단어가 문장부호로 끝난다면 ('.', '?', '!') 빼준다.
    if word[-1] in ".?!":
        core = word[:-1]
    else:
        core = word

    if not core or not core[0].isupper():
        return False
    
    for ch in core[1:]:
        if not ch.islower():
            return False
    return True


input()
words = input().split()
current_sentence = []

for word in words:
    current_sentence.append(word)
    # 현재 단어가 문장부호('.', '?' '!' 중 하나)로 끝나면, 한 문장이 종료된 것임.
    if word[-1] in ".?!":
        # 문장 내의 각 단어가 이름 조건을 만족하는지 확인
        count = sum(1 for w in current_sentence if is_name(w))
        print(count)
        current_sentence = []
