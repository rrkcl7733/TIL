def alphabet_distance(x, y):
    x_val = ord(x) - ord('A') + 1
    y_val = ord(y) - ord('A') + 1

    if y_val >= x_val:
        return y_val - x_val
    else:
        return (y_val + 26) - x_val


for _ in range(int(input())):
    word1, word2 = input().split()
    distances = [alphabet_distance(word1[i], word2[i]) for i in range(len(word1))]
    print("Distances:", *distances)

