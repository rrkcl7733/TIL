num = input().split()

for _ in range(int(input())):
    a = [num[int(i)] for i in input().strip()]

    print(max(a))
