s = input()
t = ("PER" * ((len(s) + 2) // 3))[:len(s)]
# 서로 다른 자리 수 세기
print(sum(1 for a, b in zip(s, t) if a != b))
