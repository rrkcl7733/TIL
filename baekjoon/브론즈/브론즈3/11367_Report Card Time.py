for _ in range(int(input())):
    a, b = input().split()
    b = int(b)
    x = 'A+' if 96 < b else 'A' if 89 < b < 97 else 'B+' if 86 < b < 90 else 'B' if 79 < b < 87 else 'C+' if 76 < b < 80 else 'C' if 69 < b < 77 else 'D+' if 66 < b < 70 else 'D' if 59 < b < 67 else 'F'
    print(a, x)
