A = int(input())
B = int(input())

tie = min(A, B)
a = (A - tie) // 2
b = (B - tie) // 2

if (a * 2 + tie, b * 2 + tie) == (A, B):
    if tie > 1:
        print("Undefined")
    else:
        print(a, b, tie, end='\n')
else:
    print("Error")
