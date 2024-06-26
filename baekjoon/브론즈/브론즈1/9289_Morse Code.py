codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]


def find(code):
    for c in range(ord('A'), ord('Z')+1):
        if codes[c - ord('A')] == code:
            return chr(c)
    return '0'


for i in range(int(input())):
    print(f"Case {i + 1}: ", end='')
    for j in input().split():
        print(find(j), end='')
    print()
