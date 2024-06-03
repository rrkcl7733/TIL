answer = ""

for _ in range(int(input())):
    data = input().split()[1]
    answer += data[1:-1]

for i in answer.split("\\n"):
    print(i)
