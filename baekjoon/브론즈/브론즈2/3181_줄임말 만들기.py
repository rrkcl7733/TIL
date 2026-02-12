sentence = input().split()

abbr = sentence[0][0]
for word in sentence[1:]:
    if word not in {"i", "pa", "te", "ni", "niti", "a", "ali", "nego", "no", "ili"}:
        abbr += word[0]

print(abbr.upper())
