N = int(input())
answers = input()

patterns = {
    "Adrian": "ABC",
    "Bruno": "BABC",
    "Goran": "CCAABB"
}

scores = {}
for name, pattern in patterns.items():
    count = 0
    for i in range(N):
        if answers[i] == pattern[i % len(pattern)]:
            count += 1
    scores[name] = count

max_score = max(scores.values())
print(max_score)
for name in ["Adrian", "Bruno", "Goran"]:
    if scores[name] == max_score:
        print(name)
