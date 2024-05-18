n = int(input())
string = input()

for i in range(1, n):
    if string[0] != string[i]:
        print("Yes")
        print(1, i+1, 1)
        break
else:
    print("No")
