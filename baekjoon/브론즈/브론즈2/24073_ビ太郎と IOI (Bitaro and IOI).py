input()
S = input()

found_I = False   # 첫 번째 I를 찾았는지
found_O = False   # I 이후 O를 찾았는지

for ch in S:
    if not found_I:
        if ch == 'I':
            found_I = True
    elif not found_O:
        if ch == 'O':
            found_O = True
    else:
        # I와 O를 이미 찾은 상태에서 다시 I가 나오면 IOI 완성
        if ch == 'I':
            print("Yes")
            break
else:
    print("No")
