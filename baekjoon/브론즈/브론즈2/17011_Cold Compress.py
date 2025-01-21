for _ in range(int(input())):
    s = input().strip()
    encoded_string = ""
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            i += 1
            count += 1
        encoded_string += str(count) + " " + s[i] + " "
        i += 1
    print(encoded_string.strip())
