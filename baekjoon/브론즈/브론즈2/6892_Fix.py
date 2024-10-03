def is_fix_free(words):
    for i in range(3):
        for j in range(3):
            if i != j and (words[j].startswith(words[i]) or words[j].endswith(words[i])):
                return 0
    return 1


N = int(input())

for i in range(N):
    words = [input() for _ in range(3)]
    if is_fix_free(words):
        print('Yes')
    else:
        print('No')
