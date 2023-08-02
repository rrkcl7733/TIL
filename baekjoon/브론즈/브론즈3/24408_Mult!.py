x = 0
for _ in range(int(input())):
    n = int(input())
    if not x:
        x = n
    else:
        if not n % x:
            print(n)
            x = 0
 
