from collections import Counter


for _ in range(int(input())):
    box_letters = input()
    
    box_counter = Counter(box_letters)
    for _ in range(int(input())):
        word_counter = Counter(input())
        # 각 문자에 대해 쿠키 박스에 충분한 수가 있는지 확인
        if all(box_counter[char] >= word_counter[char] for char in word_counter):
            print("YES")
        else:
            print("NO")
