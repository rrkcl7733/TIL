def reverse_number(n):
    return int(str(n)[::-1])


for _ in range(int(input())):
    a, b = input().split()
    rev_a = reverse_number(a)
    rev_b = reverse_number(b)
    total = rev_a + rev_b
    print(reverse_number(total))
