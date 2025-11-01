def is_dickensian(word):
    left = set("qwertasdfgzxcvb")
    right = set("yuiophjklnm")

    def hand(c):
        if c in left:
            return "L"
        elif c in right:
            return "R"
        else:
            return "?"

    prev_hand = hand(word[0])
    for c in word[1:]:
        current_hand = hand(c)
        if current_hand == prev_hand:
            return "no"
        prev_hand = current_hand
    return "yes"


word = input()
print(is_dickensian(word))
