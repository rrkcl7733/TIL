a = str.maketrans('yaeiouYAEIOU', 'aeiouyAEIOUY')
for _ in range(int(input())):
    print(input().translate(a))
