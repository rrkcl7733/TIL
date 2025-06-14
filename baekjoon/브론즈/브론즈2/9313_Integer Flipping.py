def flip_integer(num):
    # 입력된 숫자를 32비트 이진수 문자열로 변환 (앞에 0으로 채움)
    binary_str = format(num, "032b")
    reversed_str = binary_str[::-1]
    return int(reversed_str, 2)


while 1:
    line = int(input())
    if line < 0:
        break
    result = flip_integer(line)
    print(result)
