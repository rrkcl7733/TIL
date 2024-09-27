M, P = map(int, input().split())
print(*eval("M-(M:=M // P * ~-P)," * P)) #P번 반복
print(M)
