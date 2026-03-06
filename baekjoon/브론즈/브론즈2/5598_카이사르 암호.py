result = ""

for ch in input():
    idx = ord(ch) - ord('A')
    # 3글자 앞으로 이동 (복호화)
    new_idx = (idx - 3) % 26
    result += chr(new_idx + ord('A'))

print(result)
