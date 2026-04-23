A = input()
B = input()

n = len(A)

and_result = ''.join('1' if A[i] == '1' and B[i] == '1' else '0' for i in range(n))
or_result = ''.join('1' if A[i] == '1' or B[i] == '1' else '0' for i in range(n))
xor_result = ''.join('1' if A[i] != B[i] else '0' for i in range(n))
not_a_result = ''.join('0' if A[i] == '1' else '1' for i in range(n))
not_b_result = ''.join('0' if B[i] == '1' else '1' for i in range(n))

print(and_result)
print(or_result)
print(xor_result)
print(not_a_result)
print(not_b_result)
