n = int(input())
binary_str = input()
gray = binary_str[0]
# 두 번째 비트부터 인접 비트의 XOR(덧셈의 자리올림 버림, 즉 mod 2 덧셈)을 구함
for i in range(1, n):
    # 두 인접 비트의 XOR을 문자열로 변환하여 결과에 추가
    gray += str(int(binary_str[i-1]) ^ int(binary_str[i]))

print(gray)
