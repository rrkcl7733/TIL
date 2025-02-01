n = int(input())
data_sets = [list(map(int, input().split())) for _ in range(n)]
for data in data_sets:
    word = ''
    for num in data:
        if 64 < num < 91 or 96 < num < 123:
            word += chr(num).lower()
        else:
            word += '-'
    print(word[1:] + word[0] + 'ay')
