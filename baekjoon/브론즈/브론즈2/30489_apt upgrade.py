n, m, k = map(int, input().split())
packages = sorted(list(map(int, input().split())), reverse=True)

downloaded = 0
for i in range(min(n, m + k)):
    downloaded += packages[i]

print(downloaded / sum(packages) * 100)
