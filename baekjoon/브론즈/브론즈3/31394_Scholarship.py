num_scores = int(input())
scores = [int(input()) for _ in range(num_scores)]

score_set = set(scores)
average_score = sum(scores) / num_scores

if 3 in score_set:
    ans = "None"
elif len(score_set) == 1 and 5 in score_set:
    ans = "Named"
elif average_score >= 4.5:
    ans = "High"
else:
    ans = "Common"

print(ans)
